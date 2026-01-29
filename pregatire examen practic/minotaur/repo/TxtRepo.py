from data.Enums import LabyrinthEnum, GamepieceEnum
from data.Labyrinth import Labyrinth
from repo.MemRepo import MemRepo


class TxtRepo(MemRepo):
    def __init__(self):
        super().__init__()

    def readfile(self):
        self._labyrinth = []
        with open("labirint.txt", "r") as file:
            linecount = 0
            for line in file:
                row = []
                for char in line:
                    if char == "0":
                        row.append(Labyrinth(LabyrinthEnum.OPEN, GamepieceEnum.NONE))
                    if char == "1":
                        row.append(Labyrinth(LabyrinthEnum.WALL, GamepieceEnum.NONE))
                    if char == "9":
                        row.append(Labyrinth(LabyrinthEnum.EXIT, GamepieceEnum.NONE))
                if row:
                    self._labyrinth.append(row)
                else:
                    return
                linecount += 1