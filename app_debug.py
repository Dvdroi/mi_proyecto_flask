from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Verificar que los templates existen
@app.route('/check')
def check_files():
    template_dir = os.path.join(app.root_path, 'templates')
    files = os.listdir(template_dir) if os.path.exists(template_dir) else []
    return f"Archivos en templates: {files}"

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error cargando index.html: {str(e)}"

@app.route('/formulario')
def formulario():
    try:
        return render_template('formulario.html')
    except Exception as e:
        return f"Error cargando formulario.html: {str(e)}"

@app.route('/procesar', methods=['POST'])
def procesar_formulario():
    try:
        nombre = request.form.get('nombre', 'No proporcionado')
        email = request.form.get('email', 'No proporcionado')
        edad = request.form.get('edad', 'No proporcionado')
        metodo = request.form.get('metodo', 'No proporcionado')
        
        datos = {
            'nombre': nombre,
            'email': email,
            'edad': edad,
            'metodo': metodo
        }
        
        return render_template('resultado.html', datos=datos)
    except Exception as e:
        return f"Error procesando formulario: {str(e)}"

@app.route('/test')
def test():
    return "¡Flask está funcionando correctamente!"

if __name__ == '__main__':
    print("🚀 Iniciando Flask...")
    print("📁 Directorio actual:", os.getcwd())
    print("📄 Verificando archivos...")
    
    # Verificar estructura de archivos
    if os.path.exists('templates'):
        templates = os.listdir('templates')
        print("📋 Templates encontrados:", templates)
    else:
        print("❌ Carpeta 'templates' no existe")
    
    if os.path.exists('static'):
        print("✅ Carpeta 'static' existe")
    else:
        print("❌ Carpeta 'static' no existe")
    
    app.run(debug=True, port=5000)