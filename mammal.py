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
        super().__init__(name, species, age, diet, "generic mammal sound")
