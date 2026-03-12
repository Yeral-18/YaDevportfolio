# Office 365 Email Configuration for ECOMAG Contact Form

## Option A: Microsoft Graph API (Recommended)

### 1. Azure AD App Registration

1. Go to [Azure Portal](https://portal.azure.com) > Azure Active Directory > App registrations > New registration.
2. Name: `ECOMAG-Web-ContactForm`
3. Supported account types: "Accounts in this organizational directory only"
4. Click **Register**.

### 2. API Permissions

1. In the app registration, go to **API permissions** > Add a permission.
2. Select **Microsoft Graph** > **Application permissions**.
3. Search and add: `Mail.Send`
4. Click **Grant admin consent** (requires admin).

### 3. Client Secret

1. Go to **Certificates & secrets** > New client secret.
2. Set description: `ecomag-web` and expiration (recommended: 24 months).
3. Copy the **Value** immediately (it won't be shown again).

### 4. Environment Variables

Set these in your Vercel/Netlify dashboard:

```
AZURE_TENANT_ID=<Directory (tenant) ID from Overview page>
AZURE_CLIENT_ID=<Application (client) ID from Overview page>
AZURE_CLIENT_SECRET=<Client secret value from step 3>
OFFICE365_SENDER_EMAIL=info@ecomagsas.com
```

### 5. Enable in Code

In `api/contact.js`, uncomment the `sendEmailViaGraph` function and its call in the handler.

### 6. Test

```bash
curl -X POST https://ecomagsas.com/api/contact \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Test","telefono":"+57 300 1234567","email":"test@test.com","mensaje":"Mensaje de prueba desde curl"}'
```

---

## Option B: SMTP (Simpler Alternative)

### 1. Install nodemailer

```bash
npm install nodemailer
```

### 2. Environment Variables

```
SMTP_USER=info@ecomagsas.com
SMTP_PASS=<app password or account password>
```

> If the account uses MFA, create an App Password in Office 365 security settings.

### 3. Enable in Code

In `api/contact.js`, uncomment the `sendEmailViaSMTP` function and its call in the handler.

### SMTP Settings Reference

| Setting | Value |
|---------|-------|
| Host    | smtp.office365.com |
| Port    | 587 |
| Secure  | false (uses STARTTLS) |
| Auth    | user + password |

---

## Rate Limiting (Optional)

To prevent abuse, add rate limiting via [Vercel KV](https://vercel.com/docs/storage/vercel-kv) or [Upstash Redis](https://upstash.com). See commented code in `api/contact.js`.

## reCAPTCHA v3 (Optional)

1. Get keys at [Google reCAPTCHA](https://www.google.com/recaptcha/admin).
2. Add `RECAPTCHA_SECRET_KEY` to env vars.
3. Add reCAPTCHA script to frontend and send token with form submission.
4. Uncomment verification code in `api/contact.js`.
