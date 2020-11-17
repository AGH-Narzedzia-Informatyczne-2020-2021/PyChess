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

        def discovered_check():
            copied_figures = self.figures.copy()
            figure = copied_figures.get(column, row)
            figure.column = column
            figure.row = row
            return copied_figures.is_checked(self.is_white)

        if (column, row) in self.get_possible_moves() and not discovered_check():
            self.column = column
            self.row = row
            return True

        if (column, row) in self.get_possible_captures() and not discovered_check():
            self.figures.get(column, row)

        return False

    def is_ally(self, another_figure):
        return self.is_white == another_figure.is_white

    def is_king(self):
        type(self) == King

    @abstractmethod
    def load_image(self):
        # Powinna ładować obrazek do zmiennej image
        pass

    @abstractmethod
    def get_possible_moves(self):
        # Powinna zwracać możliwe ruchy w formacie: (column, row),
        # gdzie column i row to miejsce na które będzie przesunięta figura.
        pass

    @abstractmethod
    def get_possible_captures(self):
        # Powinna zwracać możliwe zbicia w formacie: ((column, row), figure),
        # gdzie column i row to miejsce na które będzie przesunięta figura, a figure to bita figura.
        pass
