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
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid name")
        if not isinstance(role, str) or not role:
            raise ValueError("Invalid role")

        self.name = name
        self.role = role
        self.assigned_animals = []
        self.assigned_enclosures = []
