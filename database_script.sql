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

-- Verificar que las tablas se crearon correctamente
SHOW TABLES;

-- Mostrar estructura de la tabla usuarios
DESCRIBE usuarios;

-- Consulta para verificar los datos insertados
SELECT * FROM usuarios;