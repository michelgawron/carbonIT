from enum import Enum


class OrientationEnum(Enum):
    """
    Enumeration we are going to use to handle our fighters' orientation
    Giving integers values to our moves allows us to use the .value and the OrientationEnum(value) constructor to handle
    orientation changes. For instance if we have a fighter oriented West, we just have to add 1 to rotate it to North.
    """
    S = 0
    W = 1
    N = 2
    E = 3

