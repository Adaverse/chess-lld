from Board import Board
from GameStatus import GameStatus
from Player import Player
from Position import Position

class Game:
    def __init__(self, player1: Player, player2: Player, board = Board(), gameStatus: GameStatus = GameStatus.YTS):
        self.board = board
        self.status = gameStatus
        self.player1 = player1 # player1 is alway white side
        self.player2 = player2 # player2 is always black side
        self.nextTurn = None
        
    def initialize(self):
        self.board.initialize()
        self.status = GameStatus.YTS
        
    def run(self):
        while(self.status not in [GameStatus.FINISHED, GameStatus.FORFIETED]):
            nextPlayer = self.getNextPlayer()
            # TODO: Print the board
            # get current and target position
            curPos, targetPos = self.getNextMove(nextPlayer)
            ...
    
    def getNextPlayer(self) -> Player:
        if self.nextTurn is None:
            return self.player1
        if self.nextTurn is self.player1:
            return self.player2
        else:
            return self.player1
        
    def getNextMove(self, player: Player) -> list[Position]:
        '''
            it return current position and target position
        '''
        ...
    
    def printBoard(self):
        ...