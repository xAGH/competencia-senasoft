from os import getenv
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from src.routes import *
from src.namespaces import *

class Application:

    app: Flask
    socketio: SocketIO

    @classmethod
    def create_app(cls) -> dict[Flask and SocketIO]:
        cls.app = Flask(__name__)
        cls.socketio = SocketIO(cls.app, kwargs={
            "pingTimeout": 30000,
        }, cors_allowed_origins=["http://localhost:4200", "*"], logger=True, engineio_logger=True)
        cls.__settings()
        return {"app": cls.app, "socketio": cls.socketio}

    @classmethod
    def __settings(cls) -> None:
        try:
            cls.__register_namespaces()
            cls.__register_blueprints()
            cls.__register_routes()
            cls.__register_error_handlers()
            cls.app.config.from_mapping(
                SECRET_KEY = getenv("SECRET_KEY")
            )
            CORS(cls.app, resources={
               r"/*": {
                   "origins": ["http://localhost:4200", "*"]
               }
            }, supports_credentials=True)
        except KeyError as ke:
            raise ke
        except Exception as e:
            raise e

    @classmethod
    def __register_namespaces(cls) -> None:
        cls.socketio.on_namespace(RoomNamespace('/room'))

    @classmethod
    def __register_blueprints(cls) -> None:
        pass

    @classmethod
    def __register_routes(cls) -> None:
        cls.app.add_url_rule(users['login'], view_func = users['login_controller'], methods = ["POST"])
        cls.app.add_url_rule(users['signup'], view_func = users['signup_controller'], methods = ["POST"])
        cls.app.add_url_rule(users['auth'], view_func = users['auth_controller'], methods = ["GET"])
        cls.app.add_url_rule(rooms['create_room'], view_func=rooms['rooms_view'], methods=["POST"])
        cls.app.add_url_rule(rooms['room'], view_func=rooms['rooms_view'], methods=['GET'])
        cls.app.add_url_rule(cards['cards'], view_func=cards['cards_controller'])

    @classmethod
    def __register_error_handlers(cls) -> None:
        pass