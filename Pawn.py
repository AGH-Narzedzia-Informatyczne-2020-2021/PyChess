from Figure import Figure
from constants import WHITE, BLACK, SQUARE_SIZE
import pygame as pg


class Pawn:
    def __init__(self, row, column, color):
        self.column = column
        self.row = row
        self.color = color
        if self.color == WHITE:
            self.image = pg.transform.scale(pg.image.load('figures/wp.png'), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            self.image = pg.transform.scale(pg.image.load('figures/bp.png'), (SQUARE_SIZE, SQUARE_SIZE))

    def physically_possible_moves(self):  # czyli nie uwzględniamy że np może odsłonić króla albo w coś wejśc
        moves = []
        # chodzenie
        if self.color == WHITE:
            if self.row == 6:  # bo numerujemy od góry i od zera
                moves.append((self.x, self.y + 2))  # jeżeli jest na pozycji startowej to o 2 do przodu
            moves.append((self.x, self.y + 1))  # no i normalnie

        if self.color == BLACK:
            if self.row == 1:  # to samo co u białych
                moves.append((self.x, self.y - 2))  # jeżeli jest na pozycji startowej to o 2 do przodu
            moves.append((self.x, self.y - 1))  # no i normalnie

    def physically_possible_captures(self): #nie uwzgledniamy ze moze nie byc czego zbic
        pass

    def is_ally(self, another_figure):
        if self.color == another_figure.color:
            return True
        else:
            return False



