from enum import Enum


class LabyrinthEnum(Enum):
    WALL = "# "
    OPEN = "  "
    EXIT = "- "
class GamepieceEnum(Enum):
    ALICE = "A "
    MINOTAUR = "M "
    NONE = None

class Direction(Enum):
    UP = "U"
    DOWN = "D"
    LEFT = "L"
    RIGHT = "R"
    NONE = None

class Turn(Enum):
    PLAYER = "P"
    COMPUTER = "C"

class Gamestate(Enum):
    WIN = "WIN"
    LOSE = "LOSE"
    IDLE = "IDLE"