from flask import request, make_response, jsonify
from flask.views import MethodView
from src.models import Model
from werkzeug.security import generate_password_hash, check_password_hash

class UsersSigninController(MethodView):

    def __init__(self):
        self.model = Model()

    def post(self):

        if request.is_json:

            try:
                email = request.json['email']
                verify_email = self.model.fetch_one(f"SELECT email FROM users WHERE email = '{email}'")

                if verify_email is None or len(verify_email) == 0:
                    nickname = request.json['nickname']
                    password = request.json['password']
                    hash_password = generate_password_hash(password)
                    self.model.execute_query(f"INSERT INTO users(nickname, email, password) VALUES('{nickname}', '{email}', '{hash_password}')")
                    
                    return make_response(jsonify({
                        "message": "The user was created successfully",
                        "statuscode": 201
                    }), 201)

                return make_response(jsonify({
                    "message": "The user's email is alredy in the database",
                    "statuscode": 400
                }), 400)

            except Exception as e:
                raise e
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

    def post(self):
        
        if request.is_json:
            
            try:
                email = request.json['email']
                password = request.json['password']
                verify_data = self.model.fetch_one("SELECT * FROM users WHERE email = %s" % email)

                if len(verify_data) != 0:
                    verify_password = check_password_hash(verify_data[1])

            except:
                pass
                

class UsersAuthController(MethodView):
    pass