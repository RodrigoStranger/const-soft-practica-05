import mysql.connector
import jwt
import datetime
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
SECRET_KEY = os.getenv('SECRET_KEY')

dbconfig = {
    "host": os.getenv("MYSQL_HOST"),
    "port": int(os.getenv("MYSQL_PORT")),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE_2"),
}

@app.route('/login', methods=['POST'])
def generate_token():
    data = request.json
    if not data.get('nombre') or not data.get('contraseña'):
        return jsonify({'error': 'Nombre de usuario o contraseña faltante'}), 400
    try:
        conn = mysql.connector.connect(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre = %s", (data.get('nombre'),))
        user = cursor.fetchone()
        if user:
            if user[2] == data.get('contraseña'):
                payload = {
                    'user': user[1],
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                cursor.close()
                conn.close()
                return jsonify({'token': token})
            else:
                cursor.close()
                conn.close()
                return jsonify({'error': 'Credenciales inválidas'}), 401
        else:
            cursor.close()
            conn.close()
            return jsonify({'error': 'Credenciales inválidas'}), 401

    except mysql.connector.Error as err:
        return jsonify({'error': f'Error en la base de datos: {err}'}), 500
    
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(port=5001, debug=True)