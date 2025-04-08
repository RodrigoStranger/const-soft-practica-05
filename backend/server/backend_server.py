from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)
SECRET_KEY = "clave_secreta"

def verify_token():
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith("Bearer "):
        return None

    token = auth_header.split(" ")[1]

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


if __name__ == '__main__':
    app.run(port=5002, debug=True)