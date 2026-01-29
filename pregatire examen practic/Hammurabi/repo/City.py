from data.Enums import Gamestate


class City:
    def __init__(self, year, landOwnership, landPrice, population,
                 newcommers, starved, rats, harvestRate, unitStocks, unitsToBuySell = 0, unitsToFeed = 0, plantedLand = 0):
        self._year = year
        self._landOwnership = landOwnership
        self._landPrice = landPrice
        self._population = population
        self._newcommers = newcommers
        self._starved = starved
        self._rats = rats
        self._harvestRate = harvestRate
        self._unitStocks = unitStocks
        self._unitsToBuySell = unitsToBuySell
        self._unitsToFeed = unitsToFeed
        self._plantedLand = plantedLand
        self._gamestate = Gamestate.IDLE

    def getYear(self) -> int:
        return self._year
    def getLandOwnership(self) -> int:
        return self._landOwnership
    def getLandPrice(self) -> int:
        return self._landPrice
    def getPopulation(self) -> int:
        return self._population
    def getNewcommers(self) -> int:
        return self._newcommers
    def getStarved(self) -> int:
        return self._starved
    def getRats(self) -> int:
        return self._rats
    def getHarvestRate(self) -> int:
        return self._harvestRate
    def getUnitStocks(self) -> int:
        return self._unitStocks
    def getPlantedLand(self) -> int:
        return self._plantedLand
    def getGamestate(self) -> Gamestate:
        if self._year < 5:
            self._gamestate = Gamestate.IDLE
        elif self._population > 100 and self._landOwnership > 1000:
            self._gamestate = Gamestate.WIN
        else:
            self._gamestate = Gamestate.LOSE

        if self._starved * 2 > self._population:
            self._gamestate = Gamestate.LOSE

        return self._gamestate


    def setYear(self, value: int):
        self._year = value
    def setLandOwnership(self, value: int):
        self._landOwnership = value
    def setLandPrice(self, value: int):
        self._landPrice = value
    def setPopulation(self, value: int):
        self._population = value
    def setNewcommers(self, value: int):
        self._newcommers = value
    def setStarved(self, value: int):
        self._starved = value
    def setRats(self, value: int):
        self._rats = value
    def setHarvestRate(self, value: int):
        self._harvestRate = value
    def setUnitStocks(self, value: int):
        self._unitStocks = value

    def modifyUnitStocks(self, value: int):
        if self._unitStocks + value < 0:
            raise ValueError("Grain stock below 0")
        self._unitStocks += value

    def tryPlantedLand(self, value: int):
        if value > self._landOwnership:
            raise ValueError("Not enough land to plant")
        if self._population * 10 < value:
            raise ValueError("Not enough people to plant")
    def setPlantedLand(self, value: int):
        if value > self._landOwnership:
            raise ValueError("Not enough land to plant")
        self._plantedLand = value

    def __str__(self):
        return (f"In year {self._year}, {self._starved} people starved.\n"
                f"{self._newcommers} people came to the city.\n"
                f"City population is {self._population}.\n"
                f"City owns {self._landOwnership} acres of land.\n"
                f"Harvest was {self._harvestRate} units per acre.\n"
                f"Rats are {self._rats} units.\n"
                f"Land price is {self._landPrice} units per acre.\n"
                f"\n"
                f"Grain stocks are {self._unitStocks} units\n")