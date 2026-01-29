from data.Enums import Gamestate
from service.service import Service


class UI:
    def __init__(self):
        self.service = Service()

    def getGoodNewLand(self) -> bool:
        try:
            newLandOwnership = int(input("Acres to buy/sell (+/-) >"))
        except ValueError:
            print("invalid input")
            return False
        try:
            self.service.modifyLandOwnership(newLandOwnership)
        except ValueError as e:
            print(e)
            return False
        print(f"Unit stocks now sitting at {self.service.getUnitStocks()}")
        print(f"Land ownership is {self.service.getLandOwnership()}")
        return True

    def getGoodFeed(self) -> bool:
        try:
            unitsForFeeding = int(input("Units to feed the population >"))
        except ValueError:
            print("invalid input")
            return False
        try:
            self.service.feedPopulation(unitsForFeeding)
        except ValueError as e:
            print(e)
            return False
        print(f"Unit stocks now sitting at {self.service.getUnitStocks()}")
        return True

    def getGoodPlant(self) -> bool:
        try:
            plantedLand = int(input("Acres to plant > "))
        except ValueError:
            print("invalid input")
            return False
        try:
            self.service.computePlantedLand(plantedLand)
        except ValueError as e:
            print(e)
            return False
        print(f"Unit stocks now sitting at {self.service.getUnitStocks()}")
        return True

    def processInputs(self):
        goodNewLand = False
        goodFeed = False
        goodPlant = False
        while not (goodNewLand and goodFeed and goodPlant):
            if not goodNewLand:
                goodNewLand = self.getGoodNewLand()
                continue
            if not goodFeed:
                goodFeed = self.getGoodFeed()
                continue
            if not goodPlant:
                goodPlant = self.getGoodPlant()
                continue

    def gameloop(self):
        while True:
            print()
            print(self.service.getPrintString())
            print()
            self.processInputs()
            self.service.changeYear()
            self.service.computePassiveUnitStocks()
            gamestate = self.service.computeGamestate()
            self.service.computePopulation()
            if gamestate != Gamestate.IDLE:
                print(f"You {gamestate.value}!")
                quit()

