from constants import WHITE, BLACK


class Figure:
    def __init__(self, column, row, color):
        self.column = column
        self.row = row
        self.color = color

    def move(self, column, row):
        print("moved")
        self.column = column
        self.row = row

    def is_ally(self, another_figure):
        if self.color == another_figure.color:
            return True
        else:
            return False