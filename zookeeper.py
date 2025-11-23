'''
File: zookeeper.py
Description: Zookeeper staff member responsible for feeding animals and maintaining enclosures.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff

class Zookeeper(Staff):
    def __init__(self, name):
        # Initialise parent Staff class with role "Zookeeper"
        super().__init__(name, "Zookeeper")

    def assign_animal(self, animal):
        # Add an animal to the zookeeper's responsibility list
        # Prevent duplicates for cleaner system behaviour
        if animal in self.assigned_animals:
            return f"{animal.name} is already assigned to {self.name}."
        self.assigned_animals.append(animal)
        return f"{self.name} is now responsible for {animal.name}."

    def assign_enclosure(self, enclosure):
        # Add an enclosure to the zookeeper's responsibility list
        if enclosure in self.assigned_enclosures:
            return f"{enclosure.name} is already assigned to {self.name}."
        self.assigned_enclosures.append(enclosure)
        return f"{self.name} is now assigned to {enclosure.name}."

    def feed_animal(self, animal):
        # A zookeeper may only feed animals they are assigned
        if animal not in self.assigned_animals:
            return f"{self.name} is not assigned to feed {animal.name}."
        return animal.eat()

    def clean_enclosure(self, enclosure):
        # A zookeeper may only clean enclosures they are assigned
        if enclosure not in self.assigned_enclosures:
            return f"{self.name} is not assigned to clean {enclosure.name}."
        return enclosure.clean()
