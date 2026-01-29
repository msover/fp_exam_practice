from repo.repo import Repo
from services.Bot import Bot
from services.GameService import GameService
from ui.Printer import Printer


class InputHandler:
    def __init__(self, service: GameService, bot: Bot):
        self.service = service
        self.bot = bot

    def process(self, string: str):
        cheat = False
        string = string.split(" ")
        match string[0]:
            case "ship":
                try:
                    self.service.ship(string[1])
                except ValueError as e:
                    print(e)
            case "start":
                try:
                    self.service.startGame()
                    self.bot.setShips()
                except ValueError as e:
                    print(e)
            case "attack":
                try:
                    positionState = self.service.attack(string[1])
                    print(f"Player {positionState.name}!")
                    self.service.switchTurn()
                except ValueError as e:
                    print(e)
            case "cheat":
                cheat = True
                Printer.printBoard(self.service.repo.computerBoard)
                print("COMPUTER BOARD")
                Printer.printBoard(self.service.repo.computerTargeting)
                print("COMPUTER TARGETING")
                print()
        if not cheat:
            Printer.printBoard(self.service.repo.playerBoard)
            print("BOARD")
            Printer.printBoard(self.service.repo.playerTargeting)
            print("TARGETING")
            print()