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

        if self.is_white:
            if self.row==2:
                add_moves([(self.column, self.row + 2)]) #Pozycja startowa
                add_moves([(self.column, self.row + 1)])
            add_moves([(self.column, self.row + 1)])
        else:
            if self.row==7:
                add_moves([(self.column, self.row - 2)])
                add_moves([(self.column, self.row - 1)])
            add_moves([(self.column, self.row + -1)])


        return possible_moves