from flask import Blueprint, render_template, request

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/')
def index() :
    return render_template('pages/products/index.html')

@products_bp.route('/create-product')
def create() :
    return render_template('pages/products/create.html')