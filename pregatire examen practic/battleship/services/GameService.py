from data.GamePhase import GamePhase
from data.GameState import GameState
from data.Position import Position
from data.PositionState import PositionState
from data.Ship import Ship
from data.Turn import Turn
from repo.repo import Repo


class GameService:
    def __init__(self, repo: Repo):
        self.repo = repo

    def ship(self, shipString: str):
        """
        places a ship on the player board according to the given ship string;
        if there are 2 ships on the board already, the first board placed is overwritten
        :param shipString: a string signifying coordinates for ship position
        :return:
        """
        if self.repo.gamephase != GamePhase.PLACE:
            raise ValueError(f"Currently in gamephase {self.repo.gamephase.name}")
        c1 = shipString[0]
        l1 = shipString[1]
        c2 = shipString[2]
        l2 = shipString[3]
        c3 = shipString[4]
        l3 = shipString[5]
        pos1 = Position(int(l1), c1)
        pos2 = Position(int(l2), c2)
        pos3 = Position(int(l3), c3)
        ship = Ship(pos1, pos2, pos3)
        for existing in range(len(self.repo.playerShipList)):
            if existing == 0:
                continue
            if self.repo.playerShipList[existing] == ship:
                raise ValueError("Cannot overlap ships")
        if len(self.repo.playerShipList) > 1:
            self.repo.removePlayerShip(self.repo.playerShipList[0])
        self.repo.addPlayerShip(ship)

    def startGame(self):
        if len(self.repo.playerShipList) != 2:
            raise ValueError(f"Currently in gamephase {self.repo.gamephase.name}")
        self.repo.gamephase = GamePhase.START

    def switchTurn(self):
        if self.repo.turn == Turn.PLAYER:
            self.repo.turn = Turn.COMPUTER
        else:
            self.repo.turn = Turn.PLAYER

    def attack(self, attackString: str) -> PositionState:
        if self.repo.gamephase != GamePhase.START:
            raise ValueError(f"Currently in gamephase {self.repo.gamephase.name}")
        c1 = attackString[0]
        l1 = attackString[1]
        pos = Position(int(l1), c1, PositionState.MISS)

        if self.repo.turn == Turn.PLAYER:
            for ship in self.repo.computerShipList:
                if ship.pos1 == pos or ship.pos2 == pos or ship.pos3 == pos:
                    pos.state = PositionState.HIT
                    self.repo.updateComputerBoard(pos)
            self.repo.updatePlayerTargeting(pos)
        if self.repo.turn == Turn.COMPUTER:
            for ship in self.repo.playerShipList:
                if ship.pos1 == pos or ship.pos2 == pos or ship.pos3 == pos:
                    pos.state = PositionState.HIT
                    self.repo.updatePlayerBoard(pos)
            self.repo.updateComputerTargeting(pos)

        return pos.state

    def checkWin(self) -> GameState:
        computerShipsDestroyed = 0
        playerShipsDestroyed = 0
        for ship in self.repo.computerShipList:
            if ship.pos1.state == PositionState.HIT and ship.pos2.state == PositionState.HIT and ship.pos3.state == PositionState.HIT:
                computerShipsDestroyed += 1
        for ship in self.repo.playerShipList:
            if ship.pos1.state == PositionState.HIT and ship.pos2.state == PositionState.HIT and ship.pos3.state == PositionState.HIT:
                playerShipsDestroyed += 1
        if playerShipsDestroyed == 2:
            return GameState.LOSE
        if computerShipsDestroyed == 2:
            return GameState.WIN
        return GameState.IDLE



