from flask import request, make_response, jsonify
from flask.helpers import get_env
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from datetime import datetime, timedelta
from src.models import Model
from src.services.email_services import Email
from os import getenv


class Users():

    def __init__(self):
        self.model = Model()
        self.email = Email()
        self.secret_jwt = getenv("JWT_SECRET_KEY")

    def signup(self, email, nickname, password):
        verify_email = self.model.fetch_one(f"SELECT email FROM users WHERE email = '{email}'")

        if verify_email is None or len(verify_email) == 0:
            hash_password =  generate_password_hash(password)
            self.model.execute_query(f"INSERT INTO users(nickname, email, password) VALUES('{nickname}', '{email}', '{hash_password}')")
            id_user = self.model.fetch_one("SELECT id FROM users ORDER BY id DESC")[0]
            auth_token = jwt.encode({
                "id": id_user
            }, self.secret_jwt, "HS256")
            self.email.confirmation_email(email, nickname, auth_token)
            return make_response(jsonify({
                "message": "The user was created successfully",
                "statuscode": 201
            }), 201)

        return make_response(jsonify({
            "message": "The user's email alredy exists in the database.",
            "statuscode": 400
        }), 400)

    def login(self, email, password):
        user_data = self.model.fetch_one(f"SELECT * FROM users WHERE email = '{email}'")

        if user_data is None or len(user_data) == 0:
            
            return make_response(jsonify({
                "message": "The user don't exists in the database.",
                "statuscode": 400
            }), 400)

        if check_password_hash(user_data[3], password):
                token = jwt.encode({
                    "sub": user_data[0],
                    "email": email,
                    "nickname": user_data[1],
                    "exp": datetime.utcnow() + timedelta(minutes=60)
                }, self.secret_jwt, "HS256")

                response = make_response(jsonify({
                    "message": f"User with nickname {user_data[1]} is now login.",
                    "statuscode":200,
                    "confirmedaccount": user_data[4],
                    "token": token
                }), 200)

                response.headers["Authorization"] = token

                return response

        return make_response(jsonify({
            "message":"Wrong credentials.",
            "statuscode": 400
        }), 400)\

    def auth_user(self, token):
        try: 
            user_id = jwt.decode(token,self.secret_jwt, "HS256").get("id")
            self.model.execute_query(f"UPDATE users SET is_confirmed = 1 WHERE id = {user_id}")

            return make_response(jsonify({
                "message": "User's email confirmed successfuly.",
                "statudcode": 200
            }), 200)

        except Exception as e:
            return make_response(jsonify({
                "message": "The token is invalid.",
                "statuscode": 400,
                "error": f"{e}"
            }))