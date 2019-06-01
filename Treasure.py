from Cell import Cell


class Treasure(Cell):
    """
    This class defines a treasure cell in our game

    Methods:
        - consume_treasure(None) -> None:
            Consumes a treasure
    """

    def __init__(self, x: int, y: int, n: int):
        super(Treasure, self).__init__(x, y)
        self.__n = n

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        self.__n = value

    def __str__(self):
        return str(self.n) if self.is_empty else str(self.fighter)

    def consume_treasure(self) -> None:
        """
        Consumes a treasure if there are left on the cell
        :return: None
        """
        self.n = self.n - 1 if self.n > 0 else 0
