class Time:
    def __init__(self, timeString: str = None):
        if timeString is None:
            self.hour = 0
            self.minute = 0
        else:
            self.timeString = timeString
            timeString = timeString.split(":")
            self.hour = int(timeString[0])
            self.minute = int(timeString[1])
        self.validation()


    def getTimeString(self) -> str:
        return self.timeString

    def __sub__(self, other) -> int:
        return (self.hour * 60 + self.minute) - (other.hour * 60 + other.minute)

    def getTimeInMinutes(self) -> int:
        return self.hour * 60 + self.minute

    def __repr__(self):
        hour = ''
        minute = ''
        if self.hour < 10:
            hour = '0'
        if self.minute < 10:
            minute = '0'
        hour += f"{self.hour}"
        minute += f"{self.minute}"
        return f"{hour}:{minute}"

    def __eq__(self, other: Time):
        if not isinstance(other, Time):
            return False
        return self.hour == other.hour and self.minute == other.minute

    def validation(self):
        if self.hour < 0 or self.hour > 23:
            raise ValueError("Invalid hour")
        if self.minute < 0 or self.minute > 59:
            raise ValueError("Invalid miunute")