from data.Enums import LabyrinthEnum
from repo.TxtRepo import TxtRepo


class Position:
    def __init__(self, row, col, repo: TxtRepo):
        self._row = row
        self._col = col
        self._repo = repo

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value):
        self.validation(value, self._col)
        self._row = value

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, value):
        self.validation(self._row, value)
        self._col = value

    def validation(self, x, y):
        if x is None or y is None:
            return

        if self._repo.getLabyrinth()[x][y].labyrinth == LabyrinthEnum.WALL:
            raise ValueError(f"{x}, {y} is a wall")
