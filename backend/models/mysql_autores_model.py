from backend.models.mysql_connection_pool import MySQLPool

class AutoresModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def crear_autor(self, nombre, fecha_nacimiento, nacionalidad):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('CrearAutor', (nombre, fecha_nacimiento, nacionalidad))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def obtener_autor_por_id(self, id_autor):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ObtenerAutorPorId', (id_autor,))
            result = cursor.stored_results()
            autor = None
            for r in result:
                autor = r.fetchone()
            cursor.close()
            conn.close()
            return autor
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def obtener_autores(self):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ObtenerAutores')
            result = cursor.stored_results()
            autores = []
            for r in result:
                autores = r.fetchall()
            cursor.close()
            conn.close()
            return autores
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def actualizar_autor(self, id_autor, nombre, fecha_nacimiento, nacionalidad):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ActualizarAutor', (id_autor, nombre, fecha_nacimiento, nacionalidad))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def asignar_autor_a_libro(self, id_autor, id_libro):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('AsignarAutorALibro', (id_autor, id_libro))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e