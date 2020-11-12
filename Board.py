import sys

import pygame as pg

from Pawn import Pawn
from constants import WIDTH, HEIGHT, WINDOW_NAME, COLUMNS, ROWS, SQUARE_SIZE, BLACK, WHITE

class Board:
    def __init__(self):
        self.pieces = [[None for i in range(COLUMNS)] for j in range(ROWS)]
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.reset_board()
        pg.display.set_caption(WINDOW_NAME)

    def show(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                square = ((SQUARE_SIZE * j), (SQUARE_SIZE * i), (SQUARE_SIZE * (j + 1)), (SQUARE_SIZE * (i + 1)))
                print(square)
                if (i + j) % 2:
                    pg.draw.rect(self.window, BLACK, pg.Rect(square))
                else:
                    pg.draw.rect(self.window, WHITE, pg.Rect(square))

                if self.pieces[i][j] is not None:
                    self.window.blit(self.pieces[i][j].image, square)
        pg.display.flip()

    def reset_board(self):
        for i in range(COLUMNS):
            self.pieces[1][i] = Pawn(1, i, BLACK)
            self.pieces[6][i] = Pawn(6, i, WHITE)


board = Board()
while 1:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit(0)
    board.show()
