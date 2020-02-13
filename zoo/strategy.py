import abc

class RoamStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def roam(self):
        pass
    
class roamDessert(RoamStrategyAbstract):
    def roam(self):
        def roam(self):
            print(self.name+ " the " + self.__class__.__name__+ " roams around the dessert")
            
class roamTrees(RoamStrategyAbstract):
    def roam(self):
        def roam(self):
            print(self.name+ " the " + self.__class__.__name__+ " roams in the trees")
                       
class roamGrass(RoamStrategyAbstract):
    def roam(self):
        def roam(self):
            print(self.name+ " the " + self.__class__.__name__+ " roams in the grass")
            