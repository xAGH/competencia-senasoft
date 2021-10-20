from flask import Blueprint

class ApiBlueprint:

    api: Blueprint

    @classmethod
    def create_blueprint(cls):
        cls.api = Blueprint("api", __name__, url_prefix="/api")
        return cls.api
    
    @classmethod
    def __register_routes(cls):
        pass