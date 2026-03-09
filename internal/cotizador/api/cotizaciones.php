<?php
require_once 'config.php';

$conn = getConnection();
$method = $_SERVER['REQUEST_METHOD'];

switch ($method) {
    case 'GET':
        if (isset($_GET['id'])) {
            getCotizacion($conn, $_GET['id']);
        } else {
            getCotizaciones($conn);
        }
        break;

    case 'POST':
        createCotizacion($conn);
        break;

    case 'PUT':
        if (isset($_GET['id'])) {
            updateCotizacion($conn, $_GET['id']);
        }
        break;

    case 'DELETE':
        if (isset($_GET['id'])) {
            deleteCotizacion($conn, $_GET['id']);
        }
        break;

    default:
        http_response_code(405);
        echo json_encode(['error' => 'Método no permitido']);
}

$conn->close();

// Obtener todas las cotizaciones
function getCotizaciones($conn) {
    $sql = "SELECT * FROM cotizaciones ORDER BY created_at DESC";
    $result = $conn->query($sql);

    $cotizaciones = [];
    while ($row = $result->fetch_assoc()) {
        // Obtener items de cada cotización
        $row['items'] = getItems($conn, $row['id']);
        $cotizaciones[] = $row;
    }

    echo json_encode($cotizaciones);
}

// Obtener una cotización por ID
function getCotizacion($conn, $id) {
    $stmt = $conn->prepare("SELECT * FROM cotizaciones WHERE id = ?");
    $stmt->bind_param("i", $id);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($row = $result->fetch_assoc()) {
        $row['items'] = getItems($conn, $row['id']);
        echo json_encode($row);
    } else {
        http_response_code(404);
        echo json_encode(['error' => 'Cotización no encontrada']);
    }
}

// Obtener items de una cotización
function getItems($conn, $cotizacionId) {
    $stmt = $conn->prepare("SELECT * FROM cotizacion_items WHERE cotizacion_id = ? ORDER BY item_order");
    $stmt->bind_param("i", $cotizacionId);
    $stmt->execute();
    $result = $stmt->get_result();

    $items = [];
    while ($row = $result->fetch_assoc()) {
        $items[] = $row;
    }
    return $items;
}

// Crear nueva cotización
function createCotizacion($conn) {
    $data = json_decode(file_get_contents('php://input'), true);

    if (!$data) {
        http_response_code(400);
        echo json_encode(['error' => 'Datos inválidos']);
        return;
    }

    $conn->begin_transaction();

    try {
        $stmt = $conn->prepare("INSERT INTO cotizaciones
            (quote_number, client_name, client_email, client_phone, project_name,
             currency, subtotal, iva_rate, iva_amount, include_iva, total, validity_days, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");

        $stmt->bind_param("ssssssdddidis",
            $data['quoteNumber'],
            $data['clientName'],
            $data['clientEmail'],
            $data['clientPhone'],
            $data['projectName'],
            $data['currency'],
            $data['subtotal'],
            $data['ivaRate'],
            $data['ivaAmount'],
            $data['includeIva'],
            $data['total'],
            $data['validityDays'],
            $data['notes']
        );

        $stmt->execute();
        $cotizacionId = $conn->insert_id;

        // Insertar items
        if (isset($data['items']) && is_array($data['items'])) {
            $stmtItem = $conn->prepare("INSERT INTO cotizacion_items
                (cotizacion_id, description, quantity, unit_price, total, item_order)
                VALUES (?, ?, ?, ?, ?, ?)");

            foreach ($data['items'] as $index => $item) {
                $stmtItem->bind_param("isdddi",
                    $cotizacionId,
                    $item['description'],
                    $item['quantity'],
                    $item['unitPrice'],
                    $item['total'],
                    $index
                );
                $stmtItem->execute();
            }
        }

        $conn->commit();

        echo json_encode([
            'success' => true,
            'id' => $cotizacionId,
            'message' => 'Cotización guardada correctamente'
        ]);

    } catch (Exception $e) {
        $conn->rollback();
        http_response_code(500);
        echo json_encode(['error' => 'Error al guardar: ' . $e->getMessage()]);
    }
}

// Actualizar cotización
function updateCotizacion($conn, $id) {
    $data = json_decode(file_get_contents('php://input'), true);

    if (!$data) {
        http_response_code(400);
        echo json_encode(['error' => 'Datos inválidos']);
        return;
    }

    $conn->begin_transaction();

    try {
        $stmt = $conn->prepare("UPDATE cotizaciones SET
            quote_number = ?, client_name = ?, client_email = ?, client_phone = ?,
            project_name = ?, currency = ?, subtotal = ?, iva_rate = ?,
            iva_amount = ?, include_iva = ?, total = ?, validity_days = ?, notes = ?
            WHERE id = ?");

        $stmt->bind_param("ssssssdddidisi",
            $data['quoteNumber'],
            $data['clientName'],
            $data['clientEmail'],
            $data['clientPhone'],
            $data['projectName'],
            $data['currency'],
            $data['subtotal'],
            $data['ivaRate'],
            $data['ivaAmount'],
            $data['includeIva'],
            $data['total'],
            $data['validityDays'],
            $data['notes'],
            $id
        );

        $stmt->execute();

        // Eliminar items anteriores y agregar nuevos
        $stmtDelete = $conn->prepare("DELETE FROM cotizacion_items WHERE cotizacion_id = ?");
        $stmtDelete->bind_param("i", $id);
        $stmtDelete->execute();

        // Insertar nuevos items
        if (isset($data['items']) && is_array($data['items'])) {
            $stmtItem = $conn->prepare("INSERT INTO cotizacion_items
                (cotizacion_id, description, quantity, unit_price, total, item_order)
                VALUES (?, ?, ?, ?, ?, ?)");

            foreach ($data['items'] as $index => $item) {
                $stmtItem->bind_param("isdddi",
                    $id,
                    $item['description'],
                    $item['quantity'],
                    $item['unitPrice'],
                    $item['total'],
                    $index
                );
                $stmtItem->execute();
            }
        }

        $conn->commit();

        echo json_encode([
            'success' => true,
            'message' => 'Cotización actualizada correctamente'
        ]);

    } catch (Exception $e) {
        $conn->rollback();
        http_response_code(500);
        echo json_encode(['error' => 'Error al actualizar: ' . $e->getMessage()]);
    }
}

// Eliminar cotización
function deleteCotizacion($conn, $id) {
    $stmt = $conn->prepare("DELETE FROM cotizaciones WHERE id = ?");
    $stmt->bind_param("i", $id);

    if ($stmt->execute()) {
        echo json_encode([
            'success' => true,
            'message' => 'Cotización eliminada correctamente'
        ]);
    } else {
        http_response_code(500);
        echo json_encode(['error' => 'Error al eliminar']);
    }
}
