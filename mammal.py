'''
File: mammal.py
Description: Mammal subclass of Animal with a default mammal sound.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, age, diet):
        # Mammals have a default groan sound
        super().__init__(name, species, age, diet, "groan")

    def walk(self):
        # Behaviour specific to mammals
        return f"{self.name} is walking."
