from flask import Blueprint, render_template

from extensions import mysql

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index() :
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM products")
    product_count = cursor.fetchone()[0]
    cursor.close()
    return render_template('pages/home/index.html', product_count=product_count)