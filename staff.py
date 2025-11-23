'''
File: staff.py
Description: Base class for zoo staff members.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    def __init__(self, name, role):
        # Validate staff name
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid name")

        # Validate staff role
        if not isinstance(role, str) or not role:
            raise ValueError("Invalid role")

        # Store basic staff details
        self.name = name
        self.role = role

        # Lists of animals and enclosures this staff member is responsible for
        self.assigned_animals = []
        self.assigned_enclosures = []
