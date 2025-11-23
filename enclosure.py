'''
File: enclosure.py
Description: 
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, name, environment_type, size, cleanliness_level):
        self.name = name
        self.environment_type = environment_type
        self.size = size
        self.cleanliness_level = cleanliness_level
        self.animals = []