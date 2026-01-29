import random

from data.Position import Position
from data.PositionState import PositionState
from data.Ship import Ship
from repo.repo import Repo
from services.GameService import GameService


class Bot:
    def __init__(self, service: GameService):
        self.numberSet = [0, 1, 2, 3, 4, 5]
        self.letterSet = ["A", "B", "C", "D", "E", "F"]
        self.service = service

    def setShips(self):
        row1 = random.randint(0, 3)
        col1 = random.choice(self.letterSet[:3])
        row2 = random.randint(0, 3)
        col2 = random.choice(self.letterSet[-3:])
        pos1 = Position(row1, col1)
        pos2 = Position(row1 + 1, col1)
        pos3 = Position(row1 + 2, col1)
        ship1 = Ship(pos1, pos2, pos3)
        self.service.repo.addComputerShip(ship1)

        pos4 = Position(row2, col2)
        pos5 = Position(row2 + 1, col2)
        pos6 = Position(row2 + 2, col2)
        ship2 = Ship(pos4, pos5, pos6)
        self.service.repo.addComputerShip(ship2)

    def attack(self) -> PositionState:
        original = False
        while not original:
            number = random.choice(self.numberSet)
            letter = random.choice(self.letterSet)
            if self.service.repo.computerTargeting[number][ord(letter) - 65] == PositionState.EMPTY:
                original = True
        return self.service.attack(f"{letter}{number}")

