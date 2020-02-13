#Help from:
# https://github.com/jtortorelli/head-first-design-patterns-python/blob/master/src/python/chapter_2/weather_o_rama.py

class Subject:
    def register_observer(self, observer):
        raise NotImplementedError
        
    def remove_observer(self, observer):
        raise NotImplementedError
    
    def notify_observers(self):
        raise NotImplementedError
        
class Observer:
    def update(self, event):
        raise NotImplementedError