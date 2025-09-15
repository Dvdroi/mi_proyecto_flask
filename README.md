# Proyecto Flask con MySQL

Este es un proyecto Flask que integra una base de datos MySQL para el manejo de usuarios y datos del sistema.

## Características

- ✅ Aplicación Flask funcional
- ✅ Conexión a base de datos MySQL
- ✅ Tabla de usuarios con operaciones básicas
- ✅ API REST endpoints
- ✅ Manejo de errores

## Estructura del Proyecto

```
mi_proyecto_flask/
│
├── app.py                 # Aplicación principal Flask
├── conexion/
│   └── conexion.py       # Configuración de conexión MySQL
├── database_script.sql   # Script de base de datos
├── requirements.txt      # Dependencias
└── README.md            # Este archivo
```

## Instalación

### 1. Prerrequisitos

- Python 3.7 o superior
- MySQL Server instalado
- Git

### 2. Clonar el repositorio

```bash
git clone https://github.com/Dvdroi/mi_proyecto_flask.git
cd mi_proyecto_flask
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Configurar MySQL

1. Instalar MySQL si no lo tienes
2. Crear la base de datos ejecutando el script:

```sql
mysql -u root -p < database_script.sql
```

3. Actualizar las credenciales en `conexion/conexion.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'database': 'desarrollo_web',
    'user': 'root',
    'password': 'admin',  # Cambia por tu contraseña
    'port': 3306
}
```

## Uso

### Ejecutar la aplicación

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

### Endpoints disponibles

- `GET /` - Página principal
- `GET /test_db` - Probar conexión a base de datos
- `GET /usuarios` - Obtener lista de usuarios

## Estructura de Base de Datos

### Tabla: usuarios

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_usuario | INT (PK, AUTO_INCREMENT) | ID único del usuario |
| nombre | VARCHAR(100) | Nombre del usuario |
| mail | VARCHAR(255) | Email único del usuario |
| fecha_creacion | TIMESTAMP | Fecha de creación |
| fecha_modificacion | TIMESTAMP | Fecha de última modificación |

## Comandos Útiles

### Probar conexión a MySQL

```bash
python conexion/conexion.py
```

### Verificar tablas en MySQL

```sql
USE desarrollo_web;
SHOW TABLES;
SELECT * FROM usuarios;
```

## Desarrollo

Para agregar nuevas funcionalidades:

1. Crear nuevas rutas en `app.py`
2. Agregar tablas necesarias en `database_script.sql`
3. Actualizar este README con los cambios

## Contribuir

1. Fork el proyecto
2. Crear rama para nueva funcionalidad
3. Hacer commit de los cambios
4. Push a la rama
5. Crear Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT.

## Contacto

David - Desarrollador
Enlace del Proyecto: https://github.com/Dvdroi/mi_proyecto_flask.git