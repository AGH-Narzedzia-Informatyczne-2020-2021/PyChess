import pygame as pg


from chess.constants import WIDTH, HEIGHT, WINDOW_NAME, COLUMNS, ROWS, SQUARE_SIZE, BLACK, WHITE, RED
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
        self.basic_pieces_placer()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(WINDOW_NAME)
        self.turn = True  # True -> white Black ->False

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

    def basic_pieces_placer(self):
        self.pieces.append(King(1, 1, True, self.pieces))
        self.pieces.append(Rook(8, 1, True, self.pieces))
        self.pieces.append(King(1, 8, False, self.pieces))
        self.pieces.append(Rook(8, 8, False, self.pieces))

    def game(self):
        run = True
        while run:
            self.draw()
            move_waiting = False
            for event in pg.event.get():

                if event.type == pg.QUIT:
                    run = False
                    break

                if event.type == pg.MOUSEBUTTONDOWN:

                    col, row = clicked_square()
                    piece = self.pieces.get((col, row))
                    if piece is not None and self.turn == piece.is_white:
                        chosen_piece = piece
                        self.draw_possible_moves(piece.get_possible_moves())
                        move_waiting = True


            while move_waiting:
                for event in pg.event.get():

                    if event.type == pg.QUIT:
                        move_waiting = False
                        run = False
                        break

                    elif event.type == pg.MOUSEBUTTONDOWN:
                        col, row = clicked_square()
                        if chosen_piece.move(col, row):
                            self.change_turn()
                        move_waiting = False
        pg.quit()

    def draw_possible_moves(self, moves):
        for i in range(ROWS):
            for j in range(COLUMNS):
                for move in moves:
                    if (move.column, move.row) == coordinates_to_chess_tiles(i, j):
                        center = (int(SQUARE_SIZE * (i + 0.5)), int(SQUARE_SIZE * (j + 0.5)))
                        radius = SQUARE_SIZE // 4
                        pg.draw.circle(self.window, RED, center, radius)
        pg.display.flip()

    def change_turn(self):
        self.turn = not self.turn


board = Board()
board.game()
