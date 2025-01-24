from ChessPiece import ChessPiece
from ChessObectColor import ChessPieceColor
from ChessPieceType import ChessPieceType

from King import King
from Queen import Queen
from Knight import Knight
from Pawn import Pawn
from Rookie import Rookie
from Bishop import Bishop

class ChessPieceFacotory:
    
    @staticmethod
    def createChessPiece(color: ChessPieceColor, chessPieceType: ChessPieceType) -> ChessPiece:
        if chessPieceType == ChessPieceType.KING:
            return King(chessPieceType, color)
        elif chessPieceType == ChessPieceType.QUEEN:
            return Queen(chessPieceType, color)
        elif chessPieceType == ChessPieceType.KNIGHT:
            return Knight(chessPieceType, color)
        elif chessPieceType == ChessPieceType.PAWN:
            return Pawn(chessPieceType, color)
        elif chessPieceType == ChessPieceType.ROOKIE:
            return Rookie(chessPieceType, color)
        elif chessPieceType == ChessPieceType.BISHOP:
            return Bishop(chessPieceType, color)
        else:
            raise Exception("Not a valid chess piece type!")
