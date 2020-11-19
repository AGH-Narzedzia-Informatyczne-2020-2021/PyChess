from chess.pieces.Piece import Piece
from chess.constants import SQUARE_SIZE
from chess.Move import Move
import pygame as pg
import os


class Rook(Piece):

    def load_image(self):
        if self.is_white:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'wR.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'bR.png')
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

        add_moves([(self.column, row) for row in range(self.row + 1, 9)])               # pola w górę od wieży
        add_moves([(self.column, row) for row in range(self.row - 1, 0, -1)])           # pola w dół od wieży
        add_moves([(column, self.row) for column in range(self.column + 1, 9)])         # pola na prawo od wieży
        add_moves([(column, self.row) for column in range(self.column - 1, 0, -1)])     # pola na lewo od wieży

        return possible_moves
