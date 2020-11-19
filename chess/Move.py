class Move:
    def __init__(self, piece, column, row, captured_piece=None, rook_move=None):
        self.piece = piece
        self.pieces = piece.pieces
        self.column = column
        self.row = row
        self.captured_piece = captured_piece
        self.rook_move = rook_move
        self.previous_column = None
        self.previous_row = None

    def causes_self_check(self):
        self.do()
        result = self.pieces.is_checked(self.piece.is_white)
        self.undo()
        return result

    def do(self):
        self.previous_column = self.piece.column
        self.previous_row = self.piece.row
        self.piece.column = self.column
        self.piece.row = self.row
        if self.captured_piece is not None:
            self.pieces.remove(self.captured_piece)
        if self.rook_move is not None:
            self.previous_row.do()

    def undo(self):
        self.piece.column = self.previous_column
        self.piece.row = self.previous_row
        if self.captured_piece is not None:
            self.pieces.append(self.captured_piece)
        if self.rook_move is not None:
            self.previous_row.undo()