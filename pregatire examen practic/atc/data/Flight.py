from data.Time import Time


class Flight:
    def __init__(self, identifier: str, departureCity: str, departureTime: Time, arrivalCity: str, arrivalTime: Time):
        self.identifier = identifier
        self.departureCity = departureCity
        self.departureTime = departureTime
        self.arrivalCity = arrivalCity
        self.arrivalTime = arrivalTime

    def __repr__(self):
        #return f"|{self.identifier}, {self.departureCity}, {self.departureTime}, {self.arrivalCity}, {self.arrivalTime}|"
        return f"{self.departureTime} | {self.arrivalTime} | {self.departureCity} - {self.arrivalCity}"

    def __eq__(self, other: Flight):
        if not isinstance(other, Flight):
            return False
        return self.identifier == other.identifier

    def getFlightTime(self) -> int:
        return self.arrivalTime - self.departureTime

    @classmethod
    def getFromString(cls, flightString) -> Flight:
        flightString = flightString.split(",")
        identifier = flightString[0]
        departureCity = flightString[1]
        departureTime = Time(flightString[2])
        arrivalCity = flightString[3]
        arrivalTime = Time(flightString[4])
        flight = Flight(identifier, departureCity,
                        departureTime, arrivalCity, arrivalTime)
        return flight

    def getFlightString(self) -> str:
        return f"{self.identifier},{self.departureCity},{self.departureTime},{self.arrivalCity},{self.arrivalTime}\n"