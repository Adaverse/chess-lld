## Chess Low Level Design
This repository implements LLD patterns required for Chess game implementation.

The first pattern utilized is FACOTRY DEISGN PATTERN. The code snippet can be found in file `ChessPieces/ChessPiecesFactory.py`

```
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
```

and the driver code using it in file `Board.py`

```
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
```

This impolementation is simmpler version of Factory Design Pattern. Below is the UML diagram - 
<img width="818" alt="image" src="https://github.com/user-attachments/assets/85d78e2f-09bc-401c-a604-d0e427d7f6ba" />


