import random

from data.Enums import Gamestate
from repo.City import City


class Service:
    def __init__(self):
        self.city = City(1, 1000, 20, 100, 0, 0, 200, 3, 2800)

    def computeGamestate(self) -> Gamestate:
        return self.city.getGamestate()

    def modifyLandOwnership(self, value: int):
        valueInUnits = value * self.city.getLandPrice()
        self.city.modifyUnitStocks(-valueInUnits)
        self.city.setLandOwnership(self.city.getLandOwnership() + value)

    def computeRandomLandPrice(self):
        self.city.setLandPrice(random.randint(15, 25))

    def computeRandomHarvestRate(self):
        self.city.setHarvestRate(random.randint(1, 6))

    def feedPopulation(self, units):
        if units < 0:
            raise ValueError("bro...")
        self.city.modifyUnitStocks(-units)
        populationFeedingPotential = units // 20
        oversaturation = populationFeedingPotential - self.city.getPopulation()
        if oversaturation < 0:
            self.city.setStarved(abs(oversaturation))
        else:
            self.city.modifyUnitStocks(oversaturation * 20)
            self.city.setStarved(0)

    def computeNewcommers(self):
        if self.city.getStarved() == 0:
            self.city.setNewcommers(random.randint(0, 10))
        else:
            self.city.setNewcommers(0)

    def computePlantedLand(self, value: int):
        self.city.tryPlantedLand(value)
        self.city.modifyUnitStocks(-value)
        self.city.setPlantedLand(value)

    def computeRandomRatInfestation(self):
        ratDice = random.randint(1, 10)
        if ratDice < 3:
            self.city.setRats(random.randint(1//100 * self.city.getUnitStocks(), 10//100 * self.city.getUnitStocks()))
        else:
            self.city.setRats(0)

    def computePassiveUnitStocks(self):
        self.computeRandomRatInfestation()
        self.city.modifyUnitStocks(self.city.getPlantedLand() * self.city.getHarvestRate())
        self.city.modifyUnitStocks(-self.city.getRats())

    def computePopulation(self):
        self.computeNewcommers()
        self.city.setPopulation(self.city.getPopulation() - self.city.getStarved())
        self.city.setPopulation(self.city.getPopulation() + self.city.getNewcommers())

    def changeYear(self):
        self.computeRandomLandPrice()
        self.computeRandomHarvestRate()
        self.city.setYear(self.city.getYear() + 1)

    def getUnitStocks(self):
        return self.city.getUnitStocks()

    def getLandOwnership(self):
        return self.city.getLandOwnership()

    def getPrintString(self):
        return str(self.city)