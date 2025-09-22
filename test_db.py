from conexion.conexion import test_conexion, ejecutar_consulta
from models import Usuario

print("=== PRUEBA DE CONEXIÓN ===")
test_conexion()

print("\n=== PRUEBA DE CONSULTA ===")
try:
    # Verificar que las tablas existan
    resultado = ejecutar_consulta("SHOW TABLES")
    print(f"Tablas encontradas: {resultado}")
    
    # Verificar estructura de tabla usuarios
    resultado = ejecutar_consulta("DESCRIBE usuarios")
    print(f"Estructura tabla usuarios: {resultado}")
    
    # Verificar si el email ya existe
    email_test = "deiki.mc@gmail.com"
    existe = Usuario.email_existe(email_test)
    print(f"¿El email {email_test} existe? {existe}")
    
    # Intentar crear usuario de prueba
    print("\n=== PRUEBA DE CREACIÓN DE USUARIO ===")
    resultado = Usuario.crear_usuario("Test User", "test@example.com", "123456")
    print(f"Usuario creado: {resultado}")
    
except Exception as e:
    print(f"Error en las pruebas: {e}")
    import traceback
    traceback.print_exc()