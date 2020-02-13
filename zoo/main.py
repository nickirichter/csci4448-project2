import numpy as np
from Zoo import Zoo
from Animal import Animal
from Pachyderm import Pachyderm
from Feline import Feline
from Canine import Canine
from Hippo import Hippo
from Elephant import Elephant
from Rhino import Rhino
from Tiger import Tiger
from Lion import Lion
from Feline import Feline
from Cat import Cat
from Wolf import Wolf
from Dog import Dog
from Zookeeper import Zookeeper


def main():
    zk = Zookeeper()

    zoo = []

    hippo1 = Hippo("Henry")
    hippo2 = Hippo("Hailey")

    zoo.append(hippo1)
    zoo.append(hippo2)

    elephant1 = Elephant("Earl")
    elephant2 = Elephant("Ezra")

    zoo.append(elephant1)
    zoo.append(elephant2)

    rhino1 = Rhino("Ron")
    rhino2 = Rhino("Roxie")

    zoo.append(rhino1)
    zoo.append(rhino2)

    tiger1 = Tiger("Tim")
    tiger2 = Tiger("Tina")

    zoo.append(tiger1)
    zoo.append(tiger2)

    lion1 = Lion("Larry")
    lion2 = Lion("Lindsey")

    zoo.append(lion1)
    zoo.append(lion2)

    cat1 = Cat("Charlie")
    cat2 = Cat("Courtney")

    zoo.append(cat1)
    zoo.append(cat2)

    wolf1 = Wolf("Warren")
    wolf2 = Wolf("Wanda")

    zoo.append(wolf1)
    zoo.append(wolf2)

    dog1 = Dog("Danny")
    dog2 = Dog("Daisy")

    zoo.append(dog1)
    zoo.append(dog2)

    zk.wakeUpAnimals(zoo)
    print("---------------------------------")
    zk.rollCall(zoo)
    print("---------------------------------")
    zk.feed(zoo)
    print("---------------------------------")
    zk.exercise(zoo)
    print("---------------------------------")
    zk.shutDownZoo(zoo)

      
  
if __name__== "__main__":
    main()