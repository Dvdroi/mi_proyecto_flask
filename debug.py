import mysql.connector

try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='admin',
        database='desarrollo_web'
    )
    print("✅ Conexión exitosa")
    
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tablas = cursor.fetchall()
    print(f"Tablas: {tablas}")
    
    cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES ('Test', 'test@example.com', 'password123')")
    conn.commit()
    print("✅ Usuario insertado exitosamente")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"❌ Error: {e}")