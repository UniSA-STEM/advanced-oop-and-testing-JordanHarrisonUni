'''
File: animal.py
Description: 
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    def __init__(self, name, species, age, diet):
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid name")
        if not isinstance(species, str) or not species:
            raise ValueError("Invalid species")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Invalid age")
        if not isinstance(diet, str) or not diet:
            raise ValueError("Invalid diet")
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet

    def eat(self):
        pass
    def sleep(self):
        pass
    def make_sound(self):
        pass