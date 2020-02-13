from Animal import Animal
from strategy import roamDessert, roamTrees, roamGrass

class Pachyderm(Animal):

    def __init__(self, name):
        super(Pachyderm, self).__init__(name, roamDessert())
    
    def roam(self):
        print(self.name+ " the " + self.__class__.__name__+ " roams around the dessert")   