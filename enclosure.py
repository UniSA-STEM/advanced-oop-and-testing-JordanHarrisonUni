'''
File: enclosure.py
Description: Represents an enclosure in the zoo that can house animals.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    def __init__(self, name, environment_type, size, cleanliness_level, allowed_animal_types):

        # Validate data values of given attributes
        # For string instances, we check it is a string and not null
        # For int instances, we check it is an int and meets required conditions
        # For lists (allowed_animal_types), check it is a non-empty list of class types
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid name")
        if not isinstance(environment_type, str) or not environment_type:
            raise ValueError("Invalid environment type")
        if not isinstance(size, int) or size <= 0:
            raise ValueError("Invalid size")
        if not isinstance(cleanliness_level, int) or not (0 <= cleanliness_level <= 100):
            raise ValueError("Invalid cleanliness level")
        if not isinstance(allowed_animal_types, list) or not allowed_animal_types:
            raise ValueError("allowed_animal_types must be a non-empty list of class types")

        for animal_type in allowed_animal_types:
            if not isinstance(animal_type, type):
                raise ValueError("Each entry in allowed_animal_types must be a class type")

        self.name = name
        self.environment_type = environment_type
        self.size = size
        self.cleanliness_level = cleanliness_level
        self.allowed_animal_types = allowed_animal_types

        # Initially the enclosure contains no animals
        self.animals = []

    def add_animal(self, animal):
        # Check if the animal is allowed in this enclosure
        if not any(isinstance(animal, allowed) for allowed in self.allowed_animal_types):
            raise ValueError("This animal type is not allowed in this enclosure.")

        # Prevent duplicate animals being added
        if animal in self.animals:
            return f"{animal.name} is already in {self.name}."

        self.animals.append(animal)
        return f"{animal.name} has been added to {self.name}."

    def remove_animal(self, animal):
        # Remove the animal if present
        if animal in self.animals:
            self.animals.remove(animal)
            return f"{animal.name} has been removed from {self.name}."
        return f"{animal.name} is not in this enclosure."

    def clean(self):
        # Clean the enclosure by resetting cleanliness
        self.cleanliness_level = 100
        return f"{self.name} has been cleaned."

    def get_status(self):
        # Return enclosure information in a readable format
        animal_names = [animal.name for animal in self.animals]
        return (
            f"Enclosure: {self.name}\n"
            f"Environment: {self.environment_type}\n"
            f"Cleanliness: {self.cleanliness_level}%\n"
            f"Animals: {', '.join(animal_names) if animal_names else 'None'}"
        )
