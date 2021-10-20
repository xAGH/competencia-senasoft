from os import getenv
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from src.routes import users, public
from src.namespaces import *

class Application:

    app: Flask
    socketio: SocketIO

    @classmethod
    def create_app(cls) -> dict[Flask and SocketIO]:
        cls.app = Flask(__name__)
        cls.socketio = SocketIO(cls.app)
        cls.__settings()
        return {"app": cls.app, "socketio": cls.socketio}

    @classmethod
    def __settings(cls) -> None:
        try:
            cls.__register_routes()
            cls.app.config.from_mapping(
                SECRET_KEY = getenv("SECRET_KEY")
            )
        except Exception as e:
            pass

    @classmethod
    def __register_namespaces(cls) -> None:
        cls.socketio.on_namespace(RoomNamespace('/room'))

    @classmethod
    def __register_blueprints(cls) -> None:
        pass

    @classmethod
    def __register_routes(cls) -> None:
        cls.app.add_url_rule(users['signin'], view_func = users['signin_controller'], methods = ["POST"])
        cls.app.add_url_rule(users['signup'], view_func = users['signup_controller'], methods = ["POST"])

    @classmethod
    def __register_error_handlers(cls) -> None:
        pass