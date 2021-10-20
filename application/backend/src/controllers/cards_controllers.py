from flask import request, make_response, jsonify
from flask.views import MethodView
from src.models import Model
from src.services.cards_services import Cards

class CardsController(MethodView):

    def __init__(self):
        self.cards = Cards()

    def get(self):
        return self.cards.serve_cards()