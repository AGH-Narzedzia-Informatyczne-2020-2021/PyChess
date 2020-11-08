import pygame as pg

from constants import WIDTH, HEIGHT, WINDOW_NAME, COLUMNS, ROWS, SQUARE_SIZE, BLACK, WHITE


class Board:
    def __init__(self):
        self.board = [[0 for i in range(COLUMNS)] for j in range(ROWS)]
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(WINDOW_NAME)

    def show(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                square = ((SQUARE_SIZE * i), (SQUARE_SIZE * j), (SQUARE_SIZE * (i + 1)), (SQUARE_SIZE * (j + 1)))
                if (i + j) % 2:
                    pg.draw.rect(self.window, BLACK, pg.Rect(square))
                else:
                    pg.draw.rect(self.window, WHITE, pg.Rect(square))
        pg.display.flip()


