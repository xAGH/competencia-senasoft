from flask import request
from flask_socketio import rooms, send, emit, ConnectionRefusedError, join_room, leave_room
from flask_socketio.namespace import Namespace
from src.services.game_service import GameService
from src.services.cards_services import CardsService
from os import getenv

class RoomNamespace(Namespace):

    rooms: dict = {}
    cards_service: CardsService = CardsService(rooms)
    current_turn: int = None

    def on_connect(self):
        try:
            print("Connected", request.sid)
        except ConnectionRefusedError:
            raise ConnectionRefusedError
        except Exception:
            raise Exception   
    
    def on_join(self, data):
        room = data['room']
        if (not room in self.rooms):
            self.emit('room_not_found', {
                "message": f"Room {room} is not available"
            })
            return
        room_players = self.rooms[room]["players"]
        username = f"player_{len(room_players)+1}"
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
                "name":username,
                "sid":request.sid,
                "cards": [],
                "cards_discovered": []
            }
            room_players.append(new_player)
            self.emit("user_joined", {
                "message": "User was joined",
                "users": room_players,
                "you" : new_player
            }, room=room)
            self.send({
                "message": f"User {username} connected in room {room}"
            }, room=room)
        except ConnectionRefusedError as cr:
            raise ConnectionRefusedError
        except Exception as e:
            raise Exception
    
    def on_game_start(self, data):
        room = data['room']
        if len(self.rooms[room]["players"]) == int(getenv("ROOMS_LIMIT")):
            self.rooms[room]["system"]["isGameStarted"] = True
            room_time = self.rooms[room]["system"]["room_time"] = GameService.get_time()
            self.current_turn = self.rooms[room]["players"][0]
            self.emit("game_start", {
                "message": "Game is started",
                "data": self.cards_service.serve_cards(),
                "turn": self.current_turn,
                "time": room_time
            }, room=room)
            return
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
    
    def on_game_in_course(self):
        pass

    def on_make_question(self):
        pass

    def on_throw_accusation(self, data):
        room = data['room']
        accusation  = data['accusation']
        throw_accusation = self.cards_service.accusation(room, accusation['dev_card'], accusation['mod_card'], accusation['error_card'], accusation['player'])
        if throw_accusation:
            self.emit("user_win", {
                "message": "User's accusation win"
            }, room=room)
        gen_turn = GameService.next_turn(self.current_turn)
        self.current_turn = next(gen_turn)
        new_room_time = self.rooms[room]["system"]["room_time"] = GameService.get_time()
        self.emit("game_next_turn", {
            "data": "False accusation",
            "turn": self.current_turn,
            "time": new_room_time
        }, room=room)
    
    def on_game_end(self, data):
        room = data['room']
        self.rooms[room]["system"]["isGameStarted"] = False
        self.rooms.pop(room)
        self.close_room(room)
        self.emit("game_end", {
            "message": "Games end"
        }, room=room)
    
    def on_leave(self, data):
        room = data['room']
        username = data['username']
        self.rooms[room]["players"].index(username)
        self.rooms[room]["players"].remove(username)
        self.leave_room(request.sid, room)
        self.emit("user_leave", {
            "message": f"User {username} left",
            "users": self.rooms[room]["players"]
        }, room=room)
        self.send({
            "message": f"User {username} disconnected from room {room}"
        }, room=room)
    
    def on_disconnect(self):
        print("Disconnected", request.sid)   