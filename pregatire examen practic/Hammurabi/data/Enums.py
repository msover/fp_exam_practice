from enum import Enum


class Gamestate(Enum):
    IDLE = "idle"
    LOSE = "lose"
    WIN = "win"