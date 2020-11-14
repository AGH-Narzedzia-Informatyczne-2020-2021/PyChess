from chess.constants import WHITE, BLACK, SQUARE_SIZE
import pygame as pg

class Knight:
    def __init__(self, color):
        self.color = color
        if self.color == WHITE:
            self.image = pg.transform.scale(pg.image.load('chess/figures_graphics/wN.png'), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            self.image = pg.transform.scale(pg.image.load('chess/figures_graphics/bN.png'), (SQUARE_SIZE, SQUARE_SIZE))


    #chodzenie
    def physically_possible_moves(self, row, column):

        moves = []

        if self.color == WHITE:
            moves.append((row + 2), (column + 1))
            moves.append((row + 2), (column - 1))
            moves.append((row + 1), (column + 2))
            moves.append((row + 1), (column - 2))
            moves.append((row - 2), (column + 1))
            moves.append((row - 2), (column - 1))
            moves.append((row - 1), (column + 2))
            moves.append((row - 1), (column - 2))

        if self.color == BLACK:
            moves.append((row + 2), (column + 1))
            moves.append((row + 2), (column - 1))
            moves.append((row + 1), (column + 2))
            moves.append((row + 1), (column - 2))
            moves.append((row - 2), (column + 1))
            moves.append((row - 2), (column - 1))
            moves.append((row - 1), (column + 2))
            moves.append((row - 1), (column - 2))

    #bicie
    def physically_possible_captures(self, row, column):

        moves = []

        if self.color == WHITE:
            moves.append((row + 2), (column + 1))
            moves.append((row + 2), (column - 1))
            moves.append((row + 1), (column + 2))
            moves.append((row + 1), (column - 2))
            moves.append((row - 2), (column + 1))
            moves.append((row - 2), (column - 1))
            moves.append((row - 1), (column + 2))
            moves.append((row - 1), (column - 2))

        if self.color == BLACK:
            moves.append((row + 2), (column + 1))
            moves.append((row + 2), (column - 1))
            moves.append((row + 1), (column + 2))
            moves.append((row + 1), (column - 2))
            moves.append((row - 2), (column + 1))
            moves.append((row - 2), (column - 1))
            moves.append((row - 1), (column + 2))
            moves.append((row - 1), (column - 2))

    def is_ally(self, another_figure):
        if self.color == another_figure.color:
            return True
        else:
            return False
