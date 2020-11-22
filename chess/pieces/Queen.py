import pygame as pg
import os

from chess.pieces.Piece import Piece
from chess.Move import Move
from chess.constants import SQUARE_SIZE
from chess.pieces.Rook import Rook
from chess.pieces.Bishop import Bishop


class Queen(Piece):

    def load_image(self):
        if self.is_white:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'wQ.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            path = os.path.join(os.getcwd(), 'pieces_graphics', 'bQ.png')
            self.image = pg.transform.scale(pg.image.load(path), (SQUARE_SIZE, SQUARE_SIZE))

    def get_possible_moves(self):
        rook = Rook(self.column, self.row, self.is_white, self.pieces)
        bishop = Bishop(self.column, self.row, self.is_white, self.pieces)
        possible_moves = []
        possible_moves.extend(rook.get_possible_moves())
        possible_moves.extend(bishop.get_possible_moves())
        for move in possible_moves:
            move.piece = self
        return possible_moves
