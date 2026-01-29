from enum import Enum


class PositionState(Enum):
    EMPTY = '.'
    OCCUPIED = '#'
    MISS = 'O'
    HIT = 'X'