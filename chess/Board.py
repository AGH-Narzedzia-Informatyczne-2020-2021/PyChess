

import pygame as pg

from chess.figures.Knight import Knight
from chess.figures.Pawn import Pawn
from chess.constants import WIDTH, HEIGHT, WINDOW_NAME, COLUMNS, ROWS, SQUARE_SIZE, BLACK, WHITE


class Board:
    def __init__(self):
        self.pieces = [[None for i in range(COLUMNS)] for j in range(ROWS)]
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.reset_board()
        self.list_of_moves = [] #tuple (type of figure, moved to where)
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

    #stawianie figur
    def reset_board(self):
        #pionki
        for i in range(COLUMNS):
            self.pieces[1][i] = Pawn(BLACK)
            self.pieces[6][i] = Pawn(WHITE)
        #konie
        self.pieces[0][1] = Knight(BLACK)
        self.pieces[0][6] = Knight(BLACK)
        self.pieces[7][1] = Knight(WHITE)
        self.pieces[7][6] = Knight(WHITE)


    def move_piece(self, start_pos, end_pos):
        piece = self.pieces[start_pos[0]][start_pos[1]]
        self.pieces[start_pos[0]][start_pos[1]] = None
        self.pieces[end_pos[0]][end_pos[1]] = piece


