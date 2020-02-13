from Animal import Animal

class Canine(Animal):
    
    def roam(self):
        print(self.name+ " the " + self.__class__.__name__+ " roams in the grass")