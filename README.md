# Sistema CRUD con Flask y MySQL

Sistema de gestión de productos desarrollado con Flask y MySQL que implementa las operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

## 📋 Características

- ✅ Crear nuevos productos
- ✅ Visualizar lista de productos
- ✅ Editar productos existentes
- ✅ Eliminar productos con confirmación
- ✅ Validación de datos
- ✅ Interfaz responsive con Bootstrap 5
- ✅ Mensajes flash para feedback al usuario

## 🛠️ Tecnologías Utilizadas

- Python 3.x
- Flask 3.0.0
- MySQL
- Bootstrap 5
- Bootstrap Icons

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone [tu-repositorio-url]
cd [nombre-carpeta]
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

1. Asegúrate de tener MySQL instalado y ejecutándose
2. Importa el script SQL:

```bash
mysql -u root -p < base_datos.sql
```

3. Edita el archivo `database.py` con tus credenciales de MySQL:

```python
self.user = "tu_usuario"
self.password = "tu_contraseña"
```

### 5. Ejecutar la aplicación

```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

## 📁 Estructura del Proyecto

```
proyecto-flask/
│
├── app.py                 # Aplicación principal Flask
├── database.py            # Configuración de base de datos
├── base_datos.sql         # Script SQL
├── requirements.txt       # Dependencias Python
├── README.md             # Este archivo
│
└── templates/            # Plantillas HTML
    ├── base.html         # Plantilla base
    ├── index.html        # Página de inicio
    ├── productos.html    # Lista de productos
    ├── crear.html        # Formulario crear
    └── editar.html       # Formulario editar
```

## 🚀 Uso

### Crear Producto
1. Navega a "Nuevo Producto"
2. Completa el formulario con nombre, precio y stock
3. Haz clic en "Guardar Producto"

### Ver Productos
1. Navega a "Productos"
2. Verás una tabla con todos los productos registrados

### Editar Producto
1. En la lista de productos, haz clic en el botón de editar (lápiz)
2. Modifica los datos necesarios
3. Haz clic en "Actualizar Producto"

### Eliminar Producto
1. En la lista de productos, haz clic en el botón de eliminar (basura)
2. Confirma la eliminación en el modal que aparece

## 🔒 Seguridad

- Validación de datos en servidor
- Uso de consultas parametrizadas para prevenir SQL Injection
- Confirmación antes de eliminar registros

## 📝 Notas

- Asegúrate de cambiar la `secret_key` en `app.py` en producción
- Las credenciales de base de datos deben mantenerse seguras
- No subir credenciales a repositorios públicos

## 👨‍💻 Autor

[Tu Nombre]

## 📄 Licencia

Este proyecto es de código abierto para fines educativos.