from flask import make_response, jsonify
from src.models import Model
from random import randint
from src.namespaces.room_namespace import RoomNamespace

class Cards():
    
    """Clase para proveer servicios en cuanto a acciones de las cartas."""

    def __init__(self) -> None:
        """
        Método constructor.
            |- Retorno -> None;
            |- Función -> Inicia una instancia de la clase de Model() para operaciones en base de datos, además, 
                          crea una referencia del diccionario rooms en la clase RoomNamespace.
        """
        self.model = Model()
        self.rooms = RoomNamespace.rooms

    def get_cards(self) -> tuple:

        """
        Método obtener cartas.
            |- Retorno -> Tuple(list, list, list) o recibido en tres variables => var1: list, var2: list, var3: list = get_cards()
            |- Función -> Consulta las cartas en la base de datos según su categoria (developer, module, error)
        """

        developers_cards: list = self.model.fetch_all("SELECT c.id, ca.name AS category_name, c.name as card_name FROM cards c, categories ca WHERE ca.id = c.category AND category = 1", as_dict=True)
        modules_cards: list = self.model.fetch_all("SELECT c.id, ca.name AS category_name, c.name as card_name FROM cards c, categories ca WHERE ca.id = c.category AND category = 2", as_dict=True)
        errors_cards: list = self.model.fetch_all("SELECT c.id, ca.name AS category_name, c.name as card_name FROM cards c, categories ca WHERE ca.id = c.category AND category = 3", as_dict=True)
        return developers_cards, modules_cards, errors_cards

    def delete_seleted_cards(self, cards: list, selected_card: dict) -> list:
        """
        Método eliminar cartas seleccionadas.
            |- Retorno -> list => Lista de cartas con las seleccionadas ya eliminadas.
            |- Parámetros -> cards: list => Cartas disponibles.
                             selected_card: dict => Carta seleccionada, pendiente para ser eliminada en la lista de cartas.
            |- Función -> Elimina de una lista de cartas una carta ya seleccionada
        """
        for i in range(len(cards)):
            if cards[i]["id"] == selected_card["id"]:
                cards.pop(i)
                return cards

    def select_players_cards(self, cards: list, player: int, room: str) -> tuple:
        """
        Método seleccionar cartas de jugadores.
            |- Parámetros -> cards: list => Cartas disponibles para los jugadores.
                             player: int => Posición u orden del jugador.
                             room: str => Código de la sala.
            |- Retorno -> Tuple(list, list) o recibido en dos variables => var1: list, var2: list = select_players_cards(cards)
            |- Función -> Consulta las cartas en la base de datos según su categoria (developer, module, error)
        """
        player_cards: list = []
        for i in range(4):
            rand: int= randint(0, len(cards) - 1)
            new_card: dict = cards.pop(rand)
            player_cards.append(new_card)
            self.rooms[room]["players"][player]["cards"].append(new_card["id"])
        return player_cards, cards

    def serve_cards(self, room: str) -> make_response:
        """
        Metodo servir cartas.
            |- Parámetros -> room: str => Código de la sala.
            |- Retorno -> make_response => Respuesta enviada en formato json.
            |- Función -> Divide las cartas en las ocultas y la de los jugadores.
        """
        developers, modules, errors = self.get_cards()
        hidden_developer = developers[randint(0, len(developers) - 1)]
        hidden_module = modules[randint(0, len(modules) - 1)]
        hidden_error = errors[randint(0, len(errors) - 1)]
        hidden_cards = [hidden_developer, hidden_module, hidden_error]
        available_developers = self.delete_seleted_cards(developers, hidden_developer)
        available_modules = self.delete_seleted_cards(modules, hidden_module)
        available_errors = self.delete_seleted_cards(errors, hidden_error)
        cards = available_developers + available_modules + available_errors
        player1, cards = self.select_players_cards(cards, 0, room)
        player2, cards = self.select_players_cards(cards, 1, room)
        player3, cards = self.select_players_cards(cards, 2, room)
        player4, cards = self.select_players_cards(cards, 3, room)
        return make_response(jsonify({
            "hidden_cards": hidden_cards,
            "player1_cards": player1,
            "player2_cards": player2,
            "player3_cards": player3,
            "player4_cards": player4,
        }))

    def question(self, dev_card, mod_card, error_card, room):
        answers = []

        players = self.rooms[room]["players"]

        for i in players:

            for j in range(len(i["cards"])):
                
                if i["cards"][j] == dev_card:
                    answers.append({
                        "player_index": players.index(i),
                        "dev_card": dev_card
                    })

                if i["cards"][j] == mod_card:
                    answers.append({
                        "player_index": players.index(i),
                        "mod_card": mod_card
                    })

                if i["cards"][j] == error_card:
                    answers.append({
                        "player_index": players.index(i),
                        "error_card": error_card
                    })
        
        return make_response(jsonify({
            "answers": answers
        }))
    
    def save_discover_cards(self, room, player_index, *args):
        for i in range(len(args)):
            self.rooms[room]["players"][player_index]["cards_discovered"].append(args[i])
        
        return make_response(jsonify({
            "message": "User discovered cars append in his list.",
            "statuscode":200
        }), 200)

    def accusation(self, room, dev_card, mod_card, error_card, player):

        hidden_cards = self.rooms[room]["system"]["hidden"]
        accusation_player_cards = [dev_card, mod_card, error_card]

        if hidden_cards == accusation_player_cards:
            return make_response(jsonify({
                "win": True,
                "player":  player
            }))

        return make_response(jsonify({
            "win": False,
            "player":  player
        }))