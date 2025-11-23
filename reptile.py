'''
File: reptile.py
Description: Reptile subclass of Animal with a default reptile sound.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Reptile(Animal):
    def __init__(self, name, species, age, diet):
        # Reptiles have a default sound of "hiss"
        super().__init__(name, species, age, diet, "hiss")

    def bask(self):
        # Behaviour specific to reptiles
        return f"{self.name} is basking in the sun."
