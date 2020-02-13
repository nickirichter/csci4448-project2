from Animal import Animal
import numpy as np

class Feline(Animal):
    
    def roam(self):
        print(self.name+ " the " + self.__class__.__name__+ " roams in the trees")
        
    def eat(self):
        n = np.random.randint(0, 3)
        
        if n == 0:
            self.roam()
        elif n == 1:
            self.makeNoise()
        else:
            self.goToSleep()