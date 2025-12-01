from flask import Flask, render_template

# import blueprints
from blueprints.home.route import home_bp
from blueprints.products.route import products_bp
from blueprints.history.route import history_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(products_bp)
app.register_blueprint(history_bp)

if __name__ == "__main__" :
    app.run(debug=True)