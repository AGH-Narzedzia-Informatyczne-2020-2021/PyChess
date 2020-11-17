from chess.figures.Pawn import Pawn
from chess.figures.Rook import Rook
from chess.figures.Knight import Knight
from chess.figures.King import King
from chess.figures.Bishop import Bishop
from chess.figures.Queen import Queen


class Figures(list):

    def get(self, column, row):
        for figure in self:
            if (column, row) == (figure.column, figure.row):
                return figure
        return None

    def get(self, square):
        return self.get(square[0], square[1])

    def get_king(self, is_white):
        for figure in self:
            if type(figure) == King and figure.is_white == is_white:
                return figure

    def is_checked(self, is_white):
        possible_captures = []

        for figure in self:
            if figure.is_white != is_white:
                possible_captures.extend(figure.get_possible_captures())

        return self.get_king() in possible_captures

    def copy(self):
        copied = Figures()
        for figure in self:
            copied.append(figure.__class__(figure.column, figure.row, figure.is_white, copied))
        return copied
