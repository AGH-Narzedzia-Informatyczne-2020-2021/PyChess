from abc import ABC, abstractmethod
from chess.figures.King import King
from chess.figures.Pawn import Pawn


class Figure(ABC):
    def __init__(self, column, row, is_white, figures):
        self.column = column
        self.row = row
        self.is_white = is_white
        self.figures = figures
        self.image = None

    def move(self, column, row):

        def discovered_check():
            copied_figures = self.figures.copy()
            copied_figure = copied_figures.get(self.column, self.row)
            copied_figure.column = column
            copied_figure.row = row
            return copied_figures.is_checked(self.is_white)

        possible_moves = self.get_possible_moves()
        possible_captures = self.get_possible_captures()

        for (move, figure) in possible_captures:
            possible_moves.remove(move)

        for (move, figure) in possible_captures:
            if move == (column, row) and not discovered_check():
                self.figures.remove(figure)
                self.column = column
                self.row = row
                return True

        for move in possible_moves:
            if move == (column, row) and not discovered_check():
                self.column = column
                self.row = row
                return True

        return False

    def is_ally(self, another_figure):
        return self.is_white == another_figure.is_white

    def is_king(self):
        return type(self) == King

    @abstractmethod
    def load_image(self):
        # Powinna ładować obrazek do zmiennej image
        pass

    @abstractmethod
    def get_possible_moves(self):
        # Powinna zwracać możliwe ruchy(w tym bicia) w formacie listy o elementach: (column, row),
        # gdzie column i row to miejsce na które będzie przesunięta figura.
        pass

    @abstractmethod
    def get_possible_captures(self):
        # Powinna zwracać możliwe zbicia w formacie listy o elementach: ((column, row), figure),
        # gdzie column i row to miejsce na które będzie przesunięta figura, a figure to bita figura.
        pass
