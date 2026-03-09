-- Base de datos para Cotizador YaDev
-- Ejecutar en phpMyAdmin o MySQL

CREATE DATABASE IF NOT EXISTS yadev_cotizador;
USE yadev_cotizador;

-- Tabla de cotizaciones
CREATE TABLE IF NOT EXISTS cotizaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quote_number VARCHAR(20) NOT NULL UNIQUE,
    client_name VARCHAR(255) NOT NULL,
    client_email VARCHAR(255),
    client_phone VARCHAR(50),
    project_name VARCHAR(255),
    currency VARCHAR(10) DEFAULT 'COP',
    subtotal DECIMAL(15,2) DEFAULT 0,
    iva_rate DECIMAL(5,2) DEFAULT 19,
    iva_amount DECIMAL(15,2) DEFAULT 0,
    include_iva TINYINT(1) DEFAULT 1,
    total DECIMAL(15,2) DEFAULT 0,
    validity_days INT DEFAULT 15,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla de items de cotización
CREATE TABLE IF NOT EXISTS cotizacion_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cotizacion_id INT NOT NULL,
    description TEXT NOT NULL,
    quantity DECIMAL(10,2) DEFAULT 1,
    unit_price DECIMAL(15,2) DEFAULT 0,
    total DECIMAL(15,2) DEFAULT 0,
    item_order INT DEFAULT 0,
    FOREIGN KEY (cotizacion_id) REFERENCES cotizaciones(id) ON DELETE CASCADE
);

-- Índices para mejor rendimiento
CREATE INDEX idx_quote_number ON cotizaciones(quote_number);
CREATE INDEX idx_client_name ON cotizaciones(client_name);
CREATE INDEX idx_created_at ON cotizaciones(created_at);
