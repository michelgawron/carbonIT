from Cell import Cell


class Mountain(Cell):
    """
    Mountain class - it is primarily used as a wrapper in case we would like to implement a different behaviour for those cells
    """
    def __init__(self, x: int, y: int):
        super(Mountain, self).__init__(x, y, is_empty=False)

    def __str__(self):
        return "M"
