from flask import json, request, make_response, jsonify
from flask.views import MethodView
from src.models import Model
from werkzeug.security import generate_password_hash, check_password_hash

class UsersController(MethodView):

    def __init__(self):
        self.model = Model()

    def post(self):

        if request.is_json:
            try:
                email = request.json['email']
                verify_data = self.model.fetch_one("SELECT * FROM users WHERE email = %s" % email)

                if len(verify_data) == 0:
                    nickname = request.json['nickname']
                    password = request.json['password']
                    hash_password = generate_password_hash(password)
                    self.model.execute_query("INSERT INTO users(nickname, email, password) VALUES(%s, %s, %s)" % email, nickname, hash_password)
                    
                    return make_response(jsonify({
                        "message": "The user was created successfully",
                        "statuscode": 201
                    }), 201)

                return make_response(jsonify({
                    "message": "The user's email is alredy in the database",
                    "statuscode": 400
                }), 400)

            except Exception as e:
                
                return make_response(jsonify({
                    "message": "Send me an 'email', 'nickname' and 'password' key's.",
                    "statuscode": 400,
                    "error": f"{e}"
                }), 400)

        return make_response(jsonify({
            "message":"Send me a JSON format.",
            "statuscode":400
        }), 400)