from flask import Flask, render_template, request, redirect, url_for, flash
from database import Database

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia esto por una clave segura
db = Database()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    query = "SELECT * FROM productos ORDER BY id_producto DESC"
    productos = db.fetch_all(query)
    return render_template('productos.html', productos=productos)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        
        # Validación básica
        if not nombre or not precio or not stock:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('crear'))
        
        try:
            precio = float(precio)
            stock = int(stock)
            
            if precio < 0 or stock < 0:
                flash('El precio y stock deben ser valores positivos', 'error')
                return redirect(url_for('crear'))
            
            query = "INSERT INTO productos (nombre, precio, stock) VALUES (%s, %s, %s)"
            db.execute_query(query, (nombre, precio, stock))
            flash('Producto creado exitosamente', 'success')
            return redirect(url_for('productos'))
        
        except ValueError:
            flash('Precio y stock deben ser valores numéricos', 'error')
            return redirect(url_for('crear'))
    
    return render_template('crear.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        
        # Validación
        if not nombre or not precio or not stock:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('editar', id=id))
        
        try:
            precio = float(precio)
            stock = int(stock)
            
            if precio < 0 or stock < 0:
                flash('El precio y stock deben ser valores positivos', 'error')
                return redirect(url_for('editar', id=id))
            
            query = "UPDATE productos SET nombre=%s, precio=%s, stock=%s WHERE id_producto=%s"
            db.execute_query(query, (nombre, precio, stock, id))
            flash('Producto actualizado exitosamente', 'success')
            return redirect(url_for('productos'))
        
        except ValueError:
            flash('Precio y stock deben ser valores numéricos', 'error')
            return redirect(url_for('editar', id=id))
    
    query = "SELECT * FROM productos WHERE id_producto = %s"
    producto = db.fetch_one(query, (id,))
    
    if not producto:
        flash('Producto no encontrado', 'error')
        return redirect(url_for('productos'))
    
    return render_template('editar.html', producto=producto)

@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar(id):
    # Verificar que el producto existe antes de eliminar
    query_verificar = "SELECT * FROM productos WHERE id_producto = %s"
    producto = db.fetch_one(query_verificar, (id,))
    
    if not producto:
        flash('El producto no existe', 'error')
        return redirect(url_for('productos'))
    
    # Eliminar el producto
    query = "DELETE FROM productos WHERE id_producto = %s"
    db.execute_query(query, (id,))
    flash(f'Producto "{producto["nombre"]}" eliminado exitosamente', 'success')
    return redirect(url_for('productos'))

if __name__ == '__main__':
    app.run(debug=True)