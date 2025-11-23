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
        super().__init__(name, "Zookeeper")
