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

        def discovered_check():
            copied_pieces = self.pieces.copy()
            copied_piece = copied_pieces.get((self.column, self.row))
            copied_piece.column = column
            copied_piece.row = row
            return copied_pieces.is_checked(self.is_white)

        possible_moves = self.get_possible_moves()
        possible_captures = self.get_possible_captures()

        for (move, piece) in possible_captures:
            possible_moves.remove(move)

        for (move, piece) in possible_captures:
            if move == (column, row) and not discovered_check():
                self.pieces.remove(piece)
                self.column = column
                self.row = row
                return True

        for move in possible_moves:
            if move == (column, row) and not discovered_check():
                self.column = column
                self.row = row
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

    @abstractmethod
    def get_possible_captures(self):
        # Powinna zwracać możliwe zbicia w formacie listy o elementach: ((column, row), piece),
        # gdzie column i row to miejsce na które będzie przesunięta figura, a piece to bita figura.
        pass
