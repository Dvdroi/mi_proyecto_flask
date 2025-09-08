<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for
import json
import csv
import os
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Crear directorios necesarios
os.makedirs('datos', exist_ok=True)
os.makedirs('database', exist_ok=True)

# Inicializar base de datos SQLite con corrección de columnas
def init_db():
    conn = sqlite3.connect('database/usuarios.db')
    cursor = conn.cursor()
    
    # Crear tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            edad INTEGER NOT NULL,
            fecha TEXT
        )
    ''')
    
    # Verificar si la columna 'fecha' existe, si no, agregarla
    cursor.execute("PRAGMA table_info(usuarios)")
    columnas = [col[1] for col in cursor.fetchall()]
    
    if 'fecha' not in columnas:
        print("🔧 Agregando columna 'fecha' a la tabla usuarios...")
        cursor.execute('ALTER TABLE usuarios ADD COLUMN fecha TEXT')
        # Actualizar registros existentes con fecha actual
        fecha_default = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('UPDATE usuarios SET fecha = ? WHERE fecha IS NULL', (fecha_default,))
    
    conn.commit()
    conn.close()
    print("✅ Base de datos inicializada correctamente")

# Inicializar la base de datos al arrancar
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar_formulario():
    try:
        nombre = request.form['nombre']
        email = request.form['email']
        edad = int(request.form['edad'])
        metodo = request.form['metodo']
        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        datos_usuario = {
            'nombre': nombre,
            'email': email,
            'edad': edad,
            'fecha': fecha_actual
        }
        
        mensaje = ""
        
        if metodo == 'txt' or metodo == 'todos':
            # Guardar en archivo TXT
            with open('datos/usuarios.txt', 'a', encoding='utf-8') as f:
                f.write(f"Nombre: {nombre}, Email: {email}, Edad: {edad}, Fecha: {fecha_actual}\n")
            mensaje += "✅ Guardado en archivo TXT. "
        
        if metodo == 'json' or metodo == 'todos':
            # Guardar en archivo JSON
            if os.path.exists('datos/usuarios.json'):
                with open('datos/usuarios.json', 'r', encoding='utf-8') as f:
                    usuarios = json.load(f)
            else:
                usuarios = []
            
            usuarios.append(datos_usuario)
            
            with open('datos/usuarios.json', 'w', encoding='utf-8') as f:
                json.dump(usuarios, f, ensure_ascii=False, indent=4)
            mensaje += "✅ Guardado en archivo JSON. "
        
        if metodo == 'csv' or metodo == 'todos':
            # Guardar en archivo CSV
            file_exists = os.path.exists('datos/usuarios.csv')
            with open('datos/usuarios.csv', 'a', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(['Nombre', 'Email', 'Edad', 'Fecha'])
                writer.writerow([nombre, email, edad, fecha_actual])
            mensaje += "✅ Guardado en archivo CSV. "
        
        if metodo == 'sqlite' or metodo == 'todos':
            # Guardar en base de datos SQLite
            conn = sqlite3.connect('database/usuarios.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO usuarios (nombre, email, edad, fecha)
                VALUES (?, ?, ?, ?)
            ''', (nombre, email, edad, fecha_actual))
            conn.commit()
            conn.close()
            mensaje += "✅ Guardado en base de datos SQLite. "
        
        return render_template('resultado.html', 
                             datos=datos_usuario, 
                             mensaje=mensaje.strip())
    
    except Exception as e:
        return f"Error procesando formulario: {str(e)}"

@app.route('/datos_txt')
def leer_txt():
    datos = []
    try:
        if os.path.exists('datos/usuarios.txt'):
            with open('datos/usuarios.txt', 'r', encoding='utf-8') as f:
                for linea in f:
                    if linea.strip():
                        datos.append(linea.strip())
        else:
            datos = ["No hay datos guardados en archivo TXT todavía."]
    except Exception as e:
        datos = [f"Error leyendo archivo: {str(e)}"]
    
    return render_template('datos_txt.html', datos=datos)

@app.route('/datos_json')
def leer_json():
    datos = []
    try:
        if os.path.exists('datos/usuarios.json'):
            with open('datos/usuarios.json', 'r', encoding='utf-8') as f:
                datos = json.load(f)
        else:
            datos = [{"mensaje": "No hay datos guardados en archivo JSON todavía."}]
    except Exception as e:
        datos = [{"error": f"Error leyendo archivo JSON: {str(e)}"}]
    
    return render_template('datos_json.html', datos=datos)

@app.route('/datos_csv')
def leer_csv():
    datos = []
    try:
        if os.path.exists('datos/usuarios.csv'):
            with open('datos/usuarios.csv', 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                datos = list(reader)
        else:
            datos = [{"mensaje": "No hay datos guardados en archivo CSV todavía."}]
    except Exception as e:
        datos = [{"error": f"Error leyendo archivo CSV: {str(e)}"}]
    
    return render_template('datos_csv.html', datos=datos)

@app.route('/datos_sqlite')
def ver_usuarios():
    datos = []
    try:
        conn = sqlite3.connect('database/usuarios.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM usuarios ORDER BY id DESC')
        filas = cursor.fetchall()
        
        for fila in filas:
            datos.append({
                'id': fila[0],
                'nombre': fila[1],
                'email': fila[2],
                'edad': fila[3],
                'fecha': fila[4] if len(fila) > 4 and fila[4] else 'Sin fecha'
            })
        
        conn.close()
        
        if not datos:
            datos = [{"mensaje": "No hay usuarios registrados en la base de datos todavía."}]
            
    except Exception as e:
        datos = [{"error": f"Error leyendo base de datos: {str(e)}"}]
    
    return render_template('datos_sqlite.html', datos=datos)

# Rutas de redirección para compatibilidad con el navbar
@app.route('/leer_txt')
def redir_txt():
    return redirect(url_for('leer_txt'))

@app.route('/leer_json') 
def redir_json():
    return redirect(url_for('leer_json'))

@app.route('/leer_csv')
def redir_csv():
    return redirect(url_for('leer_csv'))

@app.route('/test')
def test():
    return "¡Flask está funcionando correctamente!"

# Ruta para limpiar la base de datos (opcional)
@app.route('/reset_db')
def reset_db():
    try:
        if os.path.exists('database/usuarios.db'):
            os.remove('database/usuarios.db')
        init_db()
        return "✅ Base de datos reiniciada correctamente. <a href='/'>Volver al inicio</a>"
    except Exception as e:
        return f"Error reiniciando base de datos: {str(e)}"

if __name__ == '__main__':
    print("🚀 Iniciando Flask con corrección de base de datos...")
    print("📁 Directorio actual:", os.getcwd())
    
    if os.path.exists('templates'):
        templates = os.listdir('templates')
        print(f"📋 Templates encontrados: {len(templates)} archivos")
    
    if os.path.exists('static'):
        print("✅ Carpeta 'static' existe")
    
    print("🗄️ Verificando y corrigiendo base de datos...")
    
    app.run(debug=True, port=5000)
=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return render_template('usuario.html', nombre=nombre)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
>>>>>>> 9bddd804a0b953ccb0f048ca2ad739fcc0ce6349
