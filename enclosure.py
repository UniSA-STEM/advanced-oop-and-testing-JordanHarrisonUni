'''
File: enclosure.py
Description: Represents an enclosure in the zoo that can house animals.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, name, environment_type, size, cleanliness_level, allowed_animal_type):

        # Validate string values
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid name")
        if not isinstance(environment_type, str) or not environment_type:
            raise ValueError("Invalid environment type")

        # Validate size
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Invalid size")

        # Validate cleanliness level (0–100)
        if not isinstance(cleanliness_level, int) or not (0 <= cleanliness_level <= 100):
            raise ValueError("Invalid cleanliness level")

        # Validate allowed animal type
        if not isinstance(allowed_animal_type, type):
            raise ValueError("allowed_animal_type must be a class type")

        self.name = name
        self.environment_type = environment_type
        self.size = size
        self.cleanliness_level = cleanliness_level
        self.allowed_animal_type = allowed_animal_type
        
        # Start with an empty list of animals inside the enclosure
        self.animals = []
