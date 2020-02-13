from Canine import Canine

class Wolf(Canine):
    
    def makeNoise(self):
        print(self.name+ " the " + self.__class__.__name__+ " howls")