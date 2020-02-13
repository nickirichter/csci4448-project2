from Zoo import Zoo
from observer import Subject

class Zookeeper(Subject):
    
    def __init__(self):
        self.task = None
        self.observers = []
        
    def register_observer(self, observer):
        self.observers.append(observer)
        
    def remove_observer(self, observer):
        self.observers.remove(observer)
        
    def notify_observers(self):
        for o in self.observers:
            o.update(self.task)
            
    def task_changed(self):
        self.notify_observers()
    
    def wakeUpAnimals(self, animals):
        self.task = "wake"
        self.task_changed()
        print("Zookeeper wakes up animals:")
        for a in animals:
            a.wakeUp()
            
    def rollCall(self, animals):
        self.task = "take roll of all"
        self.task_changed()
        print("Zookeeper starts roll call of animals:")
        for a in animals:
            a.makeNoise()
            
    def feed(self, animals):
        self.task = "feed"
        self.task_changed()
        print("Zookeeper feeds animals:")
        for a in animals:
            a.eat()
            
    def exercise(self, animals):
        self.task = "exercise"
        self.task_changed()
        print("Zookeeper exercises animals:")
        for a in animals:
            a.roam()
            
    def shutDownZoo(self, animals):
        self.task = "put to sleep all"
        self.task_changed()
        print("Zookeeper shuts down zoo:")
        for a in animals:
            a.goToSleep()