"""This is my attempt to make a SeeNSay"""

class SeeNSay:
    """SeeNSay Class"""
    def __init__(self, animal, animal_noise):
        """Init Instances"""
        
        self.animal = animal 
        self.animal_noise = animal_noise
        
    def spin(self):
        """Spin will return Aniaml with Noise"""
        return "The %s says %s" % (animal, animal_noise) #prints the animal with the correct animal noise

Pig = ('Pig', 'Oink')
Cat = ('Cat', 'Meow')
Cow = ('Cow', 'Moo')

class Animal:
    """Animal class"""
    def animal_noise(self):
        """Animal Noise Method"""
        pass
    def animal_name(self):
        """Animal Name Method"""
        pass

print(SeeNSay.spin(Pig))
print(SeeNSay.spin(Cat))
print(SeeNSay.spin(Cow))