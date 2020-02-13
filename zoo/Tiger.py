from Feline import Feline

class Tiger(Feline):
    
    def makeNoise(self):
        print(self.name+ " the " + self.__class__.__name__+ " hisses")