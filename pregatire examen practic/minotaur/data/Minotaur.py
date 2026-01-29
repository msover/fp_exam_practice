from data.Gamepiece import Gamepiece
from data.Position import Position
from repo.TxtRepo import TxtRepo


class Minotaur(Gamepiece):
    def __init__(self, position: Position):
        super().__init__(position)