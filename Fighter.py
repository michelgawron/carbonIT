

class Fighter(object):
    """
    This class defines our game's fighters

    Methods:
        - request_move(move: str) -> None:
            Function that is going to handle our moves requests
    """

    def __init__(self, moves, name, game):
        """
        Our fighters' constructor
        We need a reference to the game's map to request our moves
        :param moves: List of moves that the fighter should make
        :param name: Fighter's name
        :param game: Our map - we named it game in order not to override map function
        """
        self.__moves = moves
        self.__name = name
        self.__game = game

    def request_move(self, move: str):
        """
        Function that is going to handle our moves requests
        Coding it that way allows us to thread it if needed later
        In order to do so we would just have to add a mutex to the map object
        :param move: Move requested
        :return:
        """