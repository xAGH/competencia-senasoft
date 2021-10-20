from os import getenv
import random

class RoomsService:

    def generate_room_code(self, characters_quantity: int=5):
        room_code: str = ""
        for i in range(characters_quantity):
            choice: str = random.choice("0123456789ABCDEF")
            room_code += choice
        return room_code