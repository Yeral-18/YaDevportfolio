# Publish flow — API ↔ Runner bridge

> Canonical architecture doc. The API sub-repo also keeps a copy at
> `api/docs/publish-flow.md` co-located with the controller code; treat
> this file as the source of truth when they drift.

## Sequence

```
┌──────────┐                    ┌────────────┐                   ┌────────────┐
│  Studio  │                    │  Laravel   │                   │   Runner   │
│ (admin)  │                    │   API      │                   │  (Node)    │
└────┬─────┘                    └─────┬──────┘                   └─────┬──────┘
     │                                │                                │
     │ POST /v1/tenants/{id}/         │                                │
     │      publishes                 │                                │
     │ Authorization: Bearer …        │                                │
     │───────────────────────────────►│                                │
     │                                │ INSERT publishes               │
     │                                │   status=pending               │
     │                                │                                │
     │                                │ POST /webhook/build            │
     │                                │ X-YaDev-Signature: sha256=…    │
     │                                │ body={publishId,tenantId,…}    │
     │                                │───────────────────────────────►│
     │                                │                                │ verify HMAC
     │                                │                                │ enqueue BullMQ
     │                                │ 202 { jobId }                  │
     │                                │◄───────────────────────────────│
     │                                │                                │
     │                                │ UPDATE publishes               │
     │                                │   status=queued                │
     │                                │   runner_job_id=jobId          │
     │                                │   started_at=now               │
     │                                │                                │
     │ 202 { data: Publish }          │                                │
     │◄───────────────────────────────│                                │
     │                                │                                │
     │  (polls every 2-3s)            │                                │ … build runs …
     │ GET /v1/.../publishes/{id}     │                                │
     │───────────────────────────────►│                                │
     │ 200 { data: Publish }          │                                │
     │◄───────────────────────────────│                                │
     │                                │                                │
     │                                │  POST /v1/tenants/{id}/        │
     │                                │       publishes/{id}/complete  │
     │                                │  X-YaDev-Signature: sha256=…   │
     │                                │  body={status,build_log_url?,  │
     │                                │        error_message?}         │
     │                                │◄───────────────────────────────│
     │                                │ verify HMAC                    │
     │                                │ tenancy()->initialize          │
     │                                │ UPDATE publishes               │
     │                                │   status=completed|failed      │
     │                                │   completed_at=now             │
     │                                │ tenancy()->end                 │
     │                                │ 200 { data: Publish }          │
     │                                │───────────────────────────────►│
```

## Auth

Both directions use HMAC-SHA256 over the **raw body** with a header:

```
X-YaDev-Signature: sha256=<64 lowercase hex chars>
```

* API → Runner: signed with `RUNNER_WEBHOOK_SECRET`.
* Runner → API: signed with `RUNNER_CALLBACK_SECRET`. Defaults to
  `RUNNER_WEBHOOK_SECRET` when unset (Fase 0-2 simplicity); split them
  in production for stricter blast-radius isolation.

The `/complete` endpoint deliberately bypasses Sanctum and the
`tenant.path` middleware — both require a bearer token, which the
Runner doesn't have. Tenant context is initialised inline in
`PublishController::complete()`.

## State machine

```
       ┌──────────┐
       │ pending  │  ← created by POST /publishes
       └────┬─────┘
            │ dispatcher succeeded
            ▼
       ┌──────────┐
       │ queued   │  ← Runner returned 202 + jobId
       └────┬─────┘
            │ Runner calls /complete with status=...
            ├──────────────► completed   (terminal)
            ├──────────────► failed      (terminal)
            ▼
       (worker logs would also surface `building`, but the API never
        sees that state today — Runner emits it only inside its own
        BullMQ progress events.)

       ┌──────────┐
       │ pending  │
       └────┬─────┘
            │ dispatcher exhausted retries
            ▼
       ┌──────────┐
       │  failed  │  (terminal, with error_message populated by API)
       └──────────┘
```

## Race conditions and idempotency

| Scenario                                    | Response          | Rationale                                                  |
|---------------------------------------------|-------------------|------------------------------------------------------------|
| `/complete` for unknown publishId           | **404**           | No leak — same as cross-tenant access pattern (CLAUDE §1). |
| `/complete` with a missing X-YaDev-Sig      | **401**           | HMAC required.                                             |
| `/complete` for already-terminal publish    | **409**           | Idempotent — caller can ignore. Body includes both states. |
| Retried webhook from API to Runner          | Runner dedupes    | publishId is in body → BullMQ jobId derives uniquely.      |
| Runner calls /complete before /publishes row commits | impossible | Same MySQL connection writes the row before the HTTP call. |

The 409 path applies regardless of whether the reported terminal
status matches the stored one. We never silently "upgrade" or "rewrite"
a terminal record — that would erase audit history.

## Failure handling

* **Dispatcher network/timeout failure** → Publish row transitions
  `pending → failed`, `error_message` captures the exception. The
  controller still returns 202 to the studio because the row exists
  and the operator can retry from the dashboard.
* **Runner job failure mid-build** → Runner posts `/complete` with
  `status=failed` and `error_message`. We surface that string verbatim
  in the dashboard.
* **API down when Runner tries to /complete** → Runner retries with
  exponential backoff (its own concern). The publish row stays in
  `queued` until the next Runner heartbeat. TODO: stale-publish
  reaper job (post-MVP) to mark publishes stuck > 30min as failed.

## TODOs (post-MVP)

1. Replace inline `dispatcher->dispatch()` with a queued job on the
   `publish` queue once Horizon supervisor is wired in production.
   Today it runs synchronously inside `PublishController::store()`,
   which is acceptable in Fase 0-2 because the Runner is on the same
   host and the timeout is 5s + 1 retry — the studio sees ~6s worst
   case latency on POST.
2. Add jitter (e.g. `100..400ms`) and configurable retry count to the
   dispatcher's backoff once we measure real failure modes. The
   current `100ms * attempt#` ramp is conservative for local dev.
3. Emit metrics (`publish.dispatched`, `publish.completed`,
   `publish.failed`, `publish.duration_ms`) once Horizon metrics
   plugin is wired.
4. Stale-publish reaper command: `php artisan publish:reap` — marks
   publishes stuck in queued/building > 30min as failed, with a
   distinguishable `error_message` so the dashboard can offer a retry
   button.
5. Diverge `RUNNER_CALLBACK_SECRET` from `RUNNER_WEBHOOK_SECRET` in
   production deployment templates. Today the config defaults to the
   webhook secret when unset for Fase 0-2 simplicity.
