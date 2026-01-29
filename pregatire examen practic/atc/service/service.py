from data.Airport import Airport
from data.Flight import Flight
from data.Time import Time
from repo.Repo import Repo


class Service:
    def __init__(self):
        self.repo = Repo()
        self.repo.readfile()

    def addFlight(self, newFlight: Flight):
        for flight in self.repo.flightlist:
            if newFlight.identifier == flight.identifier:
                raise ValueError(f"duplicate id: {flight.identifier}, {newFlight.identifier}")
            if newFlight.arrivalTime == flight.departureTime:
                raise ValueError(f"arrivalTime = departureTime")
            if newFlight.arrivalTime == flight.arrivalTime:
                raise ValueError(f"arrivalTime = arrivalTime")
            if newFlight.departureTime == flight.departureTime:
                raise ValueError(f"departureTime = departureTime")
            if newFlight.departureTime == flight.arrivalTime:
                raise ValueError(f"departureTime = arrivalTime")
            if newFlight.getFlightTime() < 15 or newFlight.getFlightTime() > 90:
                raise ValueError("flight too long or too short")
        self.repo.addFlight(newFlight)

    def removeFlight(self, identifier: str = None):
        if identifier is None:
            raise ValueError("flight not specified")
        flight = Flight(identifier, 0, 0, 0, 0)
        for obj in self.repo.flightlist:
            if obj == flight:
                self.repo.removeFlight(obj)

    def getAllFlights(self):
        return self.repo.flightlist[:]

    def getAirports(self) -> list[Airport]:
        airportList: list[Airport] = []
        for flight in self.repo.flightlist:
            departureCity = flight.departureCity
            arrivalCity = flight.arrivalCity
            departureExists = False
            arrivalExists = False
            for airport in airportList:
                if departureCity == airport.city:
                    airport.activityScore += 1
                    departureExists = True
                if arrivalCity == airport.city:
                    airport.activityScore += 1
                    arrivalExists = True
            if not departureExists:
                airportList.append(Airport(departureCity, 1))
            if not arrivalExists:
                airportList.append(Airport(arrivalCity, 1))
        return sorted(airportList, key=lambda x: x.activityScore, reverse=True)

    def radarFailure(self):
        allFlights = self.repo.flightlist[:]
        allFlights = sorted(allFlights, key=lambda x: x.arrivalTime.getTimeInMinutes())
        capableFlights: list[Flight] = [allFlights[0]]
        for flight in allFlights:
            if flight.departureTime.getTimeInMinutes() >= capableFlights[-1].arrivalTime.getTimeInMinutes():
                capableFlights.append(flight)
        return capableFlights
