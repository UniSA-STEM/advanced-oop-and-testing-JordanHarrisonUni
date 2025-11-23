'''
File: main.py
Description: Demonstration script for the zoo management system.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from mammal import Mammal
from bird import Bird
from reptile import Reptile

from enclosure import Enclosure

from staff import Staff
from zookeeper import Zookeeper
from veterinarian import Veterinarian

from health_record import HealthRecord

def main():
    print("Zoo Management System Demo Starting...\n")

    simba = Mammal("Simba", "Lion", 5, "meat")
    polly = Bird("Polly", "Parrot", 2, "seeds")

    print(f"Created animal: {simba.name}, a {simba.species}")
    print(f"Created animal: {polly.name}, a {polly.species}")

if __name__ == "__main__":
    main()
