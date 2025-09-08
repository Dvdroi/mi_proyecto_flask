from flask import Flask, render_template, request, redirect, url_for
import json
import csv
import os
from datetime import datetime
import sqlite3

app = Flask(__name__)

# Crear directorios necesarios
os.makedirs('datos', exist_ok=True)

def guardar_en_txt(datos):
    with open('datos/usuarios.txt', 'a', encoding='utf-8') as archivo:
        archivo.write(f"Nombre: {datos['nombre']}, Email: {datos['email']}, Edad: {datos['edad']}, Fecha: {datos['fecha']}\n")

def guardar_en_json(datos):
    try:
        with open('datos/usuarios.json', 'r', encoding='utf-8') as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        usuarios = []
    
    usuarios.append(datos)
    
    with open('datos/usuarios.json', 'w', encoding='utf-8') as archivo:
        json.dump(usuarios, archivo, ensure_ascii=False, indent=2)

def guardar_en_csv(datos):
    archivo_existe = os.path.exists('datos/usuarios.csv')
    
    with open('datos/usuarios.csv', 'a', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=['nombre', 'email', 'edad', 'fecha'])
        
        if not archivo_existe:
            escritor.writeheader()
        
        escritor.writerow(datos)

def guardar_en_bd(datos):
    conn = sqlite3.connect('datos/usuarios.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            edad INTEGER NOT NULL,
            fecha TEXT NOT NULL
        )
    ''')
    
    cursor.execute('''
        INSERT INTO usuarios (nombre, email, edad, fecha)
        VALUES (?, ?, ?, ?)
    ''', (datos['nombre'], datos['email'], datos['edad'], datos['fecha']))
    
    conn.commit()
    conn.close()

def leer_desde_txt():
    try:
        with open('datos/usuarios.txt', 'r', encoding='utf-8') as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        return []

def leer_desde_json():
    try:
        with open('datos/usuarios.json', 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def leer_desde_csv():
    try:
        usuarios = []
        with open('datos/usuarios.csv', 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuarios.append(fila)
        return usuarios
    except FileNotFoundError:
        return []

def leer_desde_bd():
    try:
        conn = sqlite3.connect('datos/usuarios.db')
        cursor = conn.cursor()
        cursor.execute('SELECT nombre, email, edad, fecha FROM usuarios ORDER BY id DESC')
        usuarios = cursor.fetchall()
        conn.close()
        
        return [{'nombre': u[0], 'email': u[1], 'edad': u[2], 'fecha': u[3]} for u in usuarios]
    except sqlite3.Error:
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form['nombre']
    email = request.form['email']
    edad = int(request.form['edad'])
    formato = request.form['formato']
    
    datos = {
        'nombre': nombre,
        'email': email,
        'edad': edad,
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    if formato == 'txt':
        guardar_en_txt(datos)
    elif formato == 'json':
        guardar_en_json(datos)
    elif formato == 'csv':
        guardar_en_csv(datos)
    elif formato == 'bd':
        guardar_en_bd(datos)
    
    return redirect(url_for('mostrar_datos', formato=formato))

@app.route('/datos/<formato>')
def mostrar_datos(formato):
    if formato == 'txt':
        datos = leer_desde_txt()
        return render_template('mostrar_datos.html', datos=datos, formato='TXT', tipo='lineas')
    elif formato == 'json':
        datos = leer_desde_json()
        return render_template('mostrar_datos.html', datos=datos, formato='JSON', tipo='json')
    elif formato == 'csv':
        datos = leer_desde_csv()
        return render_template('mostrar_datos.html', datos=datos, formato='CSV', tipo='tabla')
    elif formato == 'bd':
        datos = leer_desde_bd()
        return render_template('mostrar_datos.html', datos=datos, formato='Base de Datos', tipo='tabla')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)