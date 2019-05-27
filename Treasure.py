from Cell import Cell


class Treasure(object, Cell):
    """
    This class defines a treasure cell in our game

    Methods:
        - consume_treasure(None) -> None:
            Consumes a treasure
    """

    def __init__(self, n):
        super(Treasure, self).__init__()
        self.__n = n

    @property
    def n(self):
        return self.__n

    @n.setter
    def n(self, value):
        self.__n = value

    def consume_treasure(self) -> None:
        """
        Consumes a treasure
        :return: None
        """
        self.n = self.n - 1
