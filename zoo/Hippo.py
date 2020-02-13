from Pachyderm import Pachyderm

class Hippo(Pachyderm):
    
    def makeNoise(self):
        print(self.name+ " the " + self.__class__.__name__+ " yawns")