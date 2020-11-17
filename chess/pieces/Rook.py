from chess.pieces.Piece import Piece
from chess.constants import SQUARE_SIZE
import pygame as pg
import os

class Rook(Piece):

    def load_image(self):
        if self.is_white:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'bR.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'wR.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))

    def get_possible_moves(self):

        possible_moves = []

        def add_moves(candidates_for_moves):

            for move in candidates_for_moves:
                piece = self.pieces.get(move)

                if piece is None:
                    possible_moves.append(move)
                elif piece.is_white != self.is_white:
                    possible_moves.append(move)
                    return
                else:
                    return

        add_moves([(self.column, row) for row in range(self.row + 1, 9)])               # pola w górę od wieży
        add_moves([(self.column, row) for row in range(self.row - 1, 0, -1)])           # pola w dół od wieży
        add_moves([(column, self.row) for column in range(self.column + 1, 9)])         # pola na prawo od wieży
        add_moves([(column, self.row) for column in range(self.column - 1, 0, -1)])     # pola na lewo od wieży

        return possible_moves

    def get_possible_captures(self):

        possible_captures = []

        for move in self.get_possible_moves():
            piece = self.pieces.get(move)
            if piece is not None:
                possible_captures.append((move, piece))

        return possible_captures
