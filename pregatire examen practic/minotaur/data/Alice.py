from data.Gamepiece import Gamepiece
from data.Position import Position


class Alice(Gamepiece):
    def __init__(self, position: Position):
        super().__init__(position)