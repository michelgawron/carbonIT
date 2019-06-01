from Cell import Cell
from Fighter import Fighter
from Map import Map
from Mountain import Mountain
from Treasure import Treasure
import argparse


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
            lines.append(list(map(lambda x: str(x).strip(), line.split('-'))))
    return lines


def game_loop(path="./test.txt", interactive_mode=False):
    """
    Loop to handle our game
    :return: None
    """
    lines = read_file(path)
    my_map = None

    fighters = []

    # Processing cells
    for line in lines:
        if line[0] == "C":
            # Map cell case - creating the map
            my_map = Map(int(line[1]), int(line[2]))

        elif line[0] == "M":
            # Moutain cell case - checking if the cell we are aiming for is empty
            if not my_map.get_cell(int(line[1]), int(line[2])).is_empty:
                # If trying to set a mountain cell on a non empty cell, raising an error
                raise IndexError(f"Trying to set an already set cell at ({int(line[1])}, {int(line[2])})")
            my_map.update_cell(int(line[1]), int(line[2]), Mountain(int(line[1]), int(line[2])))

        elif line[0] == "T":
            # Treasure cell case
            if not my_map.get_cell(int(line[1]), int(line[2])).is_empty:
                # If trying to set a mountain cell on a non empty cell, raising an error
                raise IndexError(f"Trying to set an already set cell at ({int(line[1])}, {int(line[2])})")
            my_map.update_cell(int(line[1]), int(line[2]), Treasure(int(line[1]), int(line[2]), int(line[3])))

        elif line[0] == "A":
            # Fighter cell case
            if not my_map.get_cell(int(line[2]), int(line[3])).is_empty:
                # If trying to set a mountain cell on a non empty cell, raising an error
                raise IndexError(f"Trying to set an already set cell at ({int(line[2])}, {int(line[3])})")
            my_map.update_cell(int(line[2]), int(line[3]), Cell(int(line[2]), int(line[3]), is_empty=False,
                                                                fighter=Fighter(line[-1], line[1], my_map, int(line[2]),
                                                                                int(line[3]), line[4])))
            # Appending fighter to the list of fighters
            fighters.append(my_map.get_cell(int(line[2]), int(line[3])).fighter)

    # Game loop - always true if a single fighter can consume a move
    continuation = True
    while continuation:
        continuation = False

        # Continuation condition
        for fighter in fighters:
            if fighter.consume_move():
                continuation = True

        # If interactive mode is set, printing the map
        if interactive_mode:
            print(my_map)
            key = input("Press enter to continue, q then enter to close interactive mode")
            if key == "q":
                interactive_mode = False

    print(my_map)
    my_map.generate_map()


if __name__ == '__main__':
    # Getting arguments from the command line
    parser = argparse.ArgumentParser(description="Run the fighter's game")
    parser.add_argument("--interactiveMode", "-i", help="use the interactive mode", action="store_true")
    parser.add_argument("path", metavar="P", type=str, help="path where the game's file is located")
    args, leftovers = parser.parse_known_args()
    print(args)

    # Executing the game loop in interactive mode
    game_loop(path=args.path, interactive_mode=args.interactiveMode)
