from data.GamePhase import GamePhase
from data.Position import Position
from data.PositionState import PositionState
from data.Ship import Ship
from data.Turn import Turn


class Repo:
    def __init__(self):
        self.playerShipList: list[Ship] = []
        self.computerShipList: list[Ship] = []
        self.playerBoard: list[list[PositionState]] = [[PositionState.EMPTY for _ in range(6)] for _ in range(6)]
        self.playerTargeting: list[list[PositionState]] = [[PositionState.EMPTY for _ in range(6)] for _ in range(6)]
        self.computerBoard: list[list[PositionState]] = [[PositionState.EMPTY for _ in range(6)] for _ in range(6)]
        self.computerTargeting: list[list[PositionState]] = [[PositionState.EMPTY for _ in range(6)] for _ in range(6)]
        self.gamephase = GamePhase.PLACE
        self.turn = Turn.PLAYER

    def updatePlayerTargeting(self, pos: Position):
        self.playerTargeting[pos.number][ord(pos.letter) - ord("A")] = pos.state

        for ship in self.computerShipList:
            if ship.pos1 == pos:
                ship.pos1.state = pos.state
            if ship.pos2 == pos:
                ship.pos2.state = pos.state
            if ship.pos3 == pos:
                ship.pos3.state = pos.state

    def updateComputerTargeting(self, pos: Position):
        self.computerTargeting[pos.number][ord(pos.letter) - ord("A")] = pos.state
        for ship in self.playerShipList:
            if ship.pos1 == pos:
                ship.pos1.state = pos.state
            if ship.pos2 == pos:
                ship.pos2.state = pos.state
            if ship.pos3 == pos:
                ship.pos3.state = pos.state

    def updatePlayerBoard(self, pos: Position):
        self.playerBoard[pos.number][ord(pos.letter) - ord("A")] = pos.state

        for ship in self.playerShipList:
            if ship.pos1 == pos:
                ship.pos1.state = pos.state
            if ship.pos2 == pos:
                ship.pos2.state = pos.state
            if ship.pos3 == pos:
                ship.pos3.state = pos.state

    def updateComputerBoard(self, pos: Position):
        self.computerBoard[pos.number][ord(pos.letter) - ord("A")] = pos.state
        for ship in self.computerShipList:
            if ship.pos1 == pos:
                ship.pos1.state = pos.state
            if ship.pos2 == pos:
                ship.pos2.state = pos.state
            if ship.pos3 == pos:
                ship.pos3.state = pos.state

    def addPlayerShip(self, ship: Ship):
        for existing in self.playerShipList:
            if (ship.pos1 == existing.pos1 or ship.pos1 == existing.pos2 or ship.pos1 == existing.pos3
                or ship.pos2 == existing.pos1 or ship.pos2 == existing.pos2 or ship.pos2 == existing.pos3
                or ship.pos3 == existing.pos1 or ship.pos3 == existing.pos2 or ship.pos3 == existing.pos3):
                raise ValueError("Cannot overlap ships")
        self.playerShipList.append(ship)
        self.updatePlayerBoard(ship.pos1)
        self.updatePlayerBoard(ship.pos2)
        self.updatePlayerBoard(ship.pos3)

    def addComputerShip(self, ship: Ship):
        for existing in self.computerShipList:
            if (ship.pos1 == existing.pos1 or ship.pos1 == existing.pos2 or ship.pos1 == existing.pos3
                or ship.pos2 == existing.pos1 or ship.pos2 == existing.pos2 or ship.pos2 == existing.pos3
                or ship.pos3 == existing.pos1 or ship.pos3 == existing.pos2 or ship.pos3 == existing.pos3):
                raise ValueError("Cannot overlap ships")
        self.computerShipList.append(ship)
        self.updateComputerBoard(ship.pos1)
        self.updateComputerBoard(ship.pos2)
        self.updateComputerBoard(ship.pos3)

    def removePlayerShip(self, ship: Ship):
        self.playerShipList.remove(ship)
        ship.pos1.state = PositionState.EMPTY
        ship.pos2.state = PositionState.EMPTY
        ship.pos3.state = PositionState.EMPTY
        self.updatePlayerBoard(ship.pos1)
        self.updatePlayerBoard(ship.pos2)
        self.updatePlayerBoard(ship.pos3)