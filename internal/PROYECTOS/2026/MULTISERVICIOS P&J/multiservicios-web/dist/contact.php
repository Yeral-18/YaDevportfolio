<?php
error_reporting(0);
ini_set('display_errors', 0);

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: https://multiserviciospj.com');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode(['success' => false, 'message' => 'Método no permitido']);
    exit;
}

session_start();
$lastSubmit = $_SESSION['last_contact_submit'] ?? 0;
if (time() - $lastSubmit < 60) {
    echo json_encode(['success' => false, 'message' => 'Espere un minuto entre envíos']);
    exit;
}

$data = json_decode(file_get_contents('php://input'), true);

if (!$data) {
    echo json_encode(['success' => false, 'message' => 'Datos inválidos']);
    exit;
}

function sanitize($str) {
    return str_replace(["\r", "\n", "%0a", "%0d", "%0A", "%0D"], '', htmlspecialchars(trim($str), ENT_QUOTES, 'UTF-8'));
}

$nombre = sanitize($data['nombre'] ?? '');
$telefono = sanitize($data['telefono'] ?? '');
$servicio = sanitize($data['servicio'] ?? '');
$mensaje = htmlspecialchars(trim($data['mensaje'] ?? ''), ENT_QUOTES, 'UTF-8');

$email = filter_var(trim($data['email'] ?? ''), FILTER_SANITIZE_EMAIL);
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo json_encode(['success' => false, 'message' => 'Email inválido']);
    exit;
}

if (strlen($nombre) > 200 || strlen($email) > 254 || strlen($mensaje) > 5000 || strlen($telefono) > 30) {
    echo json_encode(['success' => false, 'message' => 'Datos exceden el límite permitido']);
    exit;
}

if (empty($nombre) || empty($email)) {
    echo json_encode(['success' => false, 'message' => 'Campos requeridos vacíos']);
    exit;
}

$serviciosPermitidos = [
    'Transporte de Carga por Carretera',
    'Obras Civiles y Mantenimiento Locativo',
    'Movimiento de Carga - Izaje',
    'Remediación Ambiental',
    'Transición Energética',
    'Alquiler de Maquinaria',
    'Remediacion Ambiental',
    'Transicion Energetica',
];
if (!empty($servicio) && !in_array($servicio, $serviciosPermitidos)) {
    $servicio = 'Consulta General';
}

$to = 'noreply@multiserviciospj.com';
$subject = "Nueva consulta - $servicio - Multiservicios P&J";

$body = "
<html>
<body style='font-family:Arial,sans-serif;color:#333;'>
<div style='max-width:600px;margin:0 auto;border:1px solid #e0e0e0;border-radius:8px;overflow:hidden;'>
  <div style='background:#0089D0;color:white;padding:20px;text-align:center;'>
    <h2 style='margin:0;'>Nueva Consulta Web</h2>
    <p style='margin:5px 0 0;opacity:0.9;font-size:14px;'>Multiservicios P&amp;J S.A.S</p>
  </div>
  <div style='padding:24px;'>
    <table style='width:100%;border-collapse:collapse;'>
      <tr><td style='padding:10px 0;border-bottom:1px solid #f0f0f0;font-weight:bold;color:#0089D0;width:120px;'>Nombre:</td><td style='padding:10px 0;border-bottom:1px solid #f0f0f0;'>$nombre</td></tr>
      <tr><td style='padding:10px 0;border-bottom:1px solid #f0f0f0;font-weight:bold;color:#0089D0;'>Email:</td><td style='padding:10px 0;border-bottom:1px solid #f0f0f0;'><a href='mailto:$email' style='color:#0089D0;'>$email</a></td></tr>
      <tr><td style='padding:10px 0;border-bottom:1px solid #f0f0f0;font-weight:bold;color:#0089D0;'>Tel&eacute;fono:</td><td style='padding:10px 0;border-bottom:1px solid #f0f0f0;'><a href='tel:$telefono' style='color:#0089D0;'>$telefono</a></td></tr>
      <tr><td style='padding:10px 0;border-bottom:1px solid #f0f0f0;font-weight:bold;color:#0089D0;'>Servicio:</td><td style='padding:10px 0;border-bottom:1px solid #f0f0f0;'>$servicio</td></tr>
      <tr><td style='padding:10px 0;font-weight:bold;color:#0089D0;vertical-align:top;'>Mensaje:</td><td style='padding:10px 0;'>" . ($mensaje ?: 'Sin mensaje adicional') . "</td></tr>
    </table>
  </div>
  <div style='background:#f8f9fa;padding:16px;text-align:center;font-size:12px;color:#999;'>
    Enviado desde el sitio web www.multiserviciospj.com
  </div>
</div>
</body>
</html>";

$headers = "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/html; charset=UTF-8\r\n";
$headers .= "From: Sitio Web <noreply@multiserviciospj.com>\r\n";
$headers .= "Reply-To: $nombre <$email>\r\n";

$sent = @mail($to, $subject, $body, $headers);

$_SESSION['last_contact_submit'] = time();

if ($sent) {
    echo json_encode(['success' => true, 'message' => 'Email enviado correctamente']);
} else {
    echo json_encode(['success' => false, 'message' => 'Error al enviar']);
}
?>
