from Position import Position

class MoveStrategy:    
    def move(self, source: Position, target: Position) -> bool:
        raise NotImplementedError