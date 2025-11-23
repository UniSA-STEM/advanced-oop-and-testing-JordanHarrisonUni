'''
File: bird.py
Description: Bird subclass of Animal with a default bird sound.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age, diet):
        # Birds have a default sound of "chirp"
        super().__init__(name, species, age, diet, "chirp")

    def fly(self):
        # Behaviour specific to birds
        return f"{self.name} is flying."
