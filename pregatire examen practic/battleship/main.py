from data.GameState import GameState
from data.Turn import Turn
from repo.repo import Repo
from services.Bot import Bot
from services.GameService import GameService
from ui.InputHandler import InputHandler
from ui.Printer import Printer

repo = Repo()
service = GameService(repo)
bot = Bot(service)
inputHandler = InputHandler(service, bot)
while True:
    if repo.turn == Turn.PLAYER:
        inputHandler.process(input(">"))
    else:
        positionState = bot.attack()
        print(f"Computer {positionState.name}")
        Printer.printBoard(service.repo.playerBoard)
        print("PLAYER BOARD")
        Printer.printBoard(service.repo.playerTargeting)
        print("PLAYER TARGETING")
        print()
        service.switchTurn()
    if service.checkWin() != GameState.IDLE:
        print(service.checkWin().name)
        quit()


