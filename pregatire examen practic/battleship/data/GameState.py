from enum import Enum


class GameState(Enum):
    IDLE = "IDLE"
    WIN = "WIN"
    LOSE = "LOSE"