
class Pawn:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.firstMove = True
        self.justTwoStepped = False

    def moves(self, board):
        moves = []
        if self.color == "white":
            if self.row < len(board) - 1:
                if board[self.row + 1][self.col] is None:
                    moves.append((self.row + 1, self.col))
            if self.firstMove:
                if board[self.row + 2][self.col] is None:
                    moves.append((self.row + 2, self.col))
        elif self.color == "black":
            if self.row > 0:
                if board[self.row - 1][self.col] is None:
                    moves.append((self.row - 1, self.col))
            if self.firstMove:
                if board[self.row - 2][self.col] is None:
                    moves.append((self.row - 2, self.col))

        return moves

    def strikes(self, board):
        strikes = []
        if self.color == "white":
            if self.col > 0:
                if type(board[self.row + 1][self.col - 1]) != 0 and board[self.row + 1][self.col - 1].color == "black":
                    strikes.append((self.row + 1, self.col - 1))
                if type(board[self.row][self.col - 1]) == Pawn and board[self.row][self.col - 1].justTwoStepped:
                    strikes.append((self.row, self.col - 1))
            if self.col < len(board) - 1:
                if type(board[self.row + 1][self.col + 1]) != 0 and board[self.row + 1][self.col + 1].color == "black":
                    strikes.append((self.row + 1, self.col + 1))
                if type(board[self.row][self.col + 1]) == Pawn and board[self.row][self.col + 1].justTwoStepped:
                    strikes.append((self.row, self.col + 1))

        return strikes