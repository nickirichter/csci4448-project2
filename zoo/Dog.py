from Canine import Canine

class Dog(Canine):
    
    def makeNoise(self):
        print(self.name+ " the " + self.__class__.__name__+ " barks")