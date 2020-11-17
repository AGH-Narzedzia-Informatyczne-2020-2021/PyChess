from chess.constants import WHITE, BLACK, SQUARE_SIZE
import pygame as pg


class Pawn:
    def __init__(self, color):
        self.color = color
        if self.color == WHITE:
            self.image = pg.transform.scale(pg.image.load('chess/pieces_graphics/wp.png'), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            self.image = pg.transform.scale(pg.image.load('chess/pieces_graphics/bp.png'), (SQUARE_SIZE, SQUARE_SIZE))


    #chodzenie
    def physically_possible_moves(self, row, column):  # czyli nie uwzględniamy że np może odsłonić króla albo w coś wejśc

        moves = []

        if self.color == WHITE:
            if row == 6:  # bo numerujemy od góry i od zera
                moves.append((row+2, column))  # jeżeli jest na pozycji startowej to o 2 do przodu
            moves.append((row+1, column))  # no i normalnie

        if self.color == BLACK:
            if row == 1:  # to samo co u białych
                moves.append((row-2, column))  # jeżeli jest na pozycji startowej to o 2 do przodu
            moves.append((row-1, column))  # no i normalnie

    #zwykłe bicie
    def physically_possible_captures_normal(self, row, column): #nie uwzgledniamy ze moze nie byc czegos zbic

        moves=[]

        if self.color == WHITE:
            moves.append((row+1, column+1), (row+1, column+1))
        if self.color == BLACK:
            moves.append((row - 1, column + 1), (row - 1, column + 1))

    #en passant (w przelocie)
    def physically_possible_captures_en_passant(self, row, column, last_move = None): #UWAGA TA FUNKCJA JEST TYLKO DLA PIONKÓW

        moves = []

        if self.color == WHITE and row == 3 and last_move[0] == Pawn and last_move[1][0] == 3:
            if last_move[1][1] == column-1:
                moves.append((row+1, column-1))
            if last_move[1][1] == column + 1:
                moves.append((row + 1, column + 1))

        if self.color == BLACK and row == 4 and last_move[0] == Pawn and last_move[1][0] == 4:
            if last_move[1][1] == column-1:
                moves.append((row-1, column-1))
            if last_move[1][1] == column + 1:
                moves.append((row - 1, column + 1))

    def is_ally(self, another_figure):
        if self.color == another_figure.color:
            return True
        else:
            return False



