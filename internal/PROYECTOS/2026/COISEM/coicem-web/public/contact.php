<?php
/**
 * contact.php — COICEM S.A.S
 * PHP mail() nativo — NO SMTP (puerto 587 bloqueado en Hostinger).
 * ⚠️ $to PENDIENTE: completar con el correo real de COICEM cuando el cliente lo
 *    confirme (ver src/lib/site-config.ts → contact.email). Sin él responde aviso.
 */
error_reporting(0);
ini_set('display_errors', 0);
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: https://coicem.com');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(200); exit; }
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['success' => false, 'message' => 'Metodo no permitido']); exit;
}

// Rate limit: 1 envio por minuto
session_start();
$last = $_SESSION['last_contact_submit'] ?? 0;
if (time() - $last < 60) {
    echo json_encode(['success' => false, 'message' => 'Espere un minuto entre envios']); exit;
}

$data = json_decode(file_get_contents('php://input'), true);
if (!$data) { echo json_encode(['success' => false, 'message' => 'Datos invalidos']); exit; }

function sanitize($s) {
    return str_replace(["\r", "\n", "%0a", "%0d", "%0A", "%0D"], '', htmlspecialchars(trim($s), ENT_QUOTES, 'UTF-8'));
}

$nombre   = sanitize($data['nombre']   ?? '');
$telefono = sanitize($data['telefono'] ?? '');
$servicio = sanitize($data['servicio'] ?? '');
$mensaje  = htmlspecialchars(trim($data['mensaje'] ?? ''), ENT_QUOTES, 'UTF-8');
$email    = filter_var(trim($data['email'] ?? ''), FILTER_SANITIZE_EMAIL);

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo json_encode(['success' => false, 'message' => 'Email invalido']); exit;
}
if (strlen($nombre) > 200 || strlen($email) > 254 || strlen($mensaje) > 5000 || strlen($telefono) > 30) {
    echo json_encode(['success' => false, 'message' => 'Datos exceden el limite']); exit;
}
if (empty($nombre) || empty($email)) {
    echo json_encode(['success' => false, 'message' => 'Campos requeridos vacios']); exit;
}

// Whitelist de areas de COICEM
$permitidos = ['Operacion', 'Mantenimiento', 'Construccion', 'Energia', 'Infraestructura', 'Consulta general'];
$serv_norm = str_replace(['ó','í','é'], ['o','i','e'], $servicio);
if (!empty($servicio) && !in_array($serv_norm, $permitidos)) { $servicio = 'Consulta general'; }

// ⚠️ Destinatario PENDIENTE — completar cuando el cliente confirme su correo.
$to = '';
if (empty($to)) {
    echo json_encode(['success' => false, 'message' => 'Formulario en configuracion. Use el boton de WhatsApp o escribanos directamente.']);
    exit;
}

$subject = "Nueva cotizacion - $servicio - COICEM";
$body = "
<html><head><meta charset='UTF-8'></head>
<body style='font-family:Arial,sans-serif;color:#333;'>
<div style='max-width:600px;margin:0 auto;border:1px solid #e0e0e0;'>
  <div style='background:#0B0E14;color:#fff;padding:22px;text-align:center;'>
    <h2 style='margin:0;font-size:19px;'>Nueva Cotizacion Web</h2>
    <p style='margin:6px 0 0;color:#F79204;font-size:13px;'>COICEM S.A.S</p>
  </div>
  <div style='padding:26px;'>
    <table style='width:100%;border-collapse:collapse;'>
      <tr><td style='padding:9px 0;border-bottom:1px solid #eee;font-weight:bold;color:#025199;width:120px;'>Nombre:</td><td style='padding:9px 0;border-bottom:1px solid #eee;'>$nombre</td></tr>
      <tr><td style='padding:9px 0;border-bottom:1px solid #eee;font-weight:bold;color:#025199;'>Email:</td><td style='padding:9px 0;border-bottom:1px solid #eee;'>$email</td></tr>
      <tr><td style='padding:9px 0;border-bottom:1px solid #eee;font-weight:bold;color:#025199;'>Telefono:</td><td style='padding:9px 0;border-bottom:1px solid #eee;'>$telefono</td></tr>
      <tr><td style='padding:9px 0;border-bottom:1px solid #eee;font-weight:bold;color:#025199;'>Area:</td><td style='padding:9px 0;border-bottom:1px solid #eee;'>$servicio</td></tr>
      <tr><td style='padding:9px 0;font-weight:bold;color:#025199;vertical-align:top;'>Mensaje:</td><td style='padding:9px 0;'>" . ($mensaje ?: 'Sin mensaje') . "</td></tr>
    </table>
  </div>
  <div style='background:#f8f9fa;padding:14px;text-align:center;font-size:12px;color:#999;'>Enviado desde coicem.com</div>
</div></body></html>";

$headers  = "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$headers .= "From: Sitio Web COICEM <noreply@coicem.com>\r\n";
$headers .= "Reply-To: $nombre <$email>\r\n";

$sent = @mail($to, $subject, $body, $headers);
$_SESSION['last_contact_submit'] = time();

echo json_encode($sent
    ? ['success' => true, 'message' => 'Email enviado correctamente']
    : ['success' => false, 'message' => 'Error al enviar']);
?>
