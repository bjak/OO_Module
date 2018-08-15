"""SeeNay Class"""

from random import choice
import random
import string

class SeeNSay:

    def __init__(self):

        pass

    def animals(self,animal, animal_noise):

        self.animal = animal
        self.animal_noise = animal_noise

    def spin(self):

        ##print("The %s says %s!") % (self.name, self.noise)
        names = ['Pig', 'Dog', 'Cow']
        name = random.choice(names)
        #"".join(choice(animal))
        sounds = ['Oink', 'Ruff', 'Moo']
        sound = random.choice(sounds)
        #"".join(choice(sound))
        print("The " + name + " " + "says " + sound)

class Animal:

    def name(self, name):

        return self.name

    def noise(self, noise):

        return self.noise

class Pig(Animal):

    Pig = SeeNSay()
    Pig.name = "Pig"
    Pig.noise = "Oink"
    Pig.spin()

class Dog(Animal):

    Dog = SeeNSay()
    Dog.name = "Dog"
    Dog.noise = "Ruff"
    Dog.spin()

class Cow(Animal):

    Cow = SeeNSay()
    Cow.name = "Cow"
    Cow.noise = "Moo"
    Cow.spin()
