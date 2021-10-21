from flask import request, make_response, jsonify
from flask.views import MethodView
from src.models import Model
from src.services.cards_services import CardsService

class CardsController(MethodView):

    def __init__(self):
        self.cards = CardsService()

    def get(self):
        return self.cards.serve_cards("a")

    def post(self):
        user_id = request.json["user_id"]
        dev_card = request.json["dev_card"]
        mod_card = request.json["mod_card"]
        error_card = request.json["error_card"]
        room = request.json["room"]
        
        return self.cards.accusation(room, dev_card, mod_card, error_card, user_id)