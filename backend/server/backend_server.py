import mysql.connector
import os
import jwt
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
SECRET_KEY = os.getenv('SECRET_KEY')

dbconfig = {
    "host": os.getenv("MYSQL_HOST"),
    "port": os.getenv("MYSQL_PORT"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE_2"),
}

@app.route('/login/token', methods=['POST'])
def generate_token():
    data = request.json
    try:
        conn = mysql.connector.connect(
            host=dbconfig["host"],
            port=int(dbconfig["port"]),
            user=dbconfig["user"],
            password=dbconfig["password"],
            database=dbconfig["database"]
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nombre = %s AND contraseña = %s", 
                       (data.get('nombre'), data.get('contraseña')))
        user = cursor.fetchone()
        if user:
            payload = {
                'user': user[1],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
            cursor.close()
            conn.close()
            return jsonify({'Token de acceso': token})
        cursor.close()
        conn.close()
        return jsonify({'error': 'credenciales inválidas'}), 401
    except mysql.connector.Error as err:
        return jsonify({'error': f"Error de la base de datos: {err}"}), 500

if __name__ == '__main__':
    app.run(port=5001, debug=True)