from Fighter import Fighter


class Cell(object):
    """
    This class defines a cell in our game
    """

    def __init__(self, x: int, y: int, is_empty=True, fighter=None) -> None:
        """
        Our cell's constructor
        :param is_empty: Defines the emptiness of our cell
        :param fighter: If needed we can provide a fighter on the cell
        """
        self.__is_empty = is_empty

        # An empty cell has no fighter on it
        self.__fighter = fighter
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def is_empty(self):
        return self.__is_empty

    @is_empty.setter
    def is_empty(self, value: bool):
        if isinstance(value, bool):
            self.__is_empty = value
        else:
            raise ValueError(f"Boolean value expected, got {str(type(value))} instead")

    @property
    def fighter(self):
        return self.__fighter

    @fighter.setter
    def fighter(self, value: Fighter):
        if isinstance(value, Fighter) or value is None:
            self.__fighter = value
        else:
            raise ValueError(f"Fighter value expected, got {str(type(value))} instead")

    def __str__(self):
        return " " if self.is_empty else str(self.fighter)
