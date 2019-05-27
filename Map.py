from Cell import Cell


class Map(object):
    """
    This class defines the map of our game

    Methods:
        - updateCell(i: int, j: int, newValue: Cell) -> None:
            Updates the cell on (i, j) position in our list
    """

    def __init__(self, width: int, height: int) -> None:
        """
        Our map's constructor
        :param width: Map's width
        :param height: Map's height
        """
        self.__width = width
        self.__height = height

        # Creating a list of empty cells to initialize the game
        self.__cells = [[Cell()] * width] * height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def cells(self):
        return self.__cells

    def get_cell(self, i, j):
        return self.__cells[i][j]

    def update_cell(self, i: int, j: int, new_value: Cell):
        """
        Updates the cell on (i, j) position in our list
        :param i: indice i of the cell
        :param j: indice j of the cell
        :param new_value: new value to replace
        :return:
        """
        try:
            self.__cells[i][j] = new_value
        except IndexError:
            print("Trying to update a cell with index out of bounds")
