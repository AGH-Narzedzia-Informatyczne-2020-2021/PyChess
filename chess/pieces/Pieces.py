from chess.pieces.Pawn import Pawn
from chess.pieces.Rook import Rook
from chess.pieces.Knight import Knight
from chess.pieces.King import King
from chess.pieces.Bishop import Bishop
from chess.pieces.Queen import Queen


class Pieces(list):

    def __init__(self):
        super().__init__()

        self.append(King(5, 1, True, self))
        self.append(King(5, 8, False, self))

        self.append(Queen(4, 1, True, self))
        self.append(Queen(4, 8, False, self))

        self.append(Rook(1, 1, True, self))
        self.append(Rook(8, 1, True, self))
        self.append(Rook(8, 8, False, self))
        self.append(Rook(1, 8, False, self))

        self.append(Knight(7, 1, True, self))
        self.append(Knight(2, 1, True, self))
        self.append(Knight(2, 8, False, self))
        self.append(Knight(7, 8, False, self))

        self.append(Bishop(6, 1, True, self))
        self.append(Bishop(3, 1, True, self))
        self.append(Bishop(3, 8, False, self))
        self.append(Bishop(6, 8, False, self))

        for column in range(1, 9):
            self.append(Pawn(column, 2, True, self))
            self.append(Pawn(column, 7, False, self))

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
