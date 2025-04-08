from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask_cors import CORS, cross_origin 

from backend.blueprints.autores_blueprint import autores_blueprint
from backend.blueprints.libros_blueprint import libros_blueprint
from backend.blueprints.generos_blueprint import generos_blueprint

app = Flask(__name__)

app.register_blueprint(autores_blueprint, url_prefix='/home/autores')
app.register_blueprint(libros_blueprint, url_prefix='/home/libros')
app.register_blueprint(generos_blueprint, url_prefix='/home/generos')

cors = CORS(app)

if __name__ == "__main__":
    app.run(debug=True)