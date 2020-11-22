from chess.pieces.Piece import Piece
from chess.constants import SQUARE_SIZE
from chess.Move import Move
import pygame as pg
import os


class Pawn(Piece):

    def load_image(self):
        if self.is_white:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'wp.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'bp.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))

    def get_possible_moves(self):

        possible_moves = []

        column = self.column
        row = self.row
        add_moves = possible_moves.append
        get = self.pieces.get

        #Biale
        if self.is_white:
            #Ruch z pozycji startowej
            if row == 2:
                if get((column, row + 2)) is None and get((column, row + 1)) is None:
                    add_moves(Move(self, column, row + 2))
                    add_moves(Move(self, column, row + 1))
                elif get((column, row + 2)) is not None and get((column, row + 1)) is None:
                    add_moves(Move(self, column, row + 1))

            #Zwykly ruch
            elif row != 8:
                if get((column, row + 1)) is None:
                    add_moves(Move(self, column, row + 1))

            #Bicie
            if column != 8 and row != 8 and get((column + 1, row + 1)) is not None:
                if get((column + 1, row + 1)).is_white != self.is_white:
                    add_moves(Move(self, column + 1, row + 1, get((column + 1, row + 1))))
            if column != 1 and row != 8 and get((column - 1, row + 1)) is not None:
                if get((column - 1, row + 1)).is_white != self.is_white:
                    add_moves(Move(self, column - 1, row + 1, get((column - 1, row + 1))))

        #Czarne:
        else:
            #Ruch z pozycji startowej
            if row == 7:
                if get((column, row - 2)) is None and get((column, row - 1)) is None:
                    add_moves(Move(self, column, row - 1))
                    add_moves(Move(self, column, row - 2))
                elif get((column, row - 2)) is not None and get((column, row - 1)) is None:
                    add_moves(Move(self, column, row - 1))

            #Zwykly ruch
            elif row != 1:
                if get((column, row - 1)) is None:
                    add_moves(Move(self, column, row - 1))

            #Bicie:
            if column != 1 and row != 1 and get((column - 1, row - 1)) is not None:
                if get((column - 1, row - 1)).is_white != self.is_white:
                    add_moves(Move(self, column - 1, row - 1, get((column - 1, row - 1))))
            if column != 8 and row != 1 and get((column + 1, row - 1)) is not None:
                if get((column + 1, row - 1)).is_white != self.is_white:
                    add_moves(Move(self, column + 1, row - 1, get((column + 1, row - 1))))

        return possible_moves