from abc import ABC, abstractmethod

class Transportation(ABC):
    def __init__(self, start_place, end_place, distance):
        self.start_place = start_place
        self.end_place = end_place
        self.distance = distance

    @abstractmethod
    def cost(self):
        pass

class Walk(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def cost(self):
        return 0

class Taxi(Transportation):
    def __init__(self, start_place, end_place, distance):
        super().__init__(start_place, end_place, distance)

    def cost(self):
        return self.distance * 40

class Train(Transportation):
    def __init__(self, start_place, end_place, distance, station):
        super().__init__(start_place, end_place, distance)
        self.station = station

    def number_of_station(self):
        return self.station

    def cost(self):
        return self.station * 5

def find_cost(transportation):
    return transportation.cost()

walk = Walk("KMITL", "Lawson at KMITL", 0.6)
taxi = Taxi("Lawson at KMITl", "Latkrabang Station", 5)
train = Train("Latkrabang Station", "Payathai Station", 40, 6)

print(f"Walk cost: {find_cost(walk)}")
print(f"Taxi cost: {find_cost(taxi)}")
print(f"Train cost: {find_cost(train)} (Number of stations: {train.number_of_station()})")

taxi = Taxi("Payathai Station", "The British Council", 3)
print(f"Taxi cost: {find_cost(taxi)}")
