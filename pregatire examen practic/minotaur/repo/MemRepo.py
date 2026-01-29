from data.Enums import Direction, Turn
from data.Labyrinth import Labyrinth
from data.Movement import Movement


class MemRepo:
    def __init__(self):
        self._labyrinth: list[list[Labyrinth]] = []
        self._lastDirection = Direction.NONE
        self._lastMagnitude = 0
        self.turn = Turn.PLAYER

    def getLabyrinth(self) -> list[list[Labyrinth]]:
        return self._labyrinth

    def getLastMagnitude(self) -> int:
        return self._lastMagnitude

    def setLastMagnitude(self, magnitude: int):
        self._lastMagnitude = magnitude

