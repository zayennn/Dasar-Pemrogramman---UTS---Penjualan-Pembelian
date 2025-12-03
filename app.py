from flask import Flask, render_template

# import blueprints
from blueprints.home.route import home_bp
from blueprints.products.route import products_bp
from blueprints.history.route import history_bp
from extensions import mysql

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(products_bp)
app.register_blueprint(history_bp)


# flask mysql db config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'db_project_uts'

# image
app.config['UPLOAD_FOLDER'] = 'static/images'

mysql.init_app(app)

if __name__ == "__main__" :
    app.run(debug=True)