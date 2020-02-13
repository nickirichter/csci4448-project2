from Feline import Feline

class Lion(Feline):
    
    def makeNoise(self):
        print(self.name+ " the " + self.__class__.__name__+ " roars")