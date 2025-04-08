from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)
SECRET_KEY = "clave_secreta"

def verify_token():
    token = request.headers.get('Authorization')
    if not token:
        return False
    try:
        token = token.split(' ')[1]  # Eliminar el prefijo 'Bearer '
        jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return True
    except:
        return False

# Endpoint para obtener token OAuth
@app.route('/login/token', methods=['POST'])
def generate_token():
    data = request.json
    if not data or data.get('username') != 'admin' or data.get('password') != '1234':
        return jsonify({'error': 'Invalid credentials'}), 401
    payload = {
        'user': data['username'],
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return jsonify({'access_token': token})