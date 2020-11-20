from chess.pieces.Pawn import Pawn
from chess.pieces.Rook import Rook
from chess.pieces.Knight import Knight
from chess.pieces.King import King
from chess.pieces.Bishop import Bishop
from chess.pieces.Queen import Queen


class Pieces(list):

    def get(self, square):
        for piece in self:
            if square == (piece.column, piece.row):
                return piece
        return None

    def get_king(self, is_white):
        for piece in self:
            if type(piece) == King and piece.is_white == is_white:
                return piece

    def is_checked(self, is_white):
        king = self.get_king(is_white)

        for piece in self:
            if piece.is_white != is_white:
                for move in piece.get_possible_moves():
                    if move.captured_piece == king:
                        return True
        return False

    def copy(self):
        copied = Pieces()
        for piece in self:
            copied.append(piece.__class__(piece.column, piece.row, piece.is_white, copied))
        return copied
