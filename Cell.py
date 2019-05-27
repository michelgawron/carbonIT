from Fighter import Fighter


class Cell(object):
    """
    This class defines a cell in our game
    """

    def __init__(self):
        """
        Our cell's constructor
        """
        self.__is_empty = True

        # An empty cell has no fighter on it
        self.__fighter = None

    @property
    def is_empty(self):
        return self.__is_empty

    @is_empty.setter
    def is_empty(self, value):
        if isinstance(bool, value):
            self.__is_empty = value
        else:
            raise ValueError(f"Boolean value expected, got {str(type(value))} instead")

    @property
    def fighter(self):
        return self.__fighter

    @fighter.setter
    def fighter(self, value):
        if isinstance(Fighter, value):
            self.__fighter = value
        else:
            raise ValueError(f"Fighter value expected, got {str(type(value))} instead")

    def __str__(self):
        return " " if self.is_empty else self.fighter
