from data.Flight import Flight
from data.Time import Time


class Repo:
    def __init__(self):
        self.flightlist: list[Flight] = []

    def readfile(self):
        with open("atc.txt", "r") as file:
            for flightString in file:
                if flightString =='\n':
                    continue
                self.flightlist.append(Flight.getFromString(flightString))

    def addFlight(self, flight: Flight):
        self.flightlist.append(flight)
        self.writefile()

    def removeFlight(self, flight):
        self.flightlist.remove(flight)
        self.writefile()

    def writefile(self):
        with open("atc.txt", "w") as file:
            for flight in self.flightlist:
                file.write(flight.getFlightString())