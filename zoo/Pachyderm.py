from Animal import Animal

class Pachyderm(Animal):
    
    def roam(self):
        print(self.name+ " the " + self.__class__.__name__+ " roams around the dessert")   