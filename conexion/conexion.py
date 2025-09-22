import mysql.connector
from mysql.connector import Error
import os

def crear_conexion():
    """
    Crea y devuelve una conexión a la base de datos MySQL
    """
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            database='desarrollo_web',
            user='root',
            password='admin',  # Tu contraseña de MySQL
            charset='utf8mb4',
            collation='utf8mb4_unicode_ci',
            autocommit=True
        )
        
        if conexion.is_connected():
            print("Conexión exitosa a MySQL")
            return conexion
            
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def cerrar_conexion(conexion):
    """
    Cierra la conexión a la base de datos
    """
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

def ejecutar_consulta(consulta, parametros=None, fetch=True):
    """
    Ejecuta una consulta SQL y devuelve los resultados
    """
    conexion = crear_conexion()
    cursor = None
    resultado = None
    
    try:
        if conexion:
            cursor = conexion.cursor(dictionary=True)
            cursor.execute(consulta, parametros)
            
            if fetch:
                resultado = cursor.fetchall()
            else:
                resultado = cursor.rowcount
                
    except Error as e:
        print(f"Error al ejecutar consulta: {e}")
        if conexion:
            conexion.rollback()
            
    finally:
        if cursor:
            cursor.close()
        if conexion:
            cerrar_conexion(conexion)
            
    return resultado

def test_conexion():
    """
    Función para probar la conexión
    """
    conexion = crear_conexion()
    if conexion:
        print("✅ Conexión a la base de datos exitosa!")
        cerrar_conexion(conexion)
        return True
    else:
        print("❌ Error al conectar a la base de datos!")
        return False