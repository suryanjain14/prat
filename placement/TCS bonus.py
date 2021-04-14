class Theatre:
    def __init__(self, ):
        self.theatreId = int()
        self.theatreName = str()
        self.seatCapacity = int()
        self.ticketRate = float()
        self.theatreRating = float()
        self.balconyAvailable = bool()

    def getId(self):
        return self.theatreId

    def getName(self):
        return self.theatreName

    def getCapacity(self):
        return self.seatCapacity

    def getRating(self):
        return self.theatreRating

    def getPrice(self):
        return self.ticketRate

    def setId(self, Id):
        self.theatreId = Id

    def setName(self, name):
        self.theatreName = name

    def setCapacity(self, Capacity):
        self.seatCapacity = Capacity

    def setRating(self, rating):
        self.theatreRating = rating

    def setPrice(self, price):
        self.ticketRate = price


class MyClass:
    @staticmethod
    def findTheatreCategory(arr: Theatre, value: int):
        pass

    @staticmethod
    def searchTheatreByCapacity(arr: Theatre, value: float):
        pass
