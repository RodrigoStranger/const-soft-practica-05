from backend.models.mysql_connection_pool import MySQLPool

class GenerosModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def crear_genero(self, nombre, descripcion):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('CrearGenero', (nombre, descripcion))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def obtener_genero_por_id(self, id_genero):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ObtenerGeneroPorId', (id_genero,))
            result = cursor.stored_results()
            genero = None
            for r in result:
                genero = r.fetchone()
            cursor.close()
            conn.close()
            return genero
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def obtener_generos(self):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ObtenerGeneros')
            result = cursor.stored_results()
            generos = []
            for r in result:
                generos = r.fetchall()
            cursor.close()
            conn.close()
            return generos
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def actualizar_nombre_genero(self, id_genero, nombre):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ActualizarNombreGenero', (id_genero, nombre))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def actualizar_detalles_genero(self, id_genero, descripcion):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ActualizarDetallesGenero', (id_genero, descripcion))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def asignar_genero_a_libro(self, id_genero, id_libro):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('AsignarGeneroALibro', (id_genero, id_libro))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e
