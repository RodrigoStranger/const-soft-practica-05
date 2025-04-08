from flask import Blueprint, request, jsonify
from backend.models.mysql_generos_model import GenerosModel
from server_blueprint import verify_token

generos_blueprint = Blueprint('generos_blueprint', __name__)
generos_model = GenerosModel()

@generos_blueprint.route('/creargenero', methods=['POST'])
def crear_genero():
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        
        generos_model.crear_genero(nombre, descripcion)
        return jsonify({'mensaje': 'Género creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@generos_blueprint.route('/obtenergenero/<int:id_genero>', methods=['GET'])
def obtener_genero(id_genero):
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        genero = generos_model.obtener_genero_por_id(id_genero)
        if not genero:
            return jsonify({'mensaje': 'Género no encontrado'}), 404
        return jsonify(genero), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@generos_blueprint.route('/obtenergeneros', methods=['GET'])
def obtener_generos():
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        generos = generos_model.obtener_generos()
        return jsonify(generos), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@generos_blueprint.route('/actualizargenero/<int:id_genero>', methods=['PUT'])
def actualizar_genero(id_genero):
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        generos_model.actualizar_genero(id_genero, nombre, descripcion)
        return jsonify({'mensaje': 'Género actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

'''
@generos_blueprint.route('/asignargeneralibro/genero/<int:id_genero>/libro/<int:id_libro>', methods=['POST'])
def asignar_genero_a_libro(id_genero, id_libro):
    if not verify_token():
            return jsonify({'error': 'Token inválido'}), 401
    try:
        generos_model.asignar_genero_a_libro(id_genero, id_libro)
        return jsonify({'mensaje': 'Género asignado al libro exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
'''

@generos_blueprint.route('/asignargeneralibro', methods=['POST'])
def asignar_genero_a_libro():
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        data = request.get_json()
        id_genero = data['id_genero']
        id_libro = data['id_libro']
        generos_model.asignar_genero_a_libro(id_genero, id_libro)
        return jsonify({'mensaje': 'Género asignado al libro exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400