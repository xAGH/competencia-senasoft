from flask import request, make_response, jsonify
from functools import wraps
from os import getenv
from jwt import decode, DecodeError, InvalidTokenError, InvalidKeyError
from werkzeug.exceptions import RequestTimeout

"""
    :decorator @verify_token — Verifica el token enviado por cabecera y devuelve una autorización.
"""
def verify_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        token: str = request.headers.get('Authorization', 'Auth')
        try:
            data = decode(token, getenv("JWT_SECRET_KEY"), algorithms=["HS256"])
        except DecodeError:
            return make_response(jsonify({
                "statusCode": 401,
                "message": "Token is missing or invalid"
            }), 401)
        except InvalidTokenError:
            return make_response(jsonify({
                "statusCode": 401,
                "message": "Invalid token error"
            }), 401)
        except InvalidKeyError:
            return make_response(jsonify({
                "statusCode": 401,
                "message": "Invalid signature error, can't to read"
            }), 401)
        return func(*args, **kwargs)
    return wrapped