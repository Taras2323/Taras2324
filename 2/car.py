from Human import Human
class Car:
    def __init__(self, brand = None):
        self.Brand = brand
        self.Passengers = list()
        self.Drivers = list()
    def AddHumanToCar(self, human = Human()):
        if(human.IsDriver):
            self.Drivers.append(human)
        else:
            self.Passengers.append(human)
    def ShowInfo(self, human = Human()):
        if(human.IsDriver):
            print(f"The driver of {self.Brand} is {human.__str__()}")
        else:
            print(f"The passenger of {self.Brand} is {human.__str__()}")