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


        if self.is_white:
            if self.row == 2:
                if self.pieces.get((self.column, self.row + 2)) is None and self.pieces.get((self.column, self.row + 1)) is None:
                    possible_moves.append(Move(self, self.column, self.row + 2))
                    possible_moves.append(Move(self, self.column, self.row + 1))
                elif self.pieces.get((self.column, self.row + 2)) is not None and self.pieces.get((self.column, self.row + 1)) is None:
                    possible_moves.append(Move(self, self.column, self.row + 1))

            elif self.row != 8:
                if self.pieces.get((self.column, self.row + 1)) is None:
                    possible_moves.append(Move(self, self.column, self.row + 1))
            if self.column != 8 and self.row != 8 and self.pieces.get((self.column + 1, self.row + 1)) is not None:
                if self.pieces.get((self.column + 1, self.row + 1)).is_white != self.is_white:
                    possible_moves.append(Move(self, self.column + 1, self.row + 1, self.pieces.get((self.column + 1, self.row + 1))))
            if self.column != 1 and self.row != 8 and self.pieces.get((self.column - 1, self.row + 1)) is not None:
                if self.pieces.get((self.column - 1, self.row + 1)).is_white != self.is_white:
                    possible_moves.append(Move(self, self.column - 1, self.row + 1, self.pieces.get((self.column - 1, self.row + 1))))
        else:
            if self.row == 7:
                if self.pieces.get((self.column, self.row - 2)) is None and self.pieces.get((self.column, self.row - 1)) is None:
                    possible_moves.append(Move(self, self.column, self.row - 1))
                    possible_moves.append(Move(self, self.column, self.row - 2))
                elif self.pieces.get((self.column, self.row - 2)) is not None and self.pieces.get((self.column, self.row - 1)) is None:
                    possible_moves.append(Move(self, self.column, self.row - 1))
            elif self.row != 1:
                if self.pieces.get((self.column, self.row - 1)) is None:
                    possible_moves.append(Move(self, self.column, self.row - 1))
            if self.column != 1 and self.row != 1 and self.pieces.get((self.column - 1, self.row - 1)) is not None:
                if self.pieces.get((self.column - 1, self.row - 1)).is_white != self.is_white:
                    possible_moves.append(Move(self, self.column - 1, self.row - 1, self.pieces.get((self.column - 1, self.row - 1))))
            if self.column != 8 and self.row != 1 and self.pieces.get((self.column + 1, self.row - 1)) is not None:
                if self.pieces.get((self.column + 1, self.row - 1)).is_white != self.is_white:
                    possible_moves.append(Move(self, self.column + 1, self.row - 1, self.pieces.get((self.column + 1, self.row - 1))))

        return possible_moves