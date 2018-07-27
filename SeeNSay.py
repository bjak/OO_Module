"""This is my attempt to make a SeeNSay"""

class SeeNSay:
    """SeeNSay Class"""
    def spin(self, animal, animal_noise):
        """Spinning will print the corresponding animal name with its sound"""
        self.animal = animal 
        self.animal_noise = animal_noise
        return "The %s says %s" % (self.animal, self.animal_noise) #prints the animal with the correct animal noise

class Animal:
    """Animal class"""
    def animal_noise(self, noise):
        """Animal Noise Method"""
        self.noise = noise
        pass
    def animal_name(self, name):
        """Animal Name Method"""
        self.name = name
        pass

class Pig(Animal):
    """Pig Subclass"""
    def pig_name(self):
        """Pig Name"""
        return self.name = "Pig"
    def pig_noise(self):
        """Pig Noise"""
        return self.noise = "Oink"

class Cow(Animal):
    """Cow Subclass"""
    def cow_name(self):
        """Cow Name"""
        return self.name = "Cow"
    def cow_noise(self):
        """Cow Noise"""
        return self.noise = "Moo"

class Cat(Animal):
    """Cat Subclass"""
    def cat_name(self):
        """Cat Name"""
        return self.name = "Cat"
    def cat_noise(self):
        """Cat Noise"""
        return self.noise = "Meow"
