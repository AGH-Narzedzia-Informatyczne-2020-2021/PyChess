class Move:
    def __init__(self, piece, column, row, captured_piece=None, rook_move=None):
        self.piece = piece
        self.column = column
        self.row = row
        self.captured_piece = captured_piece
        self.rook_move = rook_move
        self.previous_column = None
        self.previous_row = None

    def do(self, pieces):
        self.previous_column = self.piece.column
        self.previous_row = self.piece.row
        self.piece.column = self.column
        self.piece.row = self.row
        if self.captured_piece is not None:
            pieces.remove(self.captured_piece)
        if self.rook_move is not None:
            self.previous_row.do()

    def undo(self):
        self.piece.column = self.previous_column
        self.piece.row = self.previous_row
        if self.captured_piece is not None:
            self.pieces.append(self.captured_piece)
        if self.rook_move is not None:
            self.previous_row.undo()
