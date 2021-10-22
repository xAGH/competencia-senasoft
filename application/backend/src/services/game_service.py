from os import getenv
from random import choice
from src.services.provide_names import *
from random import choice
import time

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
    
    @classmethod
    def create_turn(cls, current_turn: int=0):
        turns: list = []
        total_players: int = int(getenv('ROOMS_LIMIT'))
        for i in range(current_turn, current_turn + total_players):
            new_turn = i % total_players
            turns.append(new_turn)
        return turns

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
    def create_random_name(cls):
        adjetives = ["Gordo", "Feo", "Panzón", "MalProgramador"]
        subjects = ["Llanta", "Gato", "Ñero", "Virgen", "Nea"]
        adjetive = choice(adjetives)
        subject = choice(subjects)
        number = choice(range(1,255))
        random_name = "{0}{1}{2}".format(adjetive, subject, number)
        return random_name

    @classmethod
    def generate_name(cls):
        subject = choice(objects)
        adjective = choice(adjectives)
        number = choice(numbers)
        return f"{adjective}{subject}{number}"