from Pachyderm import Pachyderm

class Rhino(Pachyderm):
    
    def makeNoise(self):
        print(self.name+ " the " + self.__class__.__name__+ " snorts")