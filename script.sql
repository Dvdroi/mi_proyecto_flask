-- Script para crear la base de datos y tablas del proyecto Flask
-- Fecha: 2025-09-14
-- Base de datos: desarrollo_web

-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS desarrollo_web;

-- Usar la base de datos
USE desarrollo_web;

-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    mail VARCHAR(255) NOT NULL UNIQUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insertar datos de ejemplo en la tabla usuarios
INSERT INTO usuarios (nombre, mail) VALUES
('Juan Pérez', 'juan.perez@email.com'),
('María García', 'maria.garcia@email.com'),
('Carlos López', 'carlos.lopez@email.com'),
('Ana Martínez', 'ana.martinez@email.com');

-- Crear tabla de productos (ejemplo adicional para tu proyecto)
CREATE TABLE IF NOT EXISTS productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    activo BOOLEAN DEFAULT TRUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos de ejemplo en productos
INSERT INTO productos (nombre, descripcion, precio, stock) VALUES
('Laptop Dell', 'Laptop Dell Inspiron 15 8GB RAM', 899.99, 10),
('Mouse Logitech', 'Mouse inalámbrico Logitech MX Master', 79.99, 25),
('Teclado Mecánico', 'Teclado mecánico RGB Gaming', 149.99, 15);

-- Crear tabla de pedidos (relación con usuarios)
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    estado ENUM('pendiente', 'procesando', 'enviado', 'entregado') DEFAULT 'pendiente',
    fecha_pedido TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE
);

-- Insertar pedidos de ejemplo
INSERT INTO pedidos (id_usuario, total, estado) VALUES
(1, 899.99, 'entregado'),
(2, 229.98, 'enviado'),
(3, 79.99, 'procesando');

-- Verificar que las tablas se crearon correctamente
SHOW TABLES;

-- Mostrar estructura de la tabla usuarios
DESCRIBE usuarios;

-- Consulta para verificar los datos insertados
SELECT * FROM usuarios;
SELECT * FROM productos;
SELECT * FROM pedidos;