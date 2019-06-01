import Map
from OrientationEnum import OrientationEnum


class Fighter(object):
    """
    This class defines our game's fighters

    Methods:
        - request_move(move: str) -> None:
            Function that is going to handle our moves requests
        - consume_move(None) -> None:
            Function that is going to pop moves from our list and request them on the game board
    """

    def __init__(self, moves: list, name: str, game: Map, pos_x: int, pos_y: int, orientation: OrientationEnum,
                 treasure=0) -> None:
        """
        Our fighters' constructor
        We need a reference to the game's map to request our moves
        :param moves: List of moves that the fighter should make
        :param name: Fighter's name
        :param game: Our map - we named it game in order not to override map function
        :param pos_x: Position x of the fighter
        :param pos_y: Position y of the fighter
        :param orientation: String representing the orientation of the fighter
        :param treasure: Number of treasures that our fighter has - default: 0
        """
        self.__moves = list(moves)
        self.__name = name
        self.__game = game
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        if orientation not in ['N', 'S', 'E', 'W']:
            raise ValueError(f"Wrong orientation: expected: {['N', 'S', 'E', 'W']} got {orientation}")
        else:
            # Getting the orientation value from the enumeration
            self.__orientation = OrientationEnum[orientation]
            print(self.__orientation)
        self.__treasure = treasure

    def __str__(self):
        """
        Our fighter's string is going to be the first letter of its name
        :return:
        """
        return self.name[0]

    @property
    def name(self):
        return self.__name

    @property
    def pos_x(self):
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, value: int):
        if self.game.width > value >= 0:
            self.__pos_x = value
        else:
            raise IndexError(f"Trying to place the player out of bounds: {value}")

    @property
    def pos_y(self):
        return self.__pos_y

    @pos_y.setter
    def pos_y(self, value: int):
        if 0 <= value <= self.game.height:
            self.__pos_y = value
        else:
            raise IndexError(f"Trying to place the player out of bounds: {value}")

    @property
    def game(self):
        return self.__game

    @property
    def treasure(self):
        return self.__treasure

    @treasure.setter
    def treasure(self, value: int):
        if isinstance(value, int):
            self.__treasure = value
        else:
            raise ValueError(f"Trying to set a number of treasure that is not an int: {value}")

    @property
    def orientation(self):
        return self.__orientation

    def change_orientation(self, value: int) -> None:
        """
        Changing the orientation of our fighter
        :param value: 1 if change to the right or -1 if change to the left
        :return: None
        """
        if value == 1 or value == -1:
            # Using our enumeration's values to handle the new orientation
            new_orientation_value = self.__orientation.value + value

            # If the value is either 4 or -1, we correct the value to match with our enumeration
            if new_orientation_value == 4:
                new_orientation_value = 0
            elif new_orientation_value == -1:
                new_orientation_value = 3

            # Getting new orientation
            self.__orientation = OrientationEnum(new_orientation_value)
        else:
            raise ValueError(
                f"Wrong change of orientation requested by the user: expected -1 or 1, got {value} instead")

    def request_move(self, move: str) -> bool:
        """
        Function that is going to handle our moves requests
        Coding it that way allows us to thread it if needed later
        In order to do so we would just have to add a mutex to the map object
        :param move: Move requested
        :return:
        """
        if move == "D":
            self.change_orientation(1)
        elif move == "G":
            self.change_orientation(-1)
        else:
            # Checking the orientation and requesting the right move - updating position if the move was accepted
            if self.orientation == OrientationEnum.E:
                if self.game.request_move(self.pos_x, self.pos_y, self.pos_x + 1, self.pos_y):
                    self.pos_x = self.pos_x + 1

            elif self.orientation == OrientationEnum.W:
                if self.game.request_move(self.pos_x, self.pos_y, self.pos_x - 1, self.pos_y):
                    self.pos_x = self.pos_x - 1

            elif self.orientation == OrientationEnum.S:
                if self.game.request_move(self.pos_x, self.pos_y, self.pos_x, self.pos_y + 1):
                    self.pos_y = self.pos_y + 1

            elif self.orientation == OrientationEnum.N:
                if self.game.request_move(self.pos_x, self.pos_y, self.pos_x, self.pos_y - 1):
                    self.pos_y = self.pos_y - 1

    def consume_move(self) -> bool:
        """
        Function that is going to pop a move from our list
        :return: None
        """
        try:
            self.request_move(self.__moves.pop(0))
            return True
        except IndexError:
            # No more moves in the list
            return False

    def add_treasure(self) -> None:
        self.treasure = self.treasure + 1
