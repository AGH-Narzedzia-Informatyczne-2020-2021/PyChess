from chess.pieces.Pawn import Pawn
from chess.pieces.Rook import Rook
from chess.pieces.Knight import Knight
from chess.pieces.King import King
from chess.pieces.Bishop import Bishop
from chess.pieces.Queen import Queen


class Pieces(list):

    def get(self, column, row):
        for piece in self:
            if (column, row) == (piece.column, piece.row):
                return piece
        return None

    def get(self, square):
        return self.get(square[0], square[1])

    def get_king(self, is_white):
        for piece in self:
            if type(piece) == King and piece.is_white == is_white:
                return piece

    def is_checked(self, is_white):
        possible_captures = []

        for piece in self:
            if piece.is_white != is_white:
                possible_captures.extend(piece.get_possible_captures())

        return self.get_king() in possible_captures

    def copy(self):
        copied = Pieces()
        for piece in self:
            copied.append(piece.__class__(piece.column, piece.row, piece.is_white, copied))
        return copied
