from Cell import Cell


class Mountain(Cell):
    def __init__(self):
        super(Mountain, self).__init__()

    def __str__(self):
        return "M"