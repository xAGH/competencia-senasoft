from os import error
from flask import json, make_response, jsonify
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

    def question(self, sid, user_id, dev_card, mod_card, error_card):
        data = {
  "hidden_cards": [
    {
      "card_name": "Juanita",
      "category_name": "developer",
      "id": 4
    },
    {
      "card_name": "Comprobante Contable",
      "category_name": "module",
      "id": 11
    },
    {
      "card_name": "Null pointer",
      "category_name": "error",
      "id": 17
    }
  ],
  "players":{
      "player1_cards": [
          1,
    {
      "card_name": "Recibos",
      "category_name": "module",
      "id": 10
    },
    {
      "card_name": "Contabilidad",
      "category_name": "module",
      "id": 13
    },
    {
      "card_name": "404",
      "category_name": "error",
      "id": 14
    },
    {
      "card_name": "Stack Overflow",
      "category_name": "error",
      "id": 15
    }
  ],
  "player2_cards": [2, 
    {
      "card_name": "Encoding error",
      "category_name": "error",
      "id": 19
    },
    {
      "card_name": "Syntax error",
      "category_name": "error",
      "id": 18
    },
    {
      "card_name": "Facturación",
      "category_name": "module",
      "id": 9
    },
    {
      "card_name": "Usuarios",
      "category_name": "module",
      "id": 12
    }
  ],
  "player3_cards": [3, 
    {
      "card_name": "Pedro",
      "category_name": "developer",
      "id": 1
    },
    {
      "card_name": "Antonio",
      "category_name": "developer",
      "id": 5
    },
    {
      "card_name": "Juan",
      "category_name": "developer",
      "id": 2
    },
    {
      "card_name": "Carolina",
      "category_name": "developer",
      "id": 6
    }
  ],
  "player4_cards": [4, 
    {
      "card_name": "Manuel",
      "category_name": "developer",
      "id": 7
    },
    {
      "card_name": "Memory out of range",
      "category_name": "error",
      "id": 16
    },
    {
      "card_name": "Carlos",
      "category_name": "developer",
      "id": 3
    },
    {
      "card_name": "Nómina",
      "category_name": "module",
      "id": 8
    }
  ]
  }
}
        answers = []
        count = 0
        
        for i in data["players"]:
            for j in range(1, len(data["players"][i])):
                if data["players"][i][j]["id"] == dev_card:
                    answers.append({
                        "player": data["players"][i][0],
                        "dev_card": dev_card
                    })
                    count += 1

                if data["players"][i][j]["id"] == mod_card:
                    answers.append({
                        "player": data["players"][i][0],
                        "mod_card": mod_card
                    })
                    count += 1

                if data["players"][i][j]["id"] == error_card:
                    answers.append({
                        "player": data["players"][i][0],
                        "error_card": error_card
                    })
                    count += 1
        return make_response(jsonify({
            "answers": answers
        }))