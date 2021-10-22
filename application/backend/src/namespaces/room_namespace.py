import re
from flask import request
from flask_socketio import ConnectionRefusedError
from flask_socketio.namespace import Namespace
from src.services.game_service import GameService
from src.services.cards_services import CardsService
from os import getenv

class RoomNamespace(Namespace):

    rooms: dict = {}
    cards_service: CardsService = CardsService(rooms)
    current_turn: int = None
    question_turn_player : int = None
    question_mode = True
    question_cards = []

    def on_connect(self):
        try:
            print("Connected", request.sid)
        except ConnectionRefusedError:
            raise ConnectionRefusedError
        except Exception:
            raise Exception   
    
    def on_message(self, data):
        room = data['room']
        message = data['message']
        player = data['player']
        self.send({
            "message": message,
            "player": player,
            "system_message": False
        }, room=room)

    def on_join(self, data):
        room = data['room']
        if (not room in self.rooms):
            self.emit('room_not_found', {
                "message": f"Room {room} is not available"
            })
            return
        room_players = self.rooms[room]["players"]
        username = GameService.generate_name()
        try:
            if len(room_players) >= int(getenv('ROOMS_LIMIT')):
                self.emit("room_full", {
                    "message": "Room is full"
                })
                return
            match = [player for player in room_players if request.sid == player["sid"]]
            if len(match) > 0:
                username = match[0]["name"]
                self.emit("user_is_on_room", {
                    "messsage": f"El usuario {username} ya se encuentra en sala"
                })
                return
            self.enter_room(request.sid, room=room)
            new_player = {
                "name": username,
                "sid": request.sid,
                "cards": [],
                "discovered_cards": [],
                "connected": True
            }
            room_players.append(new_player)
            self.rooms[room]["system"] = {
                "hidden_cards": [],
                "isGameStarted": None
            }
            self.emit("user_joined", {
                "message": "User was joined",
                "users": room_players,
                "you" : new_player
            }, room=room)
            self.send({
                "message": f"User {username} joined in room {room}",
                "system_message": True
            }, room=room)
        except ConnectionRefusedError as cr:
            raise ConnectionRefusedError
        except Exception as e:
            raise Exception
    
    def on_request_room_info(self, data):
        room = data['room']
        players = self.rooms[room]["players"]
        self.emit("get_room_info", {
            "message": "Room information",
            "players": players,
        }, room=room)
    
    def on_game_start(self, data):
        room = data['room']
        if len(self.rooms[room]["players"]) == int(getenv("ROOMS_LIMIT")):
            self.rooms[room]["system"]["isGameStarted"] = True
            room_time = self.rooms[room]["system"]["room_time"] = GameService.get_time()
            selected_id = None
            for i in range(len(self.rooms[room]["players"])):
                player = self.rooms[room]["players"][i]
                if player["connected"]:
                    selected_id = i
                    break
            self.current_turn = selected_id
            self.rooms[room]["system"]["current_turn"] = selected_id
            self.emit("game_start", {
                "message": "Game is started",
                "data": self.cards_service.serve_cards(room),
                "players_ids": [player["sid"] for player in self.rooms[room]["players"]],
                "first_turn": self.current_turn,
                "time": room_time
            }, room=room)
            self.send({
                "message": "Starting game...",
                "system_message": True
            }, room=room)
            return
        self.rooms[room]["system"]["isGameStarted"] = False
        self.emit("game_waiting", {
            "message": "Waiting for players"
        }, room=room)
    
    def on_timeout(self, data):
        room = data['room']
        total_time = GameService.get_elapsed_seconds(self.rooms[room]["system"]["room_time"])
        if (total_time >= int(getenv('TIME_LIMIT'))):
            gen_turn = GameService.next_turn(self.current_turn)
            self.current_turn = next(gen_turn)
            new_room_time = self.rooms[room]["system"]["room_time"] = GameService.get_time()
            self.emit("game_next_turn", {
                "message": "The next game turn",
                "turn": self.current_turn,
                "time": new_room_time
            }, room=room)
    
    def on_game_round(self, data):
        room = data['room']
        selected_option = data['option']
        turn = data['turn']
        current_turn = self.rooms[room]["system"]["current_turn"]
        if(current_turn == turn):
            if (selected_option == 0): # question
                self.on_make_question({
                    "room": room
                })
                pass
            elif (selected_option == 1): # accusation
                self.on_throw_accusation({
                    "room": room
                })
                pass
            else: # No option passed
                pass
        else:
            self.on_change_turn({ # Change turn
                "room": room,
                "current_turn": current_turn
            })
    
    def on_discovered_cards(self, data):
        room = data['room']
        cards = data['cards']
        player = data['player']
        players = [player for player in self.rooms[room]["players"]]
        player_index = players["sid"].index(player)
        if player_index is None: 
            return # Not player index found
        discovered_cards = self.cards_service.save_discovered_cards(room, player_index, (cards))
        self.emit("discovered_cards", {
            "message": discovered_cards
        }, room=room)

    """
        :function - Toma el turno actual declarado al iniciar el juego y apartir de este, genera un turno adelante, para
        asi dar continuidad al siguiente usuario.
    """
    def on_change_turn(self, data):
        room = data['room']
        turn = data['current_turn']
        current_turn = self.rooms[room]["system"]["current_turn"] = turn
        new_turn = GameService.create_turn(current_turn)
        self.emit("turn_changed", {
            "message": "Next user",
            "new_turn": new_turn[0]
        }, room=room)

    """
        :method @on_make_question —  se encarga de llamar al servicio de crear una nueva pregunta
    """
    def on_make_question(self, data):
        room = data['room']
        player = data['player']
        created_question = self.cards_service.question(data['dev_card'], data['mod_card'], data['error_card'], data['room'])
        self.emit("new_question", {
            "system_answer": created_question
        }, room=room)
        self.send({
            "message": f"New question created by {player}",
            "system_message": True
        }, room=room)

    def on_throw_accusation(self, data):
        room = data['room']
        accusation  = data['accusation']
        throw_accusation = self.cards_service.accusation(room, accusation['dev_card'], accusation['mod_card'], accusation['error_card'], accusation['player'])
        if throw_accusation:
            self.emit("user_win", {
                "message": "User's accusation win"
            }, room=room)
            return
        current_turn = self.rooms[room]["system"]["current_turn"]
        new_turn = GameService.create_turn(current_turn)
        new_room_time = self.rooms[room]["system"]["room_time"] = GameService.get_time()
        self.emit("game_next_turn", {
            "data": "False accusation",
            "turn": new_turn,
            "time": new_room_time
        }, room=room)
    
    def on_game_end(self, data):
        room = data['room']
        self.rooms[room]["system"]["isGameStarted"] = False
        players = self.rooms[room]["players"]
        for i in range(players):
            self.leave_room(players["sid"], room=room)
        self.rooms.pop(room)
        self.close_room(room)
        self.emit("game_end", {
            "message": "Games end",
            "winner": ""
        }, room=room)
    
    def on_leave(self, data):
        room = data['room']
        username = data['username']
        players = self.rooms[room]["players"]
        found = [player for player in players if player["name"] == username]
        if len(found) == 0: return # Jugador no encontrado
        player = found[0]
        players.remove(player)
        self.leave_room(player["sid"], room)
        self.emit("user_leave", {
            "message": f"User {username} left",
            "users": self.rooms[room]["players"]
        }, room=room)
        self.send({
            "message": f"User {username} disconnected from room {room}",
            "system_message": True
        }, room=room)

    def on_disconnect(self):
        self.emit("user_disconnected")
    
    def on_request_disconnection(self, data):
        print("Disconnected", request.sid)
        room = data['room']
        match = [player for player in self.rooms[room]["players"] if player["sid"] == request.sid]
        if len(match) == 0: return
        self.on_leave({
            "room": room,
            "username": match[0]
        })