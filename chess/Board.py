import sys
import time

import pygame as pg

from chess.pieces.Knight import Knight
from chess.pieces.Pawn import Pawn
from chess.constants import WIDTH, HEIGHT, WINDOW_NAME, COLUMNS, ROWS, SQUARE_SIZE, BLACK, WHITE
from chess.pieces.Pieces import Pieces
from chess.pieces.Rook import Rook


class Board:
    def __init__(self):
        self.pieces = Pieces()
        self.basic_pieces_placer()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(WINDOW_NAME)

    def coordinates_to_chess_tiles(self, x, y):
        return x + 1, 8 - y


    def draw(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                square = (SQUARE_SIZE * i, SQUARE_SIZE * j, SQUARE_SIZE, SQUARE_SIZE)
                #print(square)
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




board = Board()
print(board.pieces[0], board.pieces[0].image)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)

    board.draw()
    board.pieces[0].move(board.pieces[0].column, board.pieces[0].row+1)
    time.sleep(1)
