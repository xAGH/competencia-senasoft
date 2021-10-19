from os import _OnError
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

class Application:

    app: Flask
    socketio: SocketIO

    @classmethod
    def create_app(cls) -> dict[Flask and SocketIO]:
        pass

    @classmethod
    def __settings(cls) -> None:
        pass

    @classmethod
    def __register_namespaces(cls) -> None:
        pass

    @classmethod
    def __register_blueprints(cls) -> None:
        pass

    @classmethod
    def __register_routes(cls) -> None:
        pass

    @classmethod
    def __register_error_handlers(cls) -> None:
        pass