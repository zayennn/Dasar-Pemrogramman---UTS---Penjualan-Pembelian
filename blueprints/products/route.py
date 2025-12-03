import os
from flask import Blueprint, render_template, request, url_for, redirect, current_app
from werkzeug.utils import secure_filename

from extensions import mysql

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/')
def index() :
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    return render_template('pages/products/index.html', products=products)

@products_bp.route('/create-product', methods=['GET', 'POST'])
def create() :
    if request.method == 'POST' :
        name = request.form['name']
        price = request.form['price']
        image = request.files['image']
        
        filename = None

        if image and image.filename != '': 
            filename = secure_filename(image.filename)
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(upload_path)
            
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO products (name, price, image) VALUES (%s, %s, %s)", (name, price, filename))
        mysql.connection.commit()
        cursor.close()

        return redirect(url_for('products.index'))
            
    return render_template('pages/products/create.html')

@products_bp.route('/edit-product/<int:id>', methods=['GET', 'POST'])
def update(id) :
    if request.method == 'POST' :
        name = request.form['name']
        price = request.form['price']
        image = request.files['image']
        
        cursor = mysql.connection.cursor()
        
        if image and image.filename != '':
            filename = secure_filename(image.filename)
            upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            image.save(upload_path)
            
            cursor.execute("UPDATE products SET name = %s, price = %s, image = %s WHERE id = %s", 
                         (name, price, filename, id))
        else:
            cursor.execute("UPDATE products SET name = %s, price = %s WHERE id = %s", 
                         (name, price, id))
        
        mysql.connection.commit()
        cursor.close()
        
        return redirect(url_for('products.index'))
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
    product = cursor.fetchone()
    cursor.close()
    
    if not product:
        return redirect(url_for('products.index'))
    
    return render_template('pages/products/update.html', product=product)

@products_bp.route('/delete-product/<int:id>', methods=['POST'])
def destroy(id) :
    cursor = mysql.connection.cursor()
    
    cursor.execute("SELECT image FROM products WHERE id = %s", (id,))
    product = cursor.fetchone()
    
    if product:
        cursor.execute("DELETE FROM products WHERE id = %s", (id,))
        mysql.connection.commit()
        
        if product[0]:
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], product[0])
            if os.path.exists(image_path):
                os.remove(image_path)
    
    cursor.close()
    return redirect(url_for('products.index'))