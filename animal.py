'''
File: animal.py
Description: 
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    def __init__(self, name, species, age, diet, sound):

        # Validate data values of given attributes
        # For string instances, we check it is a string and not null
        # For int instances, we check it is a int and not less than 0, 
        # as age can not be null, but should not be negative
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid name")
        if not isinstance(species, str) or not species:
            raise ValueError("Invalid species")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Invalid age")
        if not isinstance(diet, str) or not diet:
            raise ValueError("Invalid diet")
        if not isinstance(sound, str) or not sound:
            raise ValueError("Invalid sound")
        
        self.name = name
        self.species = species
        self.age = age
        self.diet = diet
        self.sound = sound

    def eat(self):
        return f"{self.name} is eating {self.diet}."

    def sleep(self):
        return f"{self.name} is now sleeping."

    def make_sound(self):
        return f"{self.name} makes a {self.sound} sound."