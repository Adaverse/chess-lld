from ChessPiece import ChessPiece
from ChessObectColor import ChessPieceColor
from ChessPieceType import ChessPieceType

from King import King
from Queen import Queen
from Knight import Knight
from Pawn import Pawn
from Rookie import Rookie
from Bishop import Bishop

from chess.MoveStrategies.KingMoveStrategy import KingMoveStrategy
from chess.MoveStrategies.QueenMoveStrategy import QueenMoveStrategy
from chess.MoveStrategies.KnightMoveStrategy import KnightMoveStrategy
from chess.MoveStrategies.PawnMoveStrategy import PawnMoveStrategy
from chess.MoveStrategies.RookieMoveStrategy import RookieMoveStrategy
from chess.MoveStrategies.BishopMoveStrategy import BishopMoveStrategy

class ChessPieceFacotory:
    
    @staticmethod
    def createChessPiece(color: ChessPieceColor, chessPieceType: ChessPieceType) -> ChessPiece:
        if chessPieceType == ChessPieceType.KING:
            return King(chessPieceType, color, KingMoveStrategy())
        elif chessPieceType == ChessPieceType.QUEEN:
            return Queen(chessPieceType, color, QueenMoveStrategy())
        elif chessPieceType == ChessPieceType.KNIGHT:
            return Knight(chessPieceType, color, KnightMoveStrategy())
        elif chessPieceType == ChessPieceType.PAWN:
            return Pawn(chessPieceType, color, PawnMoveStrategy())
        elif chessPieceType == ChessPieceType.ROOKIE:
            return Rookie(chessPieceType, color, RookieMoveStrategy())
        elif chessPieceType == ChessPieceType.BISHOP:
            return Bishop(chessPieceType, color, BishopMoveStrategy())
        else:
            raise Exception("Not a valid chess piece type!")
