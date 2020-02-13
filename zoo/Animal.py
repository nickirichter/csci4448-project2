from Zoo import Zoo

class Animal(Zoo):
    
    def __init__(self, name):
        self.name = name
    
    def setName(self, name):
        self.name = name
        
    def wakeUp(self):
        print(self.name+ " the " + self.__class__.__name__+ " wakes up")
        
    def makeNoise(self):
        print(self.name+ " the " + self.__class__.__name__+ " makes noise")
        
    def eat(self):
        print(self.name+ " the " + self.__class__.__name__+ " eats their food")
        
    def roam(self):
        print(self.name+ " the " + self.__class__.__name__+ " roams")
        
    def goToSleep(self):
        print(self.name+ " the " + self.__class__.__name__+ " goes to sleep")