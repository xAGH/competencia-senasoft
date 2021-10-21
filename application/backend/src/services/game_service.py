from os import getenv

class GameService:

    """
        :param @current_turn — representa el turno actual del jugador.
        :yield @next_turn — genera el siguiente turno apartir del jugador actual.
    """
    @classmethod
    def next_turn(cls, current_turn: int=0):
        total_players: int = int(getenv('ROOMS_LIMIT'))
        for i in range(current_turn, current_turn + total_players):
            yield i % total_players