from flask import Blueprint, request, jsonify
from backend.models.mysql_libros_model import LibrosModel
from sever_auth.authentication import verify_token

libros_blueprint = Blueprint('libros_blueprint', __name__)
libros_model = LibrosModel()

@libros_blueprint.route('/crearlibro', methods=['POST'])
def crear_libro():
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        titulo = data['titulo']
        fecha_publicacion = data['fecha_publicacion']
        descripcion = data['descripcion']
        libros_model.crear_libro(titulo, fecha_publicacion, descripcion)
        return jsonify({'mensaje': f'El libro {titulo} fue creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@libros_blueprint.route('/obtenerlibro/<int:id_libro>', methods=['GET'])
def obtener_libro(id_libro):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        libro = libros_model.obtener_libro_por_id(id_libro)
        if not libro:
            return jsonify({'mensaje': 'Libro no encontrado'}), 404
        return jsonify(libro), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@libros_blueprint.route('/obtenerlibros', methods=['GET'])
def obtener_libros():
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        libros = libros_model.obtener_libros()
        return jsonify(libros), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@libros_blueprint.route('/actualizarlibro/titulo/<int:id_libro>', methods=['PUT'])
def actualizar_titulo_libro(id_libro):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        nuevo_titulo = data['titulo']
        libros_model.actualizar_titulo_libro(id_libro, nuevo_titulo)
        return jsonify({'mensaje': f'Título del libro actualizado exitosamente a {nuevo_titulo}'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@libros_blueprint.route('/actualizarlibro/detalles/<int:id_libro>', methods=['PUT'])
def actualizar_detalles_libro(id_libro):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        fecha_publicacion = data['fecha_publicacion']
        descripcion = data['descripcion']
        libros_model.actualizar_detalles_libro(id_libro, fecha_publicacion, descripcion)
        return jsonify({'mensaje': 'Detalles del libro actualizados exitosamente'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@libros_blueprint.route('/desactivarlibro/desactivar', methods=['PUT'])
def desactivar_libro():
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        id_libro = data['id_libro']
        libros_model.desactivar_libro(id_libro)
        return jsonify({'mensaje': 'Libro desactivado exitosamente'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@libros_blueprint.route('/activarlibro/activar', methods=['PUT'])
def activar_libro():
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        id_libro = data['id_libro']
        libros_model.activar_libro(id_libro)
        return jsonify({'mensaje': 'Libro activado exitosamente'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@libros_blueprint.route('/obtenerautoresporlibro/<int:id_libro>', methods=['GET'])
def obtener_autores_por_libro(id_libro):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        autores = libros_model.listar_autores_por_libro(id_libro)
        if not autores:
            return jsonify({'mensaje': 'No se encontraron autores para este libro.'}), 404
        return jsonify(autores), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400