from data.Enums import Direction, GamepieceEnum
from data.Labyrinth import Labyrinth
from data.Movement import Movement


class InputHandler:
    def __init__(self):
        self.lastDirection = Direction.NONE

    def processInput(self, userInput) -> Movement:
        userInput = userInput.upper()
        userInput = userInput.split(" ")
        match userInput[0]:
            case "UP":
                self.lastDirection = Direction.UP
                return Movement(Direction.UP)
            case "DOWN":
                self.lastDirection = Direction.DOWN
                return Movement(Direction.DOWN)
            case "LEFT":
                self.lastDirection = Direction.LEFT
                return Movement(Direction.LEFT)
            case "RIGHT":
                self.lastDirection = Direction.RIGHT
                return Movement(Direction.RIGHT)
            case "MOVE":
                if len(userInput) == 1:
                    return Movement(self.lastDirection)
                if not userInput[1].isdigit():
                    return Movement(Direction.NONE)
                return Movement(self.lastDirection, int(userInput[1]))
            case "QUIT":
                quit()
            case _:
                return Movement(Direction.NONE)

    def printer(self, labyrinth: list[list[Labyrinth]]):
        for row in labyrinth:
            for col in row:
                if col.gamepiece == GamepieceEnum.NONE:
                    print(col.labyrinth.value, end="")
                else:
                    print(col.gamepiece.value, end="")
            print()
