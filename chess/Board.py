import os
import sys
import time

import pygame as pg

from chess.pieces.King import King
from chess.pieces.Knight import Knight
from chess.pieces.Pawn import Pawn
from chess.constants import WIDTH, HEIGHT, WINDOW_NAME, COLUMNS, ROWS, SQUARE_SIZE, BLACK, WHITE, RED
from chess.pieces.Pieces import Pieces
from chess.pieces.Rook import Rook


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


class Board:
    def __init__(self):
        self.pieces = Pieces()
        self.basic_pieces_placer()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(WINDOW_NAME)
        self.turn = True  # True -> white Black ->False

    def coordinates_to_chess_tiles(self, x, y):
        return x + 1, 8 - y

    def draw(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                square = (SQUARE_SIZE * i, SQUARE_SIZE * j, SQUARE_SIZE, SQUARE_SIZE)

                if (i + j) % 2:
                    pg.draw.rect(self.window, BLACK, pg.Rect(square))
                else:
                    pg.draw.rect(self.window, WHITE, pg.Rect(square))

                # figury
                for piece in self.pieces:
                    if self.coordinates_to_chess_tiles(i, j) == (piece.column, piece.row):
                        self.window.blit(piece.image, square)
        pg.display.flip()

    def basic_pieces_placer(self):
        self.pieces.append(Rook(1, 1, True, self.pieces))
        self.pieces.append(Rook(8, 1, True, self.pieces))
        self.pieces.append(Rook(1, 8, False, self.pieces))
        self.pieces.append(Rook(8, 8, False, self.pieces))
        for i in range(1, 9):
            self.pieces.append(Pawn(i, 2, True, self.pieces))
            self.pieces.append(Pawn(i, 7, False, self.pieces))
        self.pieces.append(Knight(2, 1, True, self.pieces))
        self.pieces.append(Knight(7, 1, True, self.pieces))
        self.pieces.append(Knight(2, 8, False, self.pieces))
        self.pieces.append(Knight(7, 8, False, self.pieces))
        self.pieces.append(King(5, 1, True, self.pieces))
        self.pieces.append(King(5, 8, False, self.pieces))


    def game(self):
        run = True
        while run:
            self.draw()
            move_waiting = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    row, col = self.coordinates_to_chess_tiles(col, row)
                    for piece in self.pieces:
                        if (row, col) == (piece.column, piece.row) and self.turn == piece.is_white:
                            chosen_piece = piece
                            self.draw_possible_moves(piece.get_legal_moves())
                            move_waiting = True

            while move_waiting:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        move_waiting = False
                        run = False
                    elif event.type == pg.MOUSEBUTTONDOWN:
                        pos = pg.mouse.get_pos()
                        row, col = get_row_col_from_mouse(pos)
                        row, col = self.coordinates_to_chess_tiles(col, row)
                        move_done = chosen_piece.move(row, col)
                        if move_done:
                            self.turn = not self.turn
                        move_waiting = False

        pg.quit()

    def draw_possible_moves(self, moves):
        for i in range(ROWS):
            for j in range(COLUMNS):
                for move in moves:
                    if (move.column, move.row) == self.coordinates_to_chess_tiles(i, j):
                        center = (int(SQUARE_SIZE * (i + 0.5)), int(SQUARE_SIZE * (j + 0.5)))
                        radius = SQUARE_SIZE // 4
                        pg.draw.circle(self.window, RED, center, radius)
        pg.display.flip()


board = Board()
board.game()
