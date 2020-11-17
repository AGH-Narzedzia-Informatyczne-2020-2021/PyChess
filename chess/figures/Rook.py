from chess.figures.Figure import Figure
from chess.constants import SQUARE_SIZE
import pygame as pg


class Rook(Figure):

    def load_image(self):
        if self.is_white:
            self.image = pg.transform.scale(pg.image.load('chess/figures_graphics/wR.png'), (SQUARE_SIZE, SQUARE_SIZE))
        else:
            self.image = pg.transform.scale(pg.image.load('chess/figures_graphics/bR.png'), (SQUARE_SIZE, SQUARE_SIZE))

    def get_possible_moves(self):

        possible_moves = []

        def add_moves(candidates_for_moves):

            for move in candidates_for_moves:
                figure = self.figures.get(move)

                if figure is None:
                    possible_moves.append(move)
                elif figure.is_white != self.is_white:
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
            figure = self.figures.get(move)
            if figure is not None:
                possible_captures.append(move, figure)

        return possible_captures
