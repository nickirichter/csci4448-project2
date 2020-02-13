from observer import Observer

class ZooAnnouncer(Observer):
    def __init__(self, zookeeper):
        self.zookeeper = zookeeper
        self.zookeeper.register_observer(self)
        self.task = None
        
    def update(self, task):
        self.task = task
        self.announce()
        
    def announce(self):
        print("Hi, this is the Zoo Announcer. The Zookeeper is about to", self.task, "the animals!")
        
    def __del__(self):
        print("Zoo is being shut down.")