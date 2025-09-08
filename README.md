# 🚀 Mi Proyecto Flask

Una aplicación web desarrollada con Flask que permite gestionar usuarios mediante diferentes métodos de almacenamiento.

## ✨ Características

- 📝 **Formulario de registro** - Captura nombre, email y edad
- 💾 **Múltiples métodos de almacenamiento**:
  - Archivo TXT
  - Archivo JSON
  - Archivo CSV
  - Base de datos SQLite
- 📊 **Visualización de datos** por cada formato
- 🎨 **Interfaz moderna** con Bootstrap 5

## 🌐 Demo

[Ver aplicación en vivo](https://mi-proyecto-flask.onrender.com)

## 🛠️ Tecnologías utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Base de datos**: SQLite
- **Despliegue**: Render

## 🚀 Instalación local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Dvdroi/mi_proyecto_flask.git
   cd mi_proyecto_flask
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la aplicación:
   ```bash
   python app.py
   ```

4. Abre tu navegador en `http://localhost:5000`

## 📁 Estructura del proyecto

```
mi_proyecto_flask/
│
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias Python
├── templates/            # Plantillas HTML
│   ├── base.html
│   ├── index.html
│   └── formulario.html
├── static/              # Archivos estáticos
│   └── styles.css
└── datos/              # Archivos de datos (se crea automáticamente)
    ├── usuarios.txt
    ├── usuarios.json
    ├── usuarios.csv
    └── usuarios.db
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue primero para discutir qué te gustaría cambiar.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

---

Desarrollado con ❤️ por [Dvdroi](https://github.com/Dvdroi)