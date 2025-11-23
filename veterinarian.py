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
        super().__init__(name, "Veterinarian")

    def check_health(self, animal):
        if not animal.health_records:
            return f"{animal.name} has no recorded health issues."
        summary = animal.get_health_summary()
        return f"Health records for {animal.name}: {summary}"

    def add_health_issue(self, animal, record):
        animal.add_health_record(record)
        return f"{self.name} added a health record for {animal.name}."

    def treat_animal(self, animal, treatment_description):
        record = HealthRecord(
            description=treatment_description,
            severity="treatment",
            date_reported=date.today().isoformat(),
            treatment=treatment_description
        )
        animal.add_health_record(record)
        return f"{self.name} treated {animal.name}."
