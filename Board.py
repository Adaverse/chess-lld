from Cell import Cell
from chess.ChessPieces.ChessPiecesFactory import ChessPieceFacotory
from chess.ChessPieces.ChessPieceType import ChessPieceType
from chess.ChessPieces.ChessObectColor import ChessObjectColor

from Position import Position

class Board:
    def __init__(self):
        self.cells: list[Cell] = [None for i in range(64)]
    
    def initialize(self):
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        currentCellColor = ChessObjectColor.BLACK
                    else:
                        currentCellColor = ChessObjectColor.WHITE
                else:
                    if j % 2 == 0:
                        currentCellColor = ChessObjectColor.WHITE
                    else:
                        currentCellColor = ChessObjectColor.BLACK
                currentPosition = Position(i, j)
                self.cells[self.getFlatCoords(i, j)] = Cell(currentCellColor, None, currentPosition)
        
        # Below is full factory design pattern
        #   factory design pattern we need
        #   1. Object that we want to create (Product)
        #   2. Product interfaace
        #   3. Factory interface
        #   4. Factory implementation
        
        # builder design pattern
        
        # 8 white and black pawns
        for i, chessObjectType in [(1, ChessObjectColor.BLACK), (6, ChessObjectColor.WHITE)]:
            for j in range(8):
                self.cells[self.getFlatCoords(i, j)] = ChessPieceFacotory.createChessPiece(chessObjectType, ChessPieceType.PAWN)
        
        for i, chessObjectType in [(0, ChessObjectColor.BLACK), (7, ChessObjectColor.WHITE)]:
            for j in [0,7]:
                self.cells[self.getFlatCoords(i, j)] = ChessPieceFacotory.createChessPiece(chessObjectType, ChessPieceType.ROOKIE)
        
            for j in [1, 6]:
                self.cells[self.getFlatCoords(i, j)] = ChessPieceFacotory.createChessPiece(chessObjectType, ChessPieceType.BISHOP)

            for j in [2, 5]:
                self.cells[self.getFlatCoords(i, j)] = ChessPieceFacotory.createChessPiece(chessObjectType, ChessPieceType.KNIGHT)
                
            self.cells[self.getFlatCoords(i, 3)] = ChessPieceFacotory.createChessPiece(chessObjectType, ChessPieceType.KING)
            self.cells[self.getFlatCoords(i, 4)] = ChessPieceFacotory.createChessPiece(chessObjectType, ChessPieceType.KING)

        
    def getFlatCoords(self, x, y):
        return x*8 + y
    
    def reset(self):
        ...