from chess.constants import WHITE, BLACK, SQUARE_SIZE
import pygame as pg


class Bishop:
    def __init__(self, color):
        self.color = color
        if self.color == WHITE:
            self.image = pg.transform.scale(pg.image.load('chess/figures_graphics/wB.png'), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            self.image = pg.transform.scale(pg.image.load('chess/figures_graphics/bB.png'), (SQUARE_SIZE, SQUARE_SIZE))

# chodzenie
    def physically_possible_moves(self, row, column):

        moves = []

        if self.color == WHITE:
            directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))   # przekątne
            for d in directions:
                for i in range(1, 8):   # max 7 pól
                    end_row = row + d[0] * i
                    end_column = column + d[1] * i
                    moves.append((end_row, end_column))

        if self.color == BLACK:
            directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))   # przekątne
            for d in directions:
                for i in range(1, 8):   # max 7 pól
                    end_row = row + d[0] * i
                    end_column = column + d[1] * i
                    moves.append((end_row, end_column))

# bicie
    def physically_possible_captures(self, row, column):

        moves = []

        if self.color == WHITE:
            directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))   # przekątne
            for d in directions:
                for i in range(1, 8):   # max 7 pól
                    end_row = row + d[0] * i
                    end_column = column + d[1] * i
                    moves.append((end_row, end_column))

        if self.color == BLACK:
            directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))   # przekątne
            for d in directions:
                for i in range(1, 8):   # max 7 pól
                    end_row = row + d[0] * i
                    end_column = column + d[1] * i
                    moves.append((end_row, end_column))

    def is_ally(self, another_figure):
        if self.color == another_figure.color:
            return True
        else:
            return False
