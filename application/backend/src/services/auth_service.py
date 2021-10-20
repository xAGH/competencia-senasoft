from flask import request, make_response, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime

class AuthService:

    def signin(self, username, password):
        pass

    def signup(self):
        pass