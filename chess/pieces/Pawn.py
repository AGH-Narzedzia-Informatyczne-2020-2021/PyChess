from chess.pieces.Piece import Piece
from chess.pieces.Queen import Queen
from chess.constants import SQUARE_SIZE
from chess.Move import Move
import pygame as pg
import os

queen = None


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

        candidates_for_moves = []

        candidate = (self.column, self.row + (1 if self.is_white else -1))

        if self.pieces.get(candidate) is None:
            possible_moves.append(Move(self, candidate[0], candidate[1]))
            if self.row == 2 if self.is_white else 7:
                candidate = (self.column, self.row + (2 if self.is_white else -2))
                if self.pieces.get(candidate) is None:
                    if candidate[1] == (8 if self.is_white else 1):
                        possible_moves.append(Move(self, candidate[0], candidate[1], pawn_promotion=True))
                    else:
                        possible_moves.append(Move(self, candidate[0], candidate[1]))

        candidates = [(self.column + change, self.row + (1 if self.is_white else -1)) for change in [1, -1]]

        for candidate in candidates:
            if candidate[0] in range(1, 9) and candidate[1] in range(1, 9):
                captured_piece = self.pieces.get(candidate)
                if captured_piece is not None and captured_piece.is_white != self.is_white:
                    if candidate[1] == (8 if self.is_white else 1):
                        possible_moves.append(Move(self, candidate[0], candidate[1], captured_piece, pawn_promotion=True))
                    else:
                        possible_moves.append(Move(self, candidate[0], candidate[1], captured_piece))

        return possible_moves

    def promote(self):
        global queen
        queen = Queen(self.column, self.row, self.is_white, self.pieces)
        self.pieces.append(queen)
        self.pieces.remove(self)

    def unpromote(self):
        global queen
        if queen in self.pieces:
            self.pieces.remove(queen)
        self.pieces.append(self)

