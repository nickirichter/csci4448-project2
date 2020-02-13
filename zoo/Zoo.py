import abc

class Zoo(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def wakeUp(self):
        pass
    
    @abc.abstractmethod
    def makeNoise(self):
        pass
    
    @abc.abstractmethod
    def eat(self):
        pass

    
    @abc.abstractmethod
    def roam(self):
        pass

    
    @abc.abstractmethod
    def goToSleep(self):
        pass