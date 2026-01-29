import copy
import random

from data.Alice import Alice
from data.Enums import GamepieceEnum, Direction, Turn, Gamestate, LabyrinthEnum
from data.Gamepiece import Gamepiece

from data.Minotaur import Minotaur
from data.Movement import Movement
from data.Position import Position
from repo.TxtRepo import TxtRepo


class Service:
    def __init__(self, repo: TxtRepo):
        self.repo = repo
        self.repo.readfile()
        self.alice = Alice(Position(None, None, self.repo))
        self.minotaur = Minotaur(Position(None, None, self.repo))

    def setGamepieces(self):
        while self.alice.pos.row is None or self.alice.pos.col is None:
            self.alice.pos.row = None
            self.alice.pos.col = None
            try:
                pos = Position(random.randint(1, 9), 1, self.repo)
                self.alice.pos.row = pos.row
                self.alice.pos.col = pos.col
            except ValueError:
                continue

        while self.minotaur.pos.row is None or self.minotaur.pos.col is None:
            self.minotaur.pos.row = None
            self.minotaur.pos.col = None
            try:
                pos = Position(random.randint(1, 9), 9, self.repo)
                self.minotaur.pos.row = pos.row
                self.minotaur.pos.col = pos.col
            except ValueError:
                continue


    def updateLabyrinth(self):
        for row in range(len(self.repo.getLabyrinth()) - 1):
            for col in range(len(self.repo.getLabyrinth()) - 1):
                if self.repo.getLabyrinth()[row][col].gamepiece == GamepieceEnum.ALICE:
                    if self.alice.pos.row != row or self.alice.pos.col != col:
                        self.repo.getLabyrinth()[row][col].gamepiece = GamepieceEnum.NONE
                if self.repo.getLabyrinth()[row][col].gamepiece == GamepieceEnum.MINOTAUR:
                    if self.minotaur.pos.row != row or self.minotaur.pos.col != col:
                        self.repo.getLabyrinth()[row][col].gamepiece = GamepieceEnum.NONE
        self.repo.getLabyrinth()[self.alice.pos.row][self.alice.pos.col].gamepiece = GamepieceEnum.ALICE
        self.repo.getLabyrinth()[self.minotaur.pos.row][self.minotaur.pos.col].gamepiece = GamepieceEnum.MINOTAUR

    def switchTurn(self):
        if self.repo.turn == Turn.PLAYER:
            self.repo.turn = Turn.COMPUTER
        else:
            self.repo.turn = Turn.PLAYER

    def getTurn(self):
        return self.repo.turn

    def getGamestate(self) -> Gamestate:
        if self.repo.getLabyrinth()[self.alice.pos.row][self.alice.pos.col].labyrinth == LabyrinthEnum.EXIT:
            return Gamestate.WIN
        if self.alice.pos.row == self.minotaur.pos.row and self.alice.pos.col == self.minotaur.pos.col:
            return Gamestate.LOSE
        return Gamestate.IDLE

    def move(self, gamepiece: Gamepiece, movement: Movement) -> str:
        oldCol = gamepiece.pos.col
        oldRow = gamepiece.pos.row
        direction = movement.direction
        magnitude = movement.magnitude
        self.repo.setLastMagnitude(magnitude)
        try:
            for i in range(magnitude):
                if self.getGamestate() != Gamestate.IDLE:
                    return ""
                if direction == Direction.UP:
                    gamepiece.pos.row -= 1
                if direction == Direction.DOWN:
                    gamepiece.pos.row += 1
                if direction == Direction.LEFT:
                    gamepiece.pos.col -= 1
                if direction == Direction.RIGHT:
                    gamepiece.pos.col += 1


                if isinstance(gamepiece, Minotaur):
                    if self.repo.getLabyrinth()[gamepiece.pos.row][
                        gamepiece.pos.col].labyrinth == LabyrinthEnum.EXIT:
                        raise ValueError
            return ""
        except ValueError:
            gamepiece.pos.row = oldRow
            gamepiece.pos.col = oldCol
            return "Invalid Movement"



