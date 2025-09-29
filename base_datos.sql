-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS desarrollo_web;
USE desarrollo_web;

-- Crear la tabla productos
CREATE TABLE IF NOT EXISTS productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar algunos datos de ejemplo
INSERT INTO productos (nombre, precio, stock) VALUES
('Laptop HP', 899.99, 15),
('Mouse Logitech', 25.50, 50),
('Teclado Mecánico', 75.00, 30),
('Monitor Samsung 24"', 199.99, 20);