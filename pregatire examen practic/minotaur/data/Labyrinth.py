from data.Enums import LabyrinthEnum, GamepieceEnum


class Labyrinth:
    def __init__(self, labyrinthEnum: LabyrinthEnum, gamepieceEnum: GamepieceEnum = GamepieceEnum.NONE):
        self.labyrinth = labyrinthEnum
        self.gamepiece = gamepieceEnum