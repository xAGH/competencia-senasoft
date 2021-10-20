from os import error
from flask import make_response, jsonify
from pymysql import err
from src.models import Model
from random import randint

class Cards():
    
    def __init__(self):
        self.model = Model()

    def get_cards(self):
        developers_cards = self.model.fetch_all("SELECT c.id, ca.name AS category_name, c.name as card_name FROM cards c, categories ca WHERE ca.id = c.category AND category = 1", as_dict=True)
        modules_cards = self.model.fetch_all("SELECT c.id, ca.name AS category_name, c.name as card_name FROM cards c, categories ca WHERE ca.id = c.category AND category = 2", as_dict=True)
        errors_cards = self.model.fetch_all("SELECT c.id, ca.name AS category_name, c.name as card_name FROM cards c, categories ca WHERE ca.id = c.category AND category = 3", as_dict=True)
        return developers_cards, modules_cards, errors_cards

    def delete_seleted_cards(self, cards, selected_card):
        for i in range(len(cards)):
            if cards[i]["id"] == selected_card["id"]:
                cards.pop(i)
                return cards

    def select_players_cards(self, cards):
        player_cards = []
        for i in range(4):
            rand = randint(0, len(cards) - 1)
            player_cards.append(cards.pop(rand))
        return player_cards, cards

    def serve_cards(self):
        developers, modules, errors = self.get_cards()
        hidden_developer = developers[randint(0, len(developers) - 1)]
        hidden_module = modules[randint(0, len(modules) - 1)]
        hidden_error = errors[randint(0, len(errors) - 1)]
        hidden_cards = [hidden_developer, hidden_module, hidden_error]
        available_developers = self.delete_seleted_cards(developers, hidden_developer)
        available_modules = self.delete_seleted_cards(modules, hidden_module)
        available_errors = self.delete_seleted_cards(errors, hidden_error)
        cards = available_developers + available_modules + available_errors
        player1, cards = self.select_players_cards(cards)
        player2, cards = self.select_players_cards(cards)
        player3, cards = self.select_players_cards(cards)
        player4, cards = self.select_players_cards(cards)
        return make_response(jsonify({
            "hidden_cards": hidden_cards,
            "player1_cards": player1,
            "player2_cards": player2,
            "player3_cards": player3,
            "player4_cards": player4,
        }))