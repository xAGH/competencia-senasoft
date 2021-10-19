from flask import request, make_response, jsonify
from flask.views import MethodView

class IndexController(MethodView):

    def __init__(self) -> None:
        pass

    def get(self):
        pass