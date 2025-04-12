from flask import Blueprint, request, jsonify
from backend.models.mysql_generos_model import GenerosModel
from sever_auth.authentication import verify_token

generos_blueprint = Blueprint('generos_blueprint', __name__)
generos_model = GenerosModel()

@generos_blueprint.route('/creargenero', methods=['POST'])
def crear_genero():
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        nombre = data['nombre']
        descripcion = data['descripcion']
        generos_model.crear_genero(nombre, descripcion)
        return jsonify({'mensaje': f'El género {nombre} fue creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@generos_blueprint.route('/obtenergenero/<int:id_genero>', methods=['GET'])
def obtener_genero(id_genero):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
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
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        generos = generos_model.obtener_generos()
        return jsonify(generos), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@generos_blueprint.route('/actualizargenero/nombre/<int:id_genero>', methods=['PUT'])
def actualizar_nombre_genero(id_genero):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        nuevo_nombre = data['nombre']
        generos_model.actualizar_nombre_genero(id_genero, nuevo_nombre)
        return jsonify({'mensaje': f'Nombre del género actualizado exitosamente a {nuevo_nombre}'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@generos_blueprint.route('/actualizargenero/descripcion/<int:id_genero>', methods=['PUT'])
def actualizar_descripcion_genero(id_genero):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        descripcion = data['descripcion']
        generos_model.actualizar_detalles_genero(id_genero, descripcion)
        return jsonify({'mensaje': 'Descripción del género actualizada exitosamente'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@generos_blueprint.route('/asignargeneralibro', methods=['POST'])
def asignar_genero_a_libro():
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        id_genero = data['id_genero']
        id_libro = data['id_libro']
        generos_model.asignar_genero_a_libro(id_genero, id_libro)
        return jsonify({'mensaje': 'Género asignado al libro exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
    
@generos_blueprint.route('/obtenerlibrosporgenero/<int:id_genero>', methods=['GET'])
def listar_libros_por_genero(id_genero):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        genero = generos_model.listar_libros_por_genero(id_genero)
        if not genero:
            return jsonify({'mensaje': 'Género no encontrado'}), 404
        return jsonify(genero), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400