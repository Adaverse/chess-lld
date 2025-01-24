from chess.ChessPieces.ChessPiece import ChessPiece
from Position import Position
from ChessPieces.ChessObectColor import ChessObjectColor
from typing import Optional

class Cell:
    def __init__(self, color: ChessObjectColor, chessPiece: Optional[ChessPiece], position: Position):
        self.color: ChessObjectColor  = color
        self.chessPiece = chessPiece
        self.position = position
    
    def isFilled(self):
        return True if self.chessPiece is not None else False
