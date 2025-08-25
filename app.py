from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <h1>¡Bienvenido al proyecto de David Cerda!</h1>
    <p>Esta es mi aplicación Flask personalizada.</p>
    <ul>
        <li><a href="/usuario/David">Ver perfil de David</a></li>
        <li><a href="/about">Acerca de</a></li>
    </ul>
    ''')

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'<h1>Perfil de {nombre}</h1><p>¡Hola {nombre}!</p>'

@app.route('/about')
def about():
    return '<h1>Acerca de David Cerda</h1><p>Desarrollador Python/Flask</p>'

if __name__ == '__main__':
    app.run(debug=True)