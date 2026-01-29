from service.service import Service
from ui.InputHandler import InputHandler


class UI:
    def __init__(self):
        self.service = Service()
        self.inputHandler = InputHandler(self.service)
    def loop(self):
        while True:
            self.inputHandler.processInput(input(">"))
