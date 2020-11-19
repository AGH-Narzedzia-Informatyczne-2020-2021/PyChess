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

        def add_moves(candidates_for_moves):

                for square in candidates_for_moves:

                    piece = self.pieces.get(square)

                    if piece is None:
                        possible_moves.append(Move(self, square[0], square[1]))

                    elif piece.is_white != self.is_white:
                        captured_piece = self.pieces.get(square)
                        possible_moves.append(Move(self, square[0], square[1], captured_piece=captured_piece))
                        return

                    else:
                        return

            add_moves((row + 2), (column + 1))
            add_moves((row + 2), (column - 1))
            add_moves((row + 1), (column + 2))
            add_moves((row + 1), (column - 2))
            add_moves((row - 2), (column + 1))
            add_moves((row - 2), (column - 1))
            add_moves((row - 1), (column + 2))
            add_moves((row - 1), (column - 2))

            return possible_moves


