from abc import ABC, abstractmethod
from chess.pieces.King import King
from chess.pieces.Pawn import Pawn


class Piece(ABC):
    def __init__(self, column, row, is_white, pieces):
        self.column = column
        self.row = row
        self.is_white = is_white
        self.pieces = pieces
        self.image = None
        self.load_image()

    def move(self, column, row):
        for move in self.get_possible_moves():
            if (column, row) == (move.column, move.row):
                move.do()
                return True
        return False

    def is_ally(self, another_piece):
        return self.is_white == another_piece.is_white

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
