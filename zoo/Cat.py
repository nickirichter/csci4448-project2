from Feline import Feline

class Cat(Feline):
    
    def makeNoise(self):
        print(self.name+ " the " + self.__class__.__name__+ " meows")