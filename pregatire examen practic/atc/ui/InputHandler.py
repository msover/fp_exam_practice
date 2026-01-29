from data.Flight import Flight
from service.service import Service


class InputHandler:
    def __init__(self, service: Service):
        self.service = service

    def processInput(self, inputString: str):
        inputString = inputString.split(" ")
        match inputString[0]:
            case "add":
                try:
                    self.service.addFlight(Flight.getFromString(inputString[1]))
                except ValueError as e:
                    print(e)
            case "del":
                try:
                    if len(inputString) == 2:
                        self.service.removeFlight(inputString[1])
                    else:
                        self.service.removeFlight()
                except ValueError as e:
                    print(e)
            case "airport":
                for airport in self.service.getAirports():
                    print(airport)
            case "radar":
                for flight in self.service.radarFailure():
                    print(flight)
            case "list":
                for flight in self.service.getAllFlights():
                    print(flight)
            case "q":
                quit()
