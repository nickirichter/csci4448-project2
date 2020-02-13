from Zoo import Zoo
from strategy import roamDessert, roamTrees, roamGrass

class Animal(Zoo):
    
    def __init__(self, name, roam_strategy):
        self.name = name
        self.roam_strategy = roam_strategy
    
    def setName(self, name):
        self.name = name
        
    def wakeUp(self):
        print(self.name+ " the " + self.__class__.__name__+ " wakes up")
        
    def makeNoise(self):
        print(self.name+ " the " + self.__class__.__name__+ " makes noise")
        
    def eat(self):
        print(self.name+ " the " + self.__class__.__name__+ " eats their food")
        
    def roam(self):
        # print(self.name+ " the " + self.__class__.__name__+ " roams")
        self.roam_strategy.roam()
        
    def goToSleep(self):
        print(self.name+ " the " + self.__class__.__name__+ " goes to sleep")