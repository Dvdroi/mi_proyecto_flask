# 🚀 Mi Proyecto Flask

Una aplicación web desarrollada con Flask que permite gestionar usuarios mediante diferentes métodos de almacenamiento.

## ✨ Características

- 📝 **Formulario de registro** - Captura nombre, email y edad
- 💾 **Múltiples métodos de guardado**:
  - Archivo TXT
  - Archivo JSON
  - Archivo CSV
  - Base de datos SQLite
- 📊 **Visualización de datos** - Consulta los datos guardados en cada formato
- 🎨 **Interfaz moderna** - Diseño responsive con Bootstrap
- ⚡ **Funcionamiento en tiempo real** - Actualización inmediata de datos

## 🛠️ Tecnologías utilizadas

- **Backend**: Python 3.x, Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Base de datos**: SQLite
- **Despliegue**: Render

## 📋 Requisitos

- Python 3.7+
- Flask 2.3.3
- Gunicorn (para producción)

## 🚀 Instalación local

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/TU_USUARIO/mi-proyecto-flask.git
   cd mi-proyecto-flask
   ```

2. **Crea un entorno virtual**:
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual**:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecuta la aplicación**:
   ```bash
   python app.py
   ```

6. **Abre tu navegador** en: http://127.0.0.1:5000

## 📁 Estructura del proyecto

```
mi_proyecto_flask/
├── app.py                 # Aplicación principal
├── requirements.txt       # Dependencias
├── README.md             # Este archivo
├── .gitignore            # Archivos a ignorar por Git
├── templates/            # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   ├── formulario.html
│   ├── resultado.html
│   ├── datos_txt.html
│   ├── datos_json.html
│   ├── datos_csv.html
│   └── datos_sqlite.html
├── static/               # Archivos estáticos
│   └── styles.css
├── datos/               # Archivos de datos (TXT, JSON, CSV)
└── database/            # Base de datos SQLite
```

## 🌐 Demo en vivo

La aplicación está desplegada en Render: [Enlace a tu app]

## 👨‍💻 Autor

Tu Nombre - [Tu GitHub](https://github.com/TU_USUARIO)

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.

---

⭐ Si te gusta este proyecto, ¡no olvides darle una estrella!