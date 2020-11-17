from abc import ABC, abstractmethod
from chess.figures.King import King


class Figure(ABC):
    def __init__(self, column, row, is_white, pieces):
        self.column = column
        self.row = row
        self.is_white = is_white
        self.pieces = pieces
        self.image = None

    def move(self, column, row):
        if (column, row) in self.get_possible_moves():
            self.column = column
            self.row = row
            return True

        if (column, row) in self.get_possible_captures():
            for figure in self.figures:
                if (figure.column, figure.row) == (column, row):
                    self.figures.remove(figure)
                    return True

        return False

    def is_ally(self, another_figure):
        return self.is_white == another_figure.is_white

    def is_king(self):
        type(self) == King

    @abstractmethod
    def load_image(self):
        pass

    @abstractmethod
    def get_possible_moves(self):
        pass

    @abstractmethod
    def get_possible_captures(self):
        pass
