from Cell import Cell
from Mountain import Mountain
from Treasure import Treasure


class Map(object):
    """
    This class defines the map of our game

    Methods:
        - update_cell(i: int, j: int, newValue: Cell) -> None:
            Updates the cell on (i, j) position in our list
        - request_move(x: int, y: int, new_x: int, new_y: int) -> bool:
            Tries to apply the move and returns true if move possible and false if not
        - generate_map() -> None:
            Generates a text file resuming the state of the map
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
        self.__cells = [[Cell(i, j) for i in range(width)] for j in range(height)]

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
        return self.__cells[j][i]

    def __str__(self):
        result = ""
        for _ in range(self.width):
            result += "____"
        result += "_\n"
        for lines in self.cells:
            result += "|"
            for index, el in enumerate(lines, start=1):
                result += f" {str(el)} -" if index != self.width else f" {str(el)} |"
            result += "\n"
            for _ in range(self.width):
                result += "____"
            result += "_\n"
        return result

    def update_cell(self, i: int, j: int, new_value: Cell) -> None:
        """
        Updates the cell on (i, j) position in our list
        :param i: indice i of the cell
        :param j: indice j of the cell
        :param new_value: new value to replace
        :return: None
        """
        try:
            self.__cells[j][i] = new_value
        except IndexError:
            print("Trying to update a cell with index out of bounds")

    def request_move(self, x: int, y: int, new_x: int, new_y: int) -> bool:
        """
        Requesting a move on the map
        :param x: Actual x coordinate of the fighter
        :param y: Actual y coordinate of the fighter
        :param new_x: New x coordinate of the fighter
        :param new_y: New y coordinate of the fighter
        :return: True if the move is possible, False else
        """
        # Checking if the move is possible (if it is not out of bounds and on an empty cell)
        if self.get_cell(new_x, new_y).is_empty and 0 <= new_x < self.width and 0 <= new_y < self.height:
            # Setting the fighter on a new cell and emptying the previous one
            self.cells[new_y][new_x].fighter = self.get_cell(x, y).fighter
            self.cells[y][x].fighter = None
            self.cells[new_y][new_x].is_empty = False
            self.cells[y][x].is_empty = True

            # Picking up treasures if there is one on the grond
            if type(self.get_cell(new_x, new_y)) is Treasure and self.get_cell(new_x, new_y).n > 0:
                self.cells[new_y][new_x].consume_treasure()
                self.get_cell(new_x, new_y).fighter.add_treasure()
            return True
        else:
            return False

    def generate_map(self, path="./resume.txt"):
        """
        Generates a text file resuming the state of the game
        :param path: Path where the file should be stored - defaults to the code directory and resume.txt file name
        :return: None
        """
        lines = f"C - {self.width} - {self.height}\n"
        for cells in self.cells:
            for cell in cells:
                if isinstance(cell, Mountain):
                    lines += f"M - {cell.x} - {cell.y}\n"
                if isinstance(cell, Treasure):
                    lines += f"T - {cell.x} - {cell.y} - {cell.n}\n"
                if not cell.fighter is None:
                    lines += f"A - {cell.fighter.name} - {cell.x} - {cell.y} - {cell.fighter.orientation.name} - {cell.fighter.treasure}\n"
        with open(path, "w") as text_file:
            text_file.writelines(lines)
