"""SeeNay Class"""

from random import choice
import random
import string

class SeeNSay:
    """SeeNSay Class"""

    def __init__(self):
        """Initialize Function"""

        pass

    def animals(self, animal, animal_noise):
        """Animals Definition"""

        self.animal = animal
        self.animal_noise = animal_noise

    def spin(self):
        """Spin Function"""
        # print("The %s says %s!") % (self.name, self.noise)
        # names = ['Pig', 'Dog', 'Cow']
        # name = random.choice(names)
        # "".join(choice(name))
        # sounds = ['Oink', 'Ruff', 'Moo']
        # sound = random.choice(sounds)
        # "".join(choice(sound))
        print("The " + self.name + " " + "says " + self.noise)

class Animal:
    """Animal Class"""
    def name(self, name):
        """Name Function"""
        self.name = name
        return self.name

    def noise(self, noise):
        """Noise Function"""
        self.noise = noise
        return self.noise

class Pig(Animal):
    """Pig Class"""
    Pig = SeeNSay()
    Pig.name = "Pig"
    Pig.noise = "Oink"
    Pig.spin()

class Dog(Animal):
    """Dog Class"""
    Dog = SeeNSay()
    Dog.name = "Dog"
    Dog.noise = "Ruff"
    Dog.spin()

class Cow(Animal):
    """Cow Class"""
    Cow = SeeNSay()
    Cow.name = "Cow"
    Cow.noise = "Moo"
    Cow.spin()
