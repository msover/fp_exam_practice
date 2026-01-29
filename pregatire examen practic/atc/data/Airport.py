class Airport:
    def __init__(self, city, activityScore = 0):
        self.city = city
        self.activityScore = activityScore

    def __str__(self):
        return f"{self.city}: {self.activityScore}"

    def __repr__(self):
        return self.__str__()