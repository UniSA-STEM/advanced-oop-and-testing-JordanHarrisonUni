'''
File: veterinarian.py
Description: Veterinarian staff member responsible for animal health and treatment.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff

class Veterinarian(Staff):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")
