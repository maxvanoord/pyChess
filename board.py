from Pieces.pawn import Pawn

class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.board = self.newGame()

    def newGame(self):
        board = [[0]*self.width for _ in range(self.height)]

        # Pawns
        for col in range(self.width):
            board[1][col] = Pawn("white", 1, col)
            board[self.height - 2][col] = Pawn("black", self.height - 2, col)

        return board

    def print(self):
        print()
        print("+-----------+")
        for row in self.board:
            for piece in row:
                print("unicode")

b = Board()
print(b.board)
print(u"\u25FC")