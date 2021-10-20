from flask import request, make_response, jsonify
from flask.views import MethodView
from src.services.users_service import Users

class UsersSignupController(MethodView):

    def __init__(self):
        self.users = Users()

    def post(self):

        if request.is_json:

            try:
                email = request.json['email']
                nickname = request.json['nickname']
                password = request.json['password']                        

                return self.users.signup(email, nickname, password)

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


class UsersLoginController(MethodView):
    def __init__(self):
        self.users = Users()

    def post(self):
        
        if request.is_json:
            
            try:
                email = request.json['email']
                password = request.json['password']

                return self.users.login(email, password)

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

    def __init__(self):
        self.users = Users()

    def get(self, id):
        return self.users.auth_user(id)