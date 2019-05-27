from Map import Map
from Mountain import Mountain


def read_file(path: str) -> list:
    """
    Reads a file that contains information for our game
    :param path: Path where we should read our file
    :return:
    """
    f = open(path, "r")
    lines = []

    for line in f:
        # Iterating over the lines and storing them in a list if they are not comments
        if not line.startswith('#'):
            lines.append(line.split('-'))
    return lines


def game_loop():
    lines = read_file("./test.txt")
    my_map = None
    for line in lines:
        if line[0] == "C":
            my_map = Map(int(line[1]), int(line[2]))
        elif line[0] == "M":
            if not my_map.get_cell(int(line[1]), int(line[2])).is_empty:
                raise IndexError(f"Trying to set an already set cell at ({int(line[1])}, {int(line[2])})")
            my_map.update_cell(int(line[1]), int(line[2]), Mountain())
        elif line[0] == "T":
        elif line[0] == "A":
