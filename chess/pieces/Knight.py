from chess.pieces.Piece import Piece
from chess.constants import SQUARE_SIZE
from chess.Move import Move
import pygame as pg
import os

class Knight(Piece):

    def load_image(self):
        if self.is_white:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'wN.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'bN.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))


    def get_possible_moves(self):

            possible_moves = []

            def add_moves(square):

                #for square in candidates_for_moves:
                    piece = self.pieces.get(square)




            add_moves((self.column + 2, self.row + 1))
            add_moves((self.column + 2, self.row - 1))
            add_moves((self.column + 1, self.row + 2))
            add_moves((self.column + 1, self.row - 2))
            add_moves((self.column - 2, self.row + 1))
            add_moves((self.column - 2, self.row - 1))
            add_moves((self.column - 1, self.row + 2))
            add_moves((self.column - 1, self.row - 2))

            return possible_moves


