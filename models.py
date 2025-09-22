from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from conexion.conexion import ejecutar_consulta

class Usuario(UserMixin):
    def __init__(self, id_usuario, nombre, email, password):
        self.id = str(id_usuario)  # Flask-Login requiere que sea string
        self.nombre = nombre
        self.email = email
        self.password_hash = password

    def verificar_password(self, password):
        """Verifica si la contraseña proporcionada coincide con el hash"""
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def crear_usuario(nombre, email, password):
        """Crea un nuevo usuario en la base de datos"""
        try:
            password_hash = generate_password_hash(password)
            consulta = """
                INSERT INTO usuarios (nombre, email, password) 
                VALUES (%s, %s, %s)
            """
            parametros = (nombre, email, password_hash)
            resultado = ejecutar_consulta(consulta, parametros, fetch=False)
            return resultado > 0
        except Exception as e:
            print(f"Error al crear usuario: {e}")
            return False

    @staticmethod
    def obtener_por_email(email):
        """Obtiene un usuario por su email"""
        try:
            consulta = "SELECT * FROM usuarios WHERE email = %s"
            resultado = ejecutar_consulta(consulta, (email,))
            
            if resultado and len(resultado) > 0:
                user_data = resultado[0]
                return Usuario(
                    user_data['id_usuario'],
                    user_data['nombre'],
                    user_data['email'],
                    user_data['password']
                )
            return None
        except Exception as e:
            print(f"Error al obtener usuario por email: {e}")
            return None

    @staticmethod
    def obtener_por_id(user_id):
        """Obtiene un usuario por su ID"""
        try:
            consulta = "SELECT * FROM usuarios WHERE id_usuario = %s"
            resultado = ejecutar_consulta(consulta, (user_id,))
            
            if resultado and len(resultado) > 0:
                user_data = resultado[0]
                return Usuario(
                    user_data['id_usuario'],
                    user_data['nombre'],
                    user_data['email'],
                    user_data['password']
                )
            return None
        except Exception as e:
            print(f"Error al obtener usuario por ID: {e}")
            return None

    @staticmethod
    def email_existe(email):
        """Verifica si un email ya existe en la base de datos"""
        try:
            consulta = "SELECT COUNT(*) as count FROM usuarios WHERE email = %s"
            resultado = ejecutar_consulta(consulta, (email,))
            return resultado[0]['count'] > 0 if resultado else False
        except Exception as e:
            print(f"Error al verificar email: {e}")
            return False

class DatoFormulario:
    """Modelo para manejar los datos del formulario"""
    
    @staticmethod
    def guardar_dato(usuario_id, titulo, contenido):
        """Guarda un nuevo dato del formulario"""
        try:
            consulta = """
                INSERT INTO datos_formulario (usuario_id, titulo, contenido) 
                VALUES (%s, %s, %s)
            """
            parametros = (usuario_id, titulo, contenido)
            resultado = ejecutar_consulta(consulta, parametros, fetch=False)
            return resultado > 0
        except Exception as e:
            print(f"Error al guardar dato: {e}")
            return False

    @staticmethod
    def obtener_por_usuario(usuario_id):
        """Obtiene todos los datos de un usuario"""
        try:
            consulta = """
                SELECT * FROM datos_formulario 
                WHERE usuario_id = %s 
                ORDER BY fecha_creacion DESC
            """
            resultado = ejecutar_consulta(consulta, (usuario_id,))
            return resultado if resultado else []
        except Exception as e:
            print(f"Error al obtener datos del usuario: {e}")
            return []