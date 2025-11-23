'''
File: veterinarian.py
Description: Veterinarian staff member responsible for animal health and treatment.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff
from health_record import HealthRecord
from datetime import date

class Veterinarian(Staff):
    def __init__(self, name):
        # Initialise parent Staff class with role "Veterinarian"
        super().__init__(name, "Veterinarian")

    def assign_animal(self, animal):
        # Add an animal to the veterinarian's responsibility list
        # Prevent duplicate assignments
        if animal in self.assigned_animals:
            return f"{animal.name} is already assigned to {self.name}."
        self.assigned_animals.append(animal)
        return f"{self.name} is now responsible for {animal.name}."

    def assign_enclosure(self, enclosure):
        # Add an enclosure to the veterinarian's responsibility list
        if enclosure in self.assigned_enclosures:
            return f"{enclosure.name} is already assigned to {self.name}."
        self.assigned_enclosures.append(enclosure)
        return f"{self.name} is now assigned to {enclosure.name}."

    def check_health(self, animal):
        # Return health information for an animal
        if not animal.health_records:
            return f"{animal.name} has no recorded health issues."
        summary = animal.get_health_summary()
        return f"Health records for {animal.name}: {summary}"

    def add_health_issue(self, animal, record):
        # Add a new health record to the animal
        animal.add_health_record(record)
        return f"{self.name} added a health record for {animal.name}."

    def treat_animal(self, animal, treatment_description):
        # Create and add a treatment record for the animal
        record = HealthRecord(
            description=treatment_description,
            severity="treatment",
            date_reported=date.today().isoformat(),
            treatment=treatment_description
        )

        animal.add_health_record(record)
        return f"{self.name} treated {animal.name}."
