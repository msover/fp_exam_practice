from data.PositionState import PositionState


class Position:
    def __init__(self, number: int, letter: str, state: PositionState = PositionState.EMPTY):
        self.number = number
        self.letter = letter
        self.state = state
        self.validate()

    def validate(self):
        if self.number < 0 or self.number > 5:
            raise ValueError("Position out of bounds")
        if self.letter < "A" or self.letter > "F":
            raise ValueError("Position out of bounds")

    def __eq__(self, other):
        return self.number == other.number and self.letter == other.letter