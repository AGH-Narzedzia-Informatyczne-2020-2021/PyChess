from chess.pieces.Piece import Piece
from chess.Move import Move
from chess.constants import SQUARE_SIZE
import os
import pygame as pg


class King(Piece):

    def load_image(self):
        if self.is_white:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'wK.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'bK.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))

    def get_possible_moves(self, x=True):
        possible_moves = []

        vectors = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
        vectors.remove((0, 0))
        for vector in vectors:
            column = self.column - vector[0]
            row = self.row - vector[1]
            if row in range(1, 9) and column in range(1, 9):
                captured_piece = self.pieces.get((column, row))
                if captured_piece is None:
                    possible_moves.append(Move(self, column, row))
                elif captured_piece.is_white != self.is_white:
                    possible_moves.append(Move(self, column, row, captured_piece=captured_piece))

        return possible_moves
