from data.Position import Position
from data.PositionState import PositionState


class Ship:
    def __init__(self, pos1: Position, pos2: Position, pos3: Position):
        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3
        self.pos1.state = PositionState.OCCUPIED
        self.pos2.state = PositionState.OCCUPIED
        self.pos3.state = PositionState.OCCUPIED
        self.validate()

    def validate(self):
        if self.pos1.letter == self.pos2.letter and self.pos2.letter == self.pos3.letter:
            if abs(self.pos1.number - self.pos2.number) != 1 or abs(self.pos3.number - self.pos2.number) != 1:
                raise ValueError("Invalid ship construction")
            else:
                return
        if self.pos1.number == self.pos2.number and self.pos3.number == self.pos2.number:
            if abs(ord(self.pos1.letter) - ord(self.pos2.letter)) != 1 or abs(ord(self.pos3.letter) - ord(self.pos2.letter)) != 1:
                raise ValueError("Invalid ship construction")
            else:
                return
        raise ValueError("Invalid ship construction")
