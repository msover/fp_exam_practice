from data.Enums import Direction, Turn, Gamestate
from repo.TxtRepo import TxtRepo
from service.Bot import Bot
from service.service import Service
from ui.InputHandler import InputHandler

repo = TxtRepo()
service = Service(repo)
bot = Bot(service)
service.setGamepieces()
service.updateLabyrinth()
labyrinth = repo.getLabyrinth()
inputHandler = InputHandler()

while True:
    if service.getGamestate() != Gamestate.IDLE:
        print(f"YOU {service.getGamestate().value}!")
        quit()
    service.updateLabyrinth()
    if service.getTurn() == Turn.PLAYER:
        inputHandler.printer(labyrinth)
        movement = inputHandler.processInput(input(">"))
        if movement.direction == Direction.NONE:
            continue
        errorString = service.move(service.alice, movement)
        if errorString == '':
            service.switchTurn()
        else:
            print(errorString)
    if service.getTurn() == Turn.COMPUTER:
        bot.issueCommand()
        service.switchTurn()
