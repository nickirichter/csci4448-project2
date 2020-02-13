from Zoo import Zoo

class Zookeeper:
    
    def wakeUpAnimals(self, animals):
        print("Zookeeper wakes up animals:")
        for a in animals:
            a.wakeUp()
            
    def rollCall(self, animals):
        print("Zookeeper starts roll call of animals:")
        for a in animals:
            a.makeNoise()
            
    def feed(self, animals):
        print("Zookeeper feeds animals:")
        for a in animals:
            a.eat()
            
    def exercise(self, animals):
        print("Zookeeper exercises animals:")
        for a in animals:
            a.roam()
            
    def shutDownZoo(self, animals):
        print("Zookeeper shuts down zoo:")
        for a in animals:
            a.goToSleep()