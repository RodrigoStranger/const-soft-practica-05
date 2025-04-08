from flask import Blueprint, request, jsonify
from backend.models.mysql_autores_model import AutoresModel
from .server_blueprint import verify_token

autores_blueprint = Blueprint('autores_blueprint', __name__)
autores_model = AutoresModel()

@autores_blueprint.route('/crearautor', methods=['POST'])
def crear_autor():
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        data = request.get_json()
        nombre = data['nombre']
        fecha_nacimiento = data['fecha_nacimiento']
        nacionalidad = data['nacionalidad']
        
        autores_model.crear_autor(nombre, fecha_nacimiento, nacionalidad)
        return jsonify({'mensaje': 'Autor creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@autores_blueprint.route('/obtenerautor/autor/<int:id_autor>', methods=['GET'])
def obtener_autor(id_autor):
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        autor = autores_model.obtener_autor_por_id(id_autor)
        if not autor:
            return jsonify({'mensaje': 'Autor no encontrado'}), 404
        return jsonify(autor), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@autores_blueprint.route('/obtenerautores', methods=['GET'])
def obtener_autores():
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        autores = autores_model.obtener_autores()
        return jsonify(autores), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@autores_blueprint.route('/actualizarautor/nombre/<int:id_autor>', methods=['PUT'])
def actualizar_nombre_autor(id_autor):
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        data = request.get_json()
        nombre = data['nombre']
        autores_model.actualizar_nombre_autor(id_autor, nombre)
        return jsonify({'mensaje': 'Nombre del autor actualizado exitosamente'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
        
@autores_blueprint.route('/actualizarautor/detalles/<int:id_autor>', methods=['PUT'])
def actualizar_detalles_autor(id_autor):
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        data = request.get_json()
        fecha_nacimiento = data['fecha_nacimiento']
        nacionalidad = data['nacionalidad']
        autores_model.actualizar_detalles_autor(id_autor, fecha_nacimiento, nacionalidad)
        return jsonify({'mensaje': 'Detalles del autor actualizados exitosamente'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
        
'''
@autores_blueprint.route('/asignarautoralibro/autor/<int:id_autor>/libro/<int:id_libro>', methods=['POST'])
def asignar_autor_a_libro(id_autor, id_libro):
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        autores_model.asignar_autor_a_libro(id_autor, id_libro)
        return jsonify({'mensaje': 'Autor asignado al libro exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
'''
@autores_blueprint.route('/asignarautoralibro', methods=['POST'])
def asignar_autor_a_libro():
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        data = request.get_json()
        id_autor = data['id_autor']
        id_libro = data['id_libro']
        autores_model.asignar_autor_a_libro(id_autor, id_libro)
        return jsonify({'mensaje': 'Autor asignado al libro exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
    
@autores_blueprint.route('/obtenerlibrosporautor/autor/<int:id_autor>', methods=['GET'])
def obtener_libros_por_autor(id_autor):
    if not verify_token():
        return jsonify({'error': 'Token inválido'}), 401
    try:
        libros = autores_model.listar_libros_por_autor(id_autor)
        if not libros:
            return jsonify({'mensaje': 'No se encontraron libros para este autor.'}), 404
        return jsonify(libros), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
