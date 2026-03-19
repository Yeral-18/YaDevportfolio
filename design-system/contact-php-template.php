<?php
/**
 * ══════════════════════════════════════════════════════════════════
 * YaDev Design System — Contact Form PHP Template
 * ══════════════════════════════════════════════════════════════════
 *
 * SETUP:
 *   1. Copy to: public/contact.php
 *   2. Replace ALL values marked [PLACEHOLDER].
 *   3. Update $serviciosPermitidos with the client's actual services.
 *   4. Upload to the same directory as index.html on Hostinger.
 *
 * HOW IT WORKS:
 *   - Accepts POST requests with JSON body from the contact form.
 *   - Validates and sanitizes all input.
 *   - Rate limits to 1 submission per minute per session.
 *   - Sends HTML email using PHP mail() to the destination address.
 *   - Sets Reply-To header so client can reply directly to the lead.
 *
 * CRITICAL — USE PHP mail() NOT SMTP:
 *   Hostinger shared hosting blocks outgoing SMTP connections on
 *   ports 587 and 465 (TLS/STARTTLS). PHPMailer with SMTP will
 *   silently fail or throw timeout errors. PHP mail() uses the
 *   server's local sendmail binary, which works on Hostinger.
 *
 * FRONTEND USAGE (JavaScript fetch):
 *   const res = await fetch('/contact.php', {
 *     method: 'POST',
 *     headers: { 'Content-Type': 'application/json' },
 *     body: JSON.stringify({ nombre, email, telefono, servicio, mensaje })
 *   });
 *   const data = await res.json();
 *   if (data.success) { ... }
 *
 * ══════════════════════════════════════════════════════════════════
 */

/* ─────────────────────────────────────────────────────────────────
   CONFIGURATION — Edit these before deploying
   ───────────────────────────────────────────────────────────────── */

/**
 * [PLACEHOLDER] Domain where the website is hosted.
 * Used for CORS header. Must match EXACTLY (no trailing slash).
 * Example: 'https://myclient.com'
 */
define('SITE_DOMAIN', 'https://PLACEHOLDER_SITE_DOMAIN');

/**
 * [PLACEHOLDER] Destination email for contact form submissions.
 * This is where lead notifications are sent.
 * Example: 'info@myclient.com'
 */
define('DESTINATION_EMAIL', 'PLACEHOLDER_DESTINATION_EMAIL');

/**
 * [PLACEHOLDER] From address for outgoing emails.
 * Must use the domain of the hosting account to avoid spam filters.
 * Example: 'noreply@myclient.com'
 */
define('FROM_EMAIL', 'noreply@PLACEHOLDER_SITE_DOMAIN_BARE');

/**
 * [PLACEHOLDER] Client/company name for email branding.
 * Example: 'ECOMAG S.A.S'
 */
define('COMPANY_NAME', 'PLACEHOLDER_COMPANY_NAME');

/**
 * [PLACEHOLDER] Brand color hex for email header background.
 * Use the primary brand color WITHOUT the # symbol.
 * Example: '0089D0'
 */
define('BRAND_COLOR', 'PLACEHOLDER_BRAND_COLOR_HEX');

/**
 * [PLACEHOLDER] Website URL shown in email footer.
 * Example: 'www.myclient.com'
 */
define('SITE_URL_DISPLAY', 'PLACEHOLDER_SITE_URL_DISPLAY');

/**
 * Rate limit: minimum seconds between submissions per session.
 * 60 seconds = 1 per minute. Increase to 120 for stricter limits.
 */
define('RATE_LIMIT_SECONDS', 60);

/* ─────────────────────────────────────────────────────────────────
   END CONFIGURATION
   ───────────────────────────────────────────────────────────────── */


/* ── Security: suppress PHP errors from leaking in response ── */
error_reporting(0);
ini_set('display_errors', 0);


/* ── Response headers ── */
header('Content-Type: application/json; charset=UTF-8');
header('Access-Control-Allow-Origin: ' . SITE_DOMAIN);
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');
header('X-Content-Type-Options: nosniff');


/* ── Handle CORS preflight ── */
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}


/* ── Only accept POST ── */
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Método no permitido']);
    exit;
}


/* ── Rate limiting (session-based, 1 per RATE_LIMIT_SECONDS) ── */
session_start();
$lastSubmit = $_SESSION['last_contact_submit'] ?? 0;
if (time() - $lastSubmit < RATE_LIMIT_SECONDS) {
    $waitSeconds = RATE_LIMIT_SECONDS - (time() - $lastSubmit);
    http_response_code(429);
    echo json_encode([
        'success' => false,
        'message' => "Por favor espera {$waitSeconds} segundos antes de enviar otro mensaje."
    ]);
    exit;
}


/* ── Parse JSON body ── */
$rawBody = file_get_contents('php://input');
if (empty($rawBody)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'Cuerpo de solicitud vacío']);
    exit;
}

$data = json_decode($rawBody, true);
if (json_last_error() !== JSON_ERROR_NONE || !is_array($data)) {
    http_response_code(400);
    echo json_encode(['success' => false, 'message' => 'JSON inválido']);
    exit;
}


/* ── Input sanitization helpers ── */

/**
 * Sanitize single-line fields.
 * Strips header injection chars (\r, \n) and HTML entities.
 */
function sanitize(string $str): string {
    $str = str_replace(["\r", "\n", "%0a", "%0d", "%0A", "%0D"], '', $str);
    return htmlspecialchars(trim($str), ENT_QUOTES, 'UTF-8');
}

/**
 * Sanitize multi-line text fields (message body).
 * Allows newlines but strips HTML to prevent XSS.
 */
function sanitizeMultiline(string $str): string {
    return htmlspecialchars(trim($str), ENT_QUOTES, 'UTF-8');
}


/* ── Extract and sanitize fields ── */
$nombre   = sanitize($data['nombre']   ?? '');
$telefono = sanitize($data['telefono'] ?? '');
$servicio = sanitize($data['servicio'] ?? '');
$mensaje  = sanitizeMultiline($data['mensaje'] ?? '');

/* Email: sanitize then validate */
$email = filter_var(trim($data['email'] ?? ''), FILTER_SANITIZE_EMAIL);
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(422);
    echo json_encode(['success' => false, 'message' => 'Email inválido']);
    exit;
}


/* ── Field length limits ── */
if (
    strlen($nombre)   > 200  ||
    strlen($email)    > 254  ||
    strlen($telefono) > 30   ||
    strlen($servicio) > 200  ||
    strlen($mensaje)  > 5000
) {
    http_response_code(422);
    echo json_encode(['success' => false, 'message' => 'Uno o más campos exceden el límite de caracteres']);
    exit;
}


/* ── Required fields ── */
if (empty($nombre) || empty($email)) {
    http_response_code(422);
    echo json_encode(['success' => false, 'message' => 'Nombre y email son requeridos']);
    exit;
}


/* ── Service whitelist ── */
/*
 * [PLACEHOLDER] Replace this array with the client's actual services.
 * Any value not in this list is replaced with 'Consulta General'.
 * This prevents service field injection.
 *
 * Leave the array empty to skip validation:
 *   $serviciosPermitidos = [];
 */
$serviciosPermitidos = [
    /* [PLACEHOLDER] Add client services here */
    /* 'Nombre del Servicio 1', */
    /* 'Nombre del Servicio 2', */
    /* 'Nombre del Servicio 3', */
];

if (!empty($serviciosPermitidos) && !empty($servicio) && !in_array($servicio, $serviciosPermitidos)) {
    $servicio = 'Consulta General';
}

if (empty($servicio)) {
    $servicio = 'Consulta General';
}


/* ── Build email content ── */
$subject = "Nueva consulta — {$servicio} — " . COMPANY_NAME;

/* Human-readable timestamp */
$timestamp = date('d/m/Y H:i') . ' (hora del servidor)';

/* Format mensaje for display — preserve newlines as <br> */
$mensajeFormatted = !empty($mensaje)
    ? nl2br($mensaje)
    : '<em style="color:#9ca3af;">Sin mensaje adicional</em>';

/* HTML email body */
$body = <<<HTML
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nueva Consulta Web</title>
</head>
<body style="margin:0;padding:0;background-color:#f3f4f6;font-family:Arial,Helvetica,sans-serif;color:#111827;">

  <table width="100%" cellpadding="0" cellspacing="0" style="background-color:#f3f4f6;padding:32px 16px;">
    <tr>
      <td align="center">
        <table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;background-color:#ffffff;border-radius:12px;overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,0.08);">

          <!-- Header -->
          <tr>
            <td style="background-color:#{BRAND_COLOR};padding:28px 32px;text-align:center;">
              <h1 style="margin:0;color:#ffffff;font-size:22px;font-weight:700;letter-spacing:-0.01em;">
                Nueva Consulta Web
              </h1>
              <p style="margin:6px 0 0;color:rgba(255,255,255,0.85);font-size:14px;">
                {COMPANY_NAME}
              </p>
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td style="padding:28px 32px;">
              <table width="100%" cellpadding="0" cellspacing="0">

                <!-- Nombre -->
                <tr>
                  <td style="padding:12px 0;border-bottom:1px solid #f0f0f0;vertical-align:top;width:130px;">
                    <span style="font-weight:700;color:#{BRAND_COLOR};font-size:14px;">Nombre</span>
                  </td>
                  <td style="padding:12px 0;border-bottom:1px solid #f0f0f0;font-size:14px;">
                    {NOMBRE}
                  </td>
                </tr>

                <!-- Email -->
                <tr>
                  <td style="padding:12px 0;border-bottom:1px solid #f0f0f0;vertical-align:top;">
                    <span style="font-weight:700;color:#{BRAND_COLOR};font-size:14px;">Email</span>
                  </td>
                  <td style="padding:12px 0;border-bottom:1px solid #f0f0f0;font-size:14px;">
                    <a href="mailto:{EMAIL}" style="color:#{BRAND_COLOR};text-decoration:none;">{EMAIL}</a>
                  </td>
                </tr>

                <!-- Telefono -->
                <tr>
                  <td style="padding:12px 0;border-bottom:1px solid #f0f0f0;vertical-align:top;">
                    <span style="font-weight:700;color:#{BRAND_COLOR};font-size:14px;">Teléfono</span>
                  </td>
                  <td style="padding:12px 0;border-bottom:1px solid #f0f0f0;font-size:14px;">
                    {TELEFONO}
                  </td>
                </tr>

                <!-- Servicio -->
                <tr>
                  <td style="padding:12px 0;border-bottom:1px solid #f0f0f0;vertical-align:top;">
                    <span style="font-weight:700;color:#{BRAND_COLOR};font-size:14px;">Servicio</span>
                  </td>
                  <td style="padding:12px 0;border-bottom:1px solid #f0f0f0;font-size:14px;">
                    <span style="display:inline-block;background-color:#f0f9ff;color:#{BRAND_COLOR};padding:2px 10px;border-radius:9999px;font-size:12px;font-weight:600;">
                      {SERVICIO}
                    </span>
                  </td>
                </tr>

                <!-- Mensaje -->
                <tr>
                  <td style="padding:12px 0;vertical-align:top;">
                    <span style="font-weight:700;color:#{BRAND_COLOR};font-size:14px;">Mensaje</span>
                  </td>
                  <td style="padding:12px 0;font-size:14px;line-height:1.6;color:#374151;">
                    {MENSAJE}
                  </td>
                </tr>

              </table>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="background-color:#f8f9fa;padding:16px 32px;text-align:center;">
              <p style="margin:0;font-size:12px;color:#9ca3af;">
                Enviado desde
                <a href="https://{SITE_URL_DISPLAY}" style="color:#{BRAND_COLOR};text-decoration:none;">
                  {SITE_URL_DISPLAY}
                </a>
                · {TIMESTAMP}
              </p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>

</body>
</html>
HTML;

/* ── Replace template placeholders in the HTML body ── */
$body = str_replace(
    ['{BRAND_COLOR}', '{COMPANY_NAME}', '{NOMBRE}', '{EMAIL}', '{TELEFONO}', '{SERVICIO}', '{MENSAJE}', '{SITE_URL_DISPLAY}', '{TIMESTAMP}'],
    [BRAND_COLOR, COMPANY_NAME, $nombre, $email, $telefono ?: '—', $servicio, $mensajeFormatted, SITE_URL_DISPLAY, $timestamp],
    $body
);


/* ── Email headers ── */
$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$headers .= "From: " . COMPANY_NAME . " Web <" . FROM_EMAIL . ">\r\n";
$headers .= "Reply-To: {$nombre} <{$email}>\r\n";
$headers .= "X-Mailer: PHP/" . PHP_VERSION . "\r\n";


/* ── Send email using PHP mail() ── */
/* NOTE: SMTP is blocked on Hostinger shared hosting.          */
/* mail() uses the server's local sendmail binary.             */
/* The @ suppresses the warning if mail() is misconfigured     */
/* but we check the return value to report success/failure.    */
$sent = @mail(DESTINATION_EMAIL, $subject, $body, $headers);


/* ── Record submission time for rate limiting ── */
$_SESSION['last_contact_submit'] = time();


/* ── Response ── */
if ($sent) {
    echo json_encode([
        'success' => true,
        'message' => 'Mensaje enviado correctamente. Nos pondremos en contacto pronto.',
    ]);
} else {
    /* mail() failed — log for debugging if needed */
    /* error_log('[contact.php] mail() returned false for ' . $email); */
    http_response_code(500);
    echo json_encode([
        'success' => false,
        'message' => 'Error al enviar el mensaje. Por favor intenta de nuevo o contáctanos directamente.',
    ]);
}
