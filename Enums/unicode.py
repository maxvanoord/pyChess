from Enums.colors import Color
from Pieces.bishop import Bishop
from Pieces.king import King
from Pieces.knight import Knight
from Pieces.pawn import Pawn
from Pieces.queen import Queen
from Pieces.rook import Rook

class Unicode:
    chrs = {
        (Color.WHITE, None): "\u25FB",
        (Color.WHITE, Pawn): "\u265F",
        (Color.WHITE, Rook): "\u265C",
        (Color.WHITE, Knight): "\u265E",
        (Color.WHITE, Bishop): "\u265D",
        (Color.WHITE, King): "\u265A",
        (Color.WHITE, Queen): "\u265B",
        (Color.BLACK, None): "\u25FC",
        (Color.BLACK, Pawn): "\u2659",
        (Color.BLACK, Rook): "\u2656",
        (Color.BLACK, Knight): "\u2658",
        (Color.BLACK, Bishop): "\u2657",
        (Color.BLACK, King): "\u2654",
        (Color.BLACK, Queen): "\u2655"
    }