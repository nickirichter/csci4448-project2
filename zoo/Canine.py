from Animal import Animal
from strategy import roamDessert, roamTrees, roamGrass

class Canine(Animal):

    def __init__(self, name):
        super(Canine, self).__init__(name, roamGrass())
    
    def roam(self):
        print(self.name+ " the " + self.__class__.__name__+ " roams in the grass")