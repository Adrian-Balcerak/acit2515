class Bike:
    def __init__(self):
        self.rider = None
        self.distance = 0

    def start_rental(self, rider):
        if self.rider != None:
            raise  RuntimeError
        self.rider = rider

    def bike(self, distance):
        if distance < 0:
            raise AttributeError
        if self.rider == None:
            raise RuntimeError
        self.distance += distance

    def end_rental(self):
        if self.rider == None:
            raise RuntimeError
        temp = self.distance
        self.rider = None
        self.distance = 0
        return temp