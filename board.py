from Enums.colors import Color
from Enums.unicode import Unicode
from Pieces.bishop import Bishop
from Pieces.king import King
from Pieces.knight import Knight
from Pieces.pawn import Pawn
from Pieces.queen import Queen
from Pieces.rook import Rook

# noinspection PyTypeChecker
class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.board = self.newGame()

    def newGame(self):
        board = [[None]*self.width for _ in range(self.height)]

        # White
        board[0][0] = Rook(Color.WHITE, 0, 0)
        board[0][1] = Knight(Color.WHITE, 0, 1)
        board[0][2] = Bishop(Color.WHITE, 0, 2)
        board[0][3] = Queen(Color.WHITE, 0, 3)
        board[0][4] = King(Color.WHITE, 0, 4)
        board[0][5] = Bishop(Color.WHITE, 0, 5)
        board[0][6] = Knight(Color.WHITE, 0, 6)
        board[0][7] = Rook(Color.WHITE, 0, 7)
        for col in range(self.width):
            board[1][col] = Pawn(Color.WHITE, 1, col)

        # Black
        for col in range(self.width):
            board[self.height - 2][col] = Pawn(Color.BLACK, self.height - 2, col)
        board[7][0] = Rook(Color.BLACK, 7, 0)
        board[7][1] = Knight(Color.BLACK, 7, 1)
        board[7][2] = Bishop(Color.BLACK, 7, 2)
        board[7][3] = Queen(Color.BLACK, 7, 3)
        board[7][4] = King(Color.BLACK, 7, 4)
        board[7][5] = Bishop(Color.BLACK, 7, 5)
        board[7][6] = Knight(Color.BLACK, 7, 6)
        board[7][7] = Rook(Color.BLACK, 7, 7)

        return board

    def print(self):
        for row in self.board:
            pRow = []
            for place in row:
                if place is not None:
                    pRow.append(Unicode.chrs[(place.color, place.__class__)])
            print(pRow)

b = Board()
b.newGame()
b.print()
