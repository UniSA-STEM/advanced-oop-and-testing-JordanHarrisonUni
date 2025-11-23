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
        super().__init__(name, species, age, diet, "hiss")

    def bask(self):
        return f"{self.name} is basking in the sun."
