from abc import ABC, abstractmethod

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

    def get_legal_moves(self):
        moves_to_delete = []
        possible_moves = self.get_possible_moves()
        for move in possible_moves:
            if move.causes_self_check():
                moves_to_delete.append(move)
        for move in moves_to_delete:
            possible_moves.remove(move)

        return possible_moves

    @abstractmethod
    def load_image(self):
        # Powinna ładować obrazek do zmiennej image
        pass

    @abstractmethod
    def get_possible_moves(self):
        # Powinna zwracać listę obiektów typu Move. Zajrzyj do klasy move żeby wiedzieć jak je tworzyć
        pass
