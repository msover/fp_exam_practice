import random

from data.Alice import Alice
from data.Enums import Direction, LabyrinthEnum
from data.Labyrinth import Labyrinth
from data.Minotaur import Minotaur
from data.Movement import Movement


class Bot:
    def __init__(self, service):
        self.service = service

    def checkForAlice(self) -> Direction:
        alice: Alice = self.service.alice
        minotaur: Minotaur = self.service.minotaur
        labyrinth: list[list[Labyrinth]] = self.service.repo.getLabyrinth()
        if alice.pos.row == minotaur.pos.row:
            obstruction = False
            startCheck = alice.pos.col
            finishCheck = minotaur.pos.col
            if startCheck > finishCheck:
                startCheck, finishCheck = finishCheck, startCheck
            for col in range(startCheck, finishCheck + 1):
                if labyrinth[alice.pos.row][col].labyrinth == LabyrinthEnum.WALL:
                    obstruction = True
            if not obstruction:
                if alice.pos.col < minotaur.pos.col:
                    return Direction.LEFT
                return Direction.RIGHT
        elif alice.pos.col == minotaur.pos.col:
            obstruction = False
            startCheck = alice.pos.row
            finishCheck = minotaur.pos.row
            if startCheck > finishCheck:
                startCheck, finishCheck = finishCheck, startCheck
            for row in range(startCheck, finishCheck + 1):
                if labyrinth[row][alice.pos.col].labyrinth == LabyrinthEnum.WALL:
                    obstruction = True
            if not obstruction:
                if alice.pos.col < minotaur.pos.col:
                    return Direction.DOWN
                return Direction.UP
        return Direction.NONE

    def chooseDirection(self) -> Direction:
        if self.checkForAlice().value is None:
            directionList = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
            return random.choice(directionList)
        return self.checkForAlice()

    def issueCommand(self):
        magnitude: int = self.service.repo.getLastMagnitude()
        direction = self.chooseDirection()
        while magnitude > 0:
            errorString = self.service.move(self.service.minotaur, Movement(direction))
            if errorString != "":
                direction = self.chooseDirection()
                magnitude += 1
            magnitude -= 1