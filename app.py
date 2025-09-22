from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import Usuario, DatoFormulario
from conexion.conexion import test_conexion

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_muy_segura_cambiar_en_produccion'

# Configuración de Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Por favor, inicia sesión para acceder a esta página.'
login_manager.login_message_category = 'warning'

@login_manager.user_loader
def load_user(user_id):
    """Función para cargar un usuario por su ID"""
    return Usuario.obtener_por_id(user_id)

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta de registro
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        print("🔍 === INICIO DE REGISTRO ===")
        
        nombre = request.form.get('nombre', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')
        
        print(f"📝 Datos recibidos: Nombre='{nombre}', Email='{email}', Password length={len(password)}")
        
        # Validaciones
        if not nombre or not email or not password:
            print("❌ Error: Campos vacíos")
            flash('Todos los campos son obligatorios', 'error')
            return render_template('registro.html')
        
        if password != confirm_password:
            print("❌ Error: Contraseñas no coinciden")
            flash('Las contraseñas no coinciden', 'error')
            return render_template('registro.html')
        
        if len(password) < 6:
            print("❌ Error: Contraseña muy corta")
            flash('La contraseña debe tener al menos 6 caracteres', 'error')
            return render_template('registro.html')
        
        if len(nombre) < 2:
            print("❌ Error: Nombre muy corto")
            flash('El nombre debe tener al menos 2 caracteres', 'error')
            return render_template('registro.html')
        
        print("✅ Validaciones pasadas, verificando email...")
        
        # Verificar si el email ya existe
        email_existe = Usuario.email_existe(email)
        print(f"📧 ¿Email existe? {email_existe}")
        
        if email_existe:
            print("❌ Error: Email ya registrado")
            flash('Este email ya está registrado', 'error')
            return render_template('registro.html')
        
        print("✅ Email disponible, creando usuario...")
        
        # Crear el usuario
        resultado_creacion = Usuario.crear_usuario(nombre, email, password)
        print(f"👤 Resultado de creación: {resultado_creacion}")
        
        if resultado_creacion:
            print("✅ Usuario creado exitosamente!")
            flash('¡Usuario registrado exitosamente! Ya puedes iniciar sesión.', 'success')
            return redirect(url_for('login'))
        else:
            print("❌ Error al crear usuario")
            flash('Error al registrar usuario. Intenta de nuevo.', 'error')
    
    return render_template('registro.html')

# Ruta de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        
        if not email or not password:
            flash('Email y contraseña son obligatorios', 'error')
            return render_template('login.html')
        
        # Buscar usuario
        usuario = Usuario.obtener_por_email(email)
        
        if usuario and usuario.verificar_password(password):
            login_user(usuario)
            flash(f'¡Bienvenido, {usuario.nombre}!', 'success')
            
            # Redirigir a la página solicitada o al dashboard
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Email o contraseña incorrectos', 'error')
    
    return render_template('login.html')

# Ruta para cerrar sesión
@app.route('/logout')
@login_required
def logout():
    nombre = current_user.nombre
    logout_user()
    flash(f'¡Hasta luego, {nombre}!', 'info')
    return redirect(url_for('index'))

# Ruta protegida - Dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    # Obtener los datos del usuario
    datos_usuario = DatoFormulario.obtener_por_usuario(current_user.id)
    return render_template('dashboard.html', usuario=current_user, datos=datos_usuario)

# Ruta protegida - Perfil
@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html', usuario=current_user)

# Ruta para el formulario de datos
@app.route('/formulario', methods=['GET', 'POST'])
@login_required
def formulario():
    if request.method == 'POST':
        titulo = request.form.get('titulo', '').strip()
        contenido = request.form.get('contenido', '').strip()
        
        if not titulo or not contenido:
            flash('Título y contenido son obligatorios', 'error')
            return render_template('datos_txt.html')
        
        if DatoFormulario.guardar_dato(current_user.id, titulo, contenido):
            flash('¡Datos guardados exitosamente!', 'success')
            return redirect(url_for('resultado', titulo=titulo, contenido=contenido))
        else:
            flash('Error al guardar los datos', 'error')
    
    return render_template('datos_txt.html')

# Ruta para mostrar resultado
@app.route('/resultado')
@login_required
def resultado():
    titulo = request.args.get('titulo', '')
    contenido = request.args.get('contenido', '')
    return render_template('resultado.html', titulo=titulo, contenido=contenido)

# Ruta para datos en texto plano
@app.route('/datos_txt')
@login_required
def datos_txt():
    return render_template('datos_txt.html')

# API para verificar conexión
@app.route('/api/test-db')
def test_db():
    if test_conexion():
        return jsonify({'status': 'success', 'message': 'Conexión exitosa'})
    else:
        return jsonify({'status': 'error', 'message': 'Error de conexión'}), 500

# Manejo de errores
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    print("🚀 Iniciando aplicación Flask...")
    print("📊 Probando conexión a la base de datos...")
    
    if test_conexion():
        print("✅ Conexión a la base de datos exitosa!")
        print("🌐 Servidor iniciando en: http://127.0.0.1:5000")
        app.run(debug=True, host='127.0.0.1', port=5000)
    else:
        print("❌ Error: No se pudo conectar a la base de datos")
        print("🔧 Verifica que MySQL esté ejecutándose y la base de datos exista")