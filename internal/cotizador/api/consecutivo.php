<?php
require_once 'config.php';

$conn = getConnection();

// Obtener el consecutivo más alto de la base de datos
$sql = "SELECT quote_number FROM cotizaciones ORDER BY id DESC";
$result = $conn->query($sql);

$maxConsecutivo = 314; // Base inicial

while ($row = $result->fetch_assoc()) {
    if (preg_match('/COT-\d{4}-(\d+)/', $row['quote_number'], $matches)) {
        $num = intval($matches[1]);
        if ($num > $maxConsecutivo) {
            $maxConsecutivo = $num;
        }
    }
}

$nextConsecutivo = $maxConsecutivo + 1;

// Generar número de cotización con fecha actual
$day = date('d');
$month = date('m');
$quoteNumber = "COT-{$day}{$month}-{$nextConsecutivo}";

echo json_encode([
    'consecutivo' => $nextConsecutivo,
    'quoteNumber' => $quoteNumber
]);

$conn->close();
