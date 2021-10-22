from flask import make_response, jsonify, Response
from src.models import Model
from random import randint

class CardsService():
    
    """Clase para proveer servicios en cuanto a acciones del juego."""

    def __init__(self: object, rooms) -> None:
        """
        Método constructor.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
            |- Retorno -> None;
            |- Función -> Inicia una instancia de la clase de Model() para operaciones en base de datos, además, 
                          crea una referencia del diccionario rooms en la clase RoomNamespace.
        """
        self.model: object = Model()
        self.rooms = rooms

    def get_cards(self:object) -> tuple:

        """
        Método obtener cartas.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
            |- Retorno -> Tuple(list, list, list) o recibido en tres variables => var1: list, var2: list, var3: list = get_cards()
            |- Función -> Consulta las cartas en la base de datos según su categoria (developer, module, error)
        """

        developers_cards: list = self.model.fetch_all("SELECT c.id, ca.name AS category_name, c.name as card_name FROM cards c, categories ca WHERE ca.id = c.category AND category = 1", as_dict=True)
        modules_cards: list = self.model.fetch_all("SELECT c.id, ca.name AS category_name, c.name as card_name FROM cards c, categories ca WHERE ca.id = c.category AND category = 2", as_dict=True)
        errors_cards: list = self.model.fetch_all("SELECT c.id, ca.name AS category_name, c.name as card_name FROM cards c, categories ca WHERE ca.id = c.category AND category = 3", as_dict=True)
        print(developers_cards, modules_cards, errors_cards)
        return developers_cards, modules_cards, errors_cards

    def delete_seleted_cards(self: object, cards: list, selected_card: dict) -> list:
        """
        Método eliminar cartas seleccionadas.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             cards: list => Cartas disponibles.
                             selected_card: dict => Carta seleccionada, pendiente para ser eliminada en la lista de cartas.
            |- Retorno -> list => Lista de cartas con las seleccionadas ya eliminadas.
            |- Función -> Elimina de una lista de cartas una carta ya seleccionada
        """
        for i in range(len(cards)):
            if cards[i]["id"] == selected_card["id"]:
                cards.pop(i)
                return cards

    def select_players_cards(self: object, cards: list, player: int, room: str) -> tuple:
        """
        Método seleccionar cartas de jugadores.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             cards: list => Cartas disponibles para los jugadores.
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
            
        return player_cards, cards

    def serve_cards(self:object, room: str) -> Response:
        """
        Metodo repartir cartas.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             room: str => Código de la sala.
            |- Retorno -> Response => Respuesta enviada en formato json.
            |- Función -> Reparte las a de los jugadores y separa las que quedarán ocultas. Ambas quedan guardadas en el diccionario raiz de rooms..
        """
        developers, modules, errors = self.get_cards()
        hidden_developer: dict= developers[randint(0, len(developers) - 1)]
        hidden_module: dict = modules[randint(0, len(modules) - 1)]
        hidden_error: dict = errors[randint(0, len(errors) - 1)]
        hidden_cards: list = [hidden_developer, hidden_module, hidden_error]
        self.add_hidden_cards_to_room(hidden_cards, room)
        available_developers: list = self.delete_seleted_cards(developers, hidden_developer)
        available_modules: list = self.delete_seleted_cards(modules, hidden_module)
        available_errors: list = self.delete_seleted_cards(errors, hidden_error)
        cards: list = available_developers + available_modules + available_errors
        player1, cards = self.select_players_cards(cards, 0, room)
        player2, cards = self.select_players_cards(cards, 1, room)
        player3, cards = self.select_players_cards(cards, 2, room)
        player4, cards = self.select_players_cards(cards, 3, room)
        return {
            "hidden_cards": hidden_cards,
            "player_cards": [player1, player2, player3, player4]
        }

    def add_hidden_cards_to_room(self: object, cards: dict, room: str) -> None:
        """
        Método añadir cartas ocultas a la sala.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             cards: dict => Cartas elegidas como ocultas. 
                             room: str => Codigo de la sala.
            |- Retorno -> None.
            |- Función -> Añade las cartas seleccionadas como ocultas al diccionario de la sala.
        """
        cards_id: list = []
        for card in cards:
            cards_id.append(card["id"])
        self.rooms[room]["system"]["hidden_cards"] = cards_id

    def question(self: object, dev_card: int, mod_card: int, error_card: int, room: str) -> Response:
        """
        Método de pregunta.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             dev_card: int => Id de una carta de desarrollador.
                             mod_card: int => Id de una carta de módulo.
                             error_card: int => Id de una carta de error.
                             room: str -> Código de la sala.
            |- Retorno -> Response => Respuesta enviada en formato json.
            |- Función -> Verifica si las cartas con las que ha hecho la pregunta un usuario, las tiene otro jugador.
            
        """
        answers: list = []

        players: dict = self.rooms[room]["players"]

        # Se recorre la lista que devuelve la llave del diccionario players en la llave "players"
        for i in players:
            # Cada iteración de i devuelve una estructura similar a la siguiente:
            # {
            #     "cards":[4, 8, 5, 9],
            #     "discovered_cards": [1, 6, 10, 11, 12, 15],
            #     "score": 1/12 * 100,
            #     "nickname": "Nickname"
            #     "conected": True
            # }
            # Se itera sobre la estructura anterior en la llave de "cards"
            for j in range(len(i["cards"])):
                # Cada iteración de j devuelve una estructura como la siguiente:
                    # [4, 8, 5, 9]

                # Se comprueba si i en la llave "cards" y posición j es igual a alguna de las 3 cartas
                # que entran como parámetro. Dado que el resultado de lo anterior sea verdadero, se agrega 
                # a la lista un diccionario con una clave player_index igual al indice del jugador que tiene la carta
                # y una llave x_card igual a la carta que tiene dicho jugador.
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
    
    def save_discovered_cards(self: object, room: str, player_index: int, *args: int) -> Response:
        """
        Método guardar cartas descubiertas.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             room: str => Código de la sala.
                             player_index: int => Índice del jugador.
                             *args: int => N argumentos adicionales que corresponden a las cartas a guardar.
            |- Retorno -> Response => Respuesta enviada en formato json.
            |- Función -> Guarda las cartas enviadas por parámetros en la lista de cartas descubiertas del jugador correspondiente.
        """
        for i in range(len(args)):
            self.rooms[room]["players"][player_index]["cards_discovered"].append(args[i])
        
        return {
            "message": "User discovered cars append in his list."
        }

    def accusation(self: object, room: str, dev_card: int, mod_card: int, error_card: int, player: int) -> Response:
        """
        Método acusación.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             room: str -> Código de la sala. 
                             dev_card: int => Id de una carta de desarrollador.
                             mod_card: int => Id de una carta de módulo.
                             error_card: int => Id de una carta de error.
                             player: int => Id o índice del jugador que ha hecho la acusación.
            |- Retorno -> True o False dependiendo de la validaciónTrue o False dependiendo de la validación
            |- Función -> Verifica las cartas ocultas definidas al inicio de la partida y las compara con las entregadas en los parámetros.
                          Si son iguales, el jugador gana, de lo contrario, pasa el turno.
        """
        hidden_cards: list = self.rooms[room]["system"]["hidden"]
        accusation_player_cards: list = [dev_card, mod_card, error_card]

        if hidden_cards == accusation_player_cards:
            return True

        return False
