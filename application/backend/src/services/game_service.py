from os import getenv
import time
from src.services.provide_names import *
from random import choice

class GameService:

    """
        :param @current_turn — representa el turno actual del jugador.
        :yield @next_turn — genera el siguiente turno apartir del jugador actual.
    """
    @classmethod
    def next_turn(cls, current_turn: int=1):
        total_players: int = int(getenv('ROOMS_LIMIT'))
        for i in range(current_turn, current_turn + total_players):
            yield i % total_players

    """
        :function get_time — obtiene el tiempo actual y lo devuelve como un entero.
    """
    @classmethod
    def get_time(cls):
        return int(time.time())
    
    """
        :function get_elapsed_seconds — devuelve la cantidad de segundos que hay de
        diferencia entre un tiempo y otro dado.
        :param @start_time — representa un tiempo existente.
    """
    @classmethod
    def get_elapsed_seconds(cls, start_time: int):
        return int(time.time()) - start_time

    @classmethod
    def generate_name(cls):
        subject = choice(objects)
        adjective = choice(adjectives)
        number = choice(numbers)
        return f"{adjective}{subject}{number}"