from abc import abstractmethod

from chess.ChessPieces.ChessObectColor import ChessObjectColor
from Position import Position
from ChessPieceType import ChessPieceType
from chess.MoveStrategies import MoveStrategy

class ChessPiece:
    def __init__(self, name: ChessPieceType, color: ChessObjectColor, isAlive: bool, moveStrategy: MoveStrategy):
        self.name: ChessPieceType = name
        self.type: ChessObjectColor = color
        self.isAlive: bool = isAlive
        self.moveStrategy: MoveStrategy = moveStrategy
    
    @abstractmethod
    def canMove(position: Position) -> bool:
        ...
