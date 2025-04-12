from flask import Blueprint, request, jsonify
from backend.models.mysql_autores_model import AutoresModel
from sever_auth.authentication import verify_token

autores_blueprint = Blueprint('autores_blueprint', __name__)
autores_model = AutoresModel()

@autores_blueprint.route('/crearautor', methods=['POST'])
def crear_autor():
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        nombre = data['nombre']
        fecha_nacimiento = data['fecha_nacimiento']
        nacionalidad = data['nacionalidad']
        autores_model.crear_autor(nombre, fecha_nacimiento, nacionalidad)
        return jsonify({'mensaje': f'El autor {nombre} fue creado exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@autores_blueprint.route('/obtenerautor/<int:id_autor>', methods=['GET'])
def obtener_autor(id_autor):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
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
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        autores = autores_model.obtener_autores()
        return jsonify(autores), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400

@autores_blueprint.route('/actualizarautor/nombre/<int:id_autor>', methods=['PUT'])
def actualizar_nombre_autor(id_autor):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        nuevo_nombre = data['nombre']
        autores_model.actualizar_nombre_autor(id_autor, nuevo_nombre)
        return jsonify({'mensaje': f'Nombre del autor actualizado exitosamente a {nuevo_nombre}'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
        
@autores_blueprint.route('/actualizarautor/detalles/<int:id_autor>', methods=['PUT'])
def actualizar_detalles_autor(id_autor):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        fecha_nacimiento = data['fecha_nacimiento']
        nacionalidad = data['nacionalidad']
        autores_model.actualizar_detalles_autor(id_autor, fecha_nacimiento, nacionalidad)
        return jsonify({'mensaje': 'Detalles del autor actualizados exitosamente'}), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
       
@autores_blueprint.route('/asignarautoralibro', methods=['POST'])
def asignar_autor_a_libro():
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        data = request.get_json()
        id_autor = data['id_autor']
        id_libro = data['id_libro']
        autores_model.asignar_autor_a_libro(id_autor, id_libro)
        return jsonify({'mensaje': 'Autor asignado al libro exitosamente'}), 201
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
    
@autores_blueprint.route('/obtenerlibrosporautor/<int:id_autor>', methods=['GET'])
def obtener_libros_por_autor(id_autor):
    if not verify_token():
        return jsonify({'error': 'Acceso no autorizado'}), 401
    try:
        libros = autores_model.listar_libros_por_autor(id_autor)
        if not libros:
            return jsonify({'mensaje': 'No se encontraron libros para este autor.'}), 404
        return jsonify(libros), 200
    except Exception as e:
        return jsonify({'mensaje': str(e)}), 400
