from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>¡Bienvenido al proyecto de David Cerda!</h1>'

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return f'<h1>Perfil de {nombre}</h1>'

if __name__ == '__main__':
    app.run(debug=True)