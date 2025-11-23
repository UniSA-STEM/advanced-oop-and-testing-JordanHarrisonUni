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

    # Create animals
    simba = Mammal("Simba", "Lion", 5, "meat")
    polly = Bird("Polly", "Parrot", 2, "seeds")

    print(f"Created animal: {simba.name}, a {simba.species}")
    print(f"Created animal: {polly.name}, a {polly.species}")

    # Create enclosures
    savannah_enclosure = Enclosure(
        "Savannah Habitat",
        "savannah",
        500,
        80,
        [Mammal]
    )

    aviary = Enclosure(
        "Aviary",
        "forest",
        200,
        90,
        [Bird]
    )

    # Add animals to enclosures
    print(savannah_enclosure.add_animal(simba))
    print(aviary.add_animal(polly))

    # Create staff members
    keeper_john = Zookeeper("John")
    vet_emily = Veterinarian("Emily")

    # Assign animals and enclosures to staff
    print(keeper_john.assign_animal(simba))
    print(keeper_john.assign_enclosure(savannah_enclosure))

    print(vet_emily.assign_animal(polly))
    print(vet_emily.assign_enclosure(aviary))

    # Print enclosure status
    print("\nEnclosure Status:")
    print(savannah_enclosure.get_status())
    print(aviary.get_status())

    print("\nStaff Actions\n")

    # Zookeeper feeds animals
    print(keeper_john.feed_animal(simba))

    # Zookeeper cleans the enclosure
    print(keeper_john.clean_enclosure(savannah_enclosure))

    # Veterinarian checks health (no records yet)
    print(vet_emily.check_health(simba))

    # Add a health issue for Simba
    simba_injury = HealthRecord(
        description="Minor leg injury",
        severity="medium",
        date_reported="2025-11-23",
        treatment="Rest"
    )

    print(vet_emily.add_health_issue(simba, simba_injury))

    # Check health again (now shows the issue)
    print(vet_emily.check_health(simba))

    # Vet treats Simba
    print(vet_emily.treat_animal(simba, "Applied bandage and prescribed rest"))

    # Final health summary
    print(vet_emily.check_health(simba))

if __name__ == "__main__":
    main()
