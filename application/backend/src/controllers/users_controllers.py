from flask import request, make_response, jsonify
from flask.views import MethodView
from src.models import Model
from werkzeug.security import generate_password_hash, check_password_hash
from src.services.users_service import Users

class UsersSigninController(MethodView):

    def __init__(self):
        self.model = Model()
        self.users = Users()

    def post(self):

        if request.is_json:

            try:
                email = request.json['email']
                nickname = request.json['nickname']
                password = request.json['password']                        

                return self.users.signin(email, nickname, password)

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


class UsersSignupController(MethodView):
    def __init__(self):
        self.model = Model()
        self.users = Users()

    def post(self):
        
        if request.is_json:
            
            try:
                email = request.json['email']
                password = request.json['password']

                return self.users.signup(email, password)

            except Exception as e:
                return make_response(jsonify({
                    "message": "Send me an 'email' and a 'password' key's.",
                    "statuscode": 400,
                    "error": f"{e}"
                }), 400)
                
        return make_response(jsonify({
            "message":"Send me a JSON format.",
            "statuscode":400
        }), 400)

class UsersAuthController(MethodView):
    pass