from data.Enums import Direction


class Movement:
    def __init__(self, direction: Direction | None = None, magnitude: int = 1):
        self.direction = direction
        self.magnitude = magnitude