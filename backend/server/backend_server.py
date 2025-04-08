from flask import Flask, request, jsonify
import jwt
import datetime
import os
import mysql.connector

app = Flask(__name__)

SECRET_KEY = os.getenv("SECRET_KEY", "clave_secreta")

dbconfig = {
    "host": os.getenv("MYSQL_HOST"),
    "port": os.getenv("MYSQL_PORT"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DATABASE_2"),
}

def get_db_connection():
    return mysql.connector.connect(
        host=dbconfig["host"],
        port=dbconfig["port"],
        user=dbconfig["user"],
        password=dbconfig["password"],
        database=dbconfig["database"]
    )

@app.route('/login/token', methods=['POST'])
def generate_token():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.callproc('validar_usuario', [username, password])
        payload = {
            'user': username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return jsonify({'access_token': token})
    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 401
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(port=5001, debug=True)