'''
File: health_record.py
Description: Represents a single health record for an animal.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class HealthRecord:
    # Validate data values of given attributes
    def __init__(self, description, severity, date_reported, treatment):
        if not isinstance(description, str) or not description:
            raise ValueError("Invalid description")
        if not isinstance(severity, str) or not severity:
            raise ValueError("Invalid severity")
        if not isinstance(date_reported, str) or not date_reported:
            raise ValueError("Invalid date")
        if not isinstance(treatment, str) or not treatment:
            raise ValueError("Invalid treatment")

        self.description = description
        self.severity = severity
        self.date_reported = date_reported
        self.treatment = treatment

    def __str__(self):
        return f"{self.date_reported}: {self.description} ({self.severity}) - Treatment: {self.treatment}"
