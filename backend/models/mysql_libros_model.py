from backend.models.mysql_connection_pool import MySQLPool

class LibrosModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def crear_libro(self, titulo, fecha_publicacion, descripcion):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('CrearLibro', (titulo, fecha_publicacion, descripcion))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def obtener_libro_por_id(self, id_libro):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ObtenerLibroPorId', (id_libro,))
            result = cursor.stored_results()
            libro = None
            for r in result:
                libro = r.fetchone()
            cursor.close()
            conn.close()
            return libro
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def obtener_libros(self):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ObtenerLibros')
            result = cursor.stored_results()
            libros = []
            for r in result:
                libros = r.fetchall()
            cursor.close()
            conn.close()
            return libros
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def actualizar_titulo_libro(self, id_libro, nuevo_titulo):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ActualizarTituloLibro', (id_libro, nuevo_titulo))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e
    
    def actualizar_detalles_libro(self, id_libro, fecha_publicacion, descripcion):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ActualizarDetallesLibro', (id_libro, fecha_publicacion, descripcion))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def desactivar_libro(self, id_libro):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('DesactivarLibro', (id_libro,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e

    def activar_libro(self, id_libro):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ActivarLibro', (id_libro,))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            if conn:
                conn.close()
            raise e
    
    def listar_autores_por_libro(self, id_libro):
        try:
            conn = self.mysql_pool.pool.get_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.callproc('ObtenerAutoresPorLibro', (id_libro,))
            autores = []
            for result in cursor.stored_results():
                autores = result.fetchall()
            cursor.close()
            conn.close()
            return autores
        except Exception as e:
            if conn:
                conn.close()
            raise e
