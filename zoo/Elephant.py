from Pachyderm import Pachyderm

class Elephant(Pachyderm):
    
    def makeNoise(self):
        print(self.name+ " the " + self.__class__.__name__+ " waves trunk")