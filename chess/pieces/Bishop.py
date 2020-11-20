from chess.pieces.Piece import Piece
from chess.constants import SQUARE_SIZE
from chess.Move import Move
import pygame as pg
import os


class Bishop(Piece):

    def load_image(self):
        if self.is_white:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'wB.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'bB.png')
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

        directions = ((-1, -1), (-1, 1), (1, -1), (1, 1))   # przekątne
        for d in directions:
            candidates = []
            for i in range(1, 8):   # max 7 pól
                end_column = self.column + d[1] * i
                end_row = self.row + d[0] * i
                if 0 < end_row <= 8 and 0 < end_column <= 8:
                    candidates.append((end_column, end_row))

            add_moves(candidates)

        return possible_moves
