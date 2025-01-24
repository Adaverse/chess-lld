from abc import abstractmethod

from chess.ChessPieces.ChessObectColor import ChessObjectColor
from Position import Position
from ChessPieceType import ChessPieceType

class ChessPiece:
    def __init__(self, name: ChessPieceType, color: ChessObjectColor, isAlive: bool):
        self.name: ChessPieceType = name
        self.type: ChessObjectColor = color
        self.isAlive: bool = isAlive
    
    @abstractmethod
    def canMove(position: Position) -> bool:
        ...
