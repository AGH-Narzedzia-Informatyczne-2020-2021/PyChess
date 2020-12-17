import pygame as pg

from chess.constants import WIDTH, HEIGHT, WINDOW_NAME, COLUMNS, ROWS, SQUARE_SIZE, BLACK, WHITE, HIGHLIGHT
from chess.pieces.King import King
from chess.pieces.Knight import Knight
from chess.pieces.Pawn import Pawn

from chess.pieces.Pieces import Pieces
from chess.pieces.Rook import Rook


def get_col_row_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return col, row


def clicked_square():
    pos = pg.mouse.get_pos()
    col, row = get_col_row_from_mouse(pos)
    col, row = coordinates_to_chess_tiles(col, row)
    return col, row


def coordinates_to_chess_tiles(col, row):
    return col + 1, 8 - row


class Board:
    def __init__(self):
        self.pieces = Pieces()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(WINDOW_NAME)
        self.turn = True  # True -> white Black ->False
        self.global_run = True

    def draw(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                square = (SQUARE_SIZE * i, SQUARE_SIZE * j, SQUARE_SIZE, SQUARE_SIZE)

                if (i + j) % 2:
                    pg.draw.rect(self.window, BLACK, pg.Rect(square))
                else:
                    pg.draw.rect(self.window, WHITE, pg.Rect(square))

                # figury
                piece = self.pieces.get(coordinates_to_chess_tiles(i, j))
                if piece is not None:
                    self.window.blit(piece.image, square)
        pg.display.flip()

    def game(self):
        while self.pieces.end_of_the_game(self.turn) is None and self.global_run:
            move_waiting = False
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    self.global_run = False
                    break

                if event.type == pg.MOUSEBUTTONDOWN:

                    col, row = clicked_square()
                    piece = self.pieces.get((col, row))
                    if piece is not None and self.turn == piece.is_white:
                        chosen_piece = piece
                        self.draw_possible_moves(piece.get_legal_moves())
                        move_waiting = True

            while move_waiting:
                for event in pg.event.get():

                    if event.type == pg.QUIT:
                        move_waiting = False
                        self.global_run = False
                        break

                    elif event.type == pg.MOUSEBUTTONDOWN:
                        col, row = clicked_square()
                        if chosen_piece.move(col, row):
                            self.change_turn()
                        move_waiting = False

            self.draw()

        return self.pieces.end_of_the_game(self.turn)

    def draw_possible_moves(self, moves):
        for i in range(ROWS):
            for j in range(COLUMNS):
                for move in moves:
                    if (move.column, move.row) == coordinates_to_chess_tiles(i, j):
                        center = (int(SQUARE_SIZE * (i + 0.5)), int(SQUARE_SIZE * (j + 0.5)))
                        radius = SQUARE_SIZE // 4
                        pg.draw.circle(self.window, HIGHLIGHT, center, radius)
        pg.display.flip()

    def change_turn(self):
        self.turn = not self.turn

    def highlight_king(self, color):
        king = self.pieces.get_king(color)
        x, y = king.column, king.row
        square = (SQUARE_SIZE * (x - 1), SQUARE_SIZE * (8-y), SQUARE_SIZE, SQUARE_SIZE)
        line1, line2 = self.square_to_cross(square)
        pg.draw.line(self.window, (255, 0, 0), line1[0:2], line1[2:4], SQUARE_SIZE // 10)
        pg.draw.line(self.window, (255, 0, 0), line2[0:2], line2[2:4], SQUARE_SIZE // 10)
        pg.display.flip()

    def after_game_screen(self, result):
        if result is not None:
            if result == 2:
                self.highlight_king(0)
                self.highlight_king(1)
            else:
                lost = not result
                self.highlight_king(lost)
            #pg.time.delay(5000)

    def square_to_cross(self, square):
        first_line = (square[0], square[1], square[0] + SQUARE_SIZE, square[1] + SQUARE_SIZE)
        second_line = (square[0], square[1] + SQUARE_SIZE, square[0] + SQUARE_SIZE, square[1])
        return first_line, second_line

    def reset_board(self):
        self.pieces = Pieces()
        self.turn = True

    def main_app(self):
        while self.global_run:
            self.after_game_screen(self.game())
            self.reset_board()
        pg.quit()


board = Board()
board.main_app()
