# Importación de librerías.
from flask import request, make_response, jsonify, Response
from flask.views import MethodView
from src.services.users_service import Users

# Este archivo contiene los controladores para los usuarios.

class UsersSignupController(MethodView):

    """Clase que controla el registro de los usuarios."""

    def __init__(self: object) -> None:
        """
        Método constructor.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
            |- Retorno -> None.
            |- Función -> Instancia un objeto de la clase User para proveer los servicios.
        """
        self.users: object = Users()

    def post(self) -> Response:
        """
        Método post.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
            |- Retorno -> Response.
            |- Función -> Valida y verifica los datos que reciba como JSON y método HTTP -> POST para enviarlos al servicio de registro de usuarios.
        """
        if request.is_json:

            try:
                email: str = request.json['email']
                nickname: str = request.json['nickname']
                password: str = request.json['password']                        

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

    """Clase que controla el login de los usuarios."""

    def __init__(self: object) -> None:
        """
        Método constructor.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
            |- Retorno -> None.
            |- Función -> Instancia un objeto de la clase User para proveer los servicios.
        """
        self.users: object = Users()

    def post(self: object) -> Response:
        """
        Método post.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
            |- Retorno -> Response.
            |- Función -> Valida y verifica los datos que reciba como JSON y método HTTP -> POST para enviarlos al servicio de login de usuarios.
        """
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

    """Clase que controla la autenticación de usuarios."""

    def __init__(self: object) -> None:
        """
        Método constructor.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
            |- Retorno -> None.
            |- Función -> Instancia un objeto de la clase User para proveer los servicios.
        """
        self.users: object = Users()

    def get(self: object, uid: int) -> Response:
        """
        Método get.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             uid: int => Id del usuario pasado como parámetro en ruta.
            |- Retorno -> Response.
            |- Función -> Atiende a un método HTTP -> GET obteniendo un uid como parametro en ruta y se lo transmite al servicio de
                          autenticación de usuarios.
        """
        return self.users.auth_user(uid)
