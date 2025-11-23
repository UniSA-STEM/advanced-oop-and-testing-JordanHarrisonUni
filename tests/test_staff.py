'''
File: test_staff.py
Description: Pytest unit tests for Staff, Zookeeper and Veterinarian behaviour.
Author: Jordan Harrison
ID: 110350998
Username: harjd001
This is my own work as defined by the University's Academic Integrity Policy.
'''

import sys
import os
# Add project root to Python import path, otherwise we cannot import our classes as tests
# are all in a subfolder.
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import pytest
from staff import Staff
from zookeeper import Zookeeper
from veterinarian import Veterinarian
from enclosure import Enclosure
from mammal import Mammal
from bird import Bird
from health_record import HealthRecord

# Fixtures
@pytest.fixture
def simba():
    return Mammal("Simba", "Lion", 5, "meat")

@pytest.fixture
def polly():
    return Bird("Polly", "Parrot", 2, "seeds")

@pytest.fixture
def savannah():
    return Enclosure("Savannah", "dry", 500, 80, [Mammal])

@pytest.fixture
def aviary():
    return Enclosure("Aviary", "forest", 200, 90, [Bird])

@pytest.fixture
def keeper():
    return Zookeeper("John")

@pytest.fixture
def vet():
    return Veterinarian("Emily")

# Tests
def test_staff_constructor():
    s = Staff("Alice", "General Staff")
    assert s.name == "Alice"
    assert s.role == "General Staff"
    assert s.assigned_animals == []
    assert s.assigned_enclosures == []

def test_invalid_staff_name():
    with pytest.raises(ValueError):
        Staff("", "Role")

def test_invalid_staff_role():
    with pytest.raises(ValueError):
        Staff("Alice", "")

def test_zookeeper_assignments(keeper, simba, savannah):
    msg1 = keeper.assign_animal(simba)
    msg2 = keeper.assign_enclosure(savannah)
    assert simba in keeper.assigned_animals
    assert savannah in keeper.assigned_enclosures
    assert msg1 == "John is now responsible for Simba."
    assert msg2 == "John is now assigned to Savannah."

def test_zookeeper_duplicate_animal_assignment(keeper, simba):
    keeper.assign_animal(simba)
    msg = keeper.assign_animal(simba)
    assert msg == "Simba is already assigned to John."

def test_zookeeper_duplicate_enclosure_assignment(keeper, savannah):
    keeper.assign_enclosure(savannah)
    msg = keeper.assign_enclosure(savannah)
    assert msg == "Savannah is already assigned to John."

def test_zookeeper_feed_animal(keeper, simba):
    keeper.assign_animal(simba)
    result = keeper.feed_animal(simba)
    assert result == "Simba is eating meat."

def test_zookeeper_feed_unassigned_animal(keeper, simba):
    result = keeper.feed_animal(simba)
    assert result == "John is not assigned to feed Simba."

def test_zookeeper_clean_enclosure(keeper, savannah):
    keeper.assign_enclosure(savannah)
    savannah.cleanliness_level = 10
    result = keeper.clean_enclosure(savannah)
    assert result == "Savannah has been cleaned."
    assert savannah.cleanliness_level == 100

def test_zookeeper_clean_unassigned_enclosure(keeper, savannah):
    result = keeper.clean_enclosure(savannah)
    assert result == "John is not assigned to clean Savannah."

def test_vet_assignments(vet, polly, aviary):
    msg1 = vet.assign_animal(polly)
    msg2 = vet.assign_enclosure(aviary)
    assert polly in vet.assigned_animals
    assert aviary in vet.assigned_enclosures
    assert msg1 == "Emily is now responsible for Polly."
    assert msg2 == "Emily is now assigned to Aviary."

def test_vet_duplicate_animal_assignment(vet, polly):
    vet.assign_animal(polly)
    msg = vet.assign_animal(polly)
    assert msg == "Polly is already assigned to Emily."

def test_vet_duplicate_enclosure_assignment(vet, aviary):
    vet.assign_enclosure(aviary)
    msg = vet.assign_enclosure(aviary)
    assert msg == "Aviary is already assigned to Emily."

def test_vet_check_empty_health(vet, simba):
    result = vet.check_health(simba)
    assert result == "Simba has no recorded health issues."

def test_vet_add_health_issue(vet, simba):
    record = HealthRecord("Leg injury", "medium", "2025-11-23", "rest")
    result = vet.add_health_issue(simba, record)
    assert simba.health_records[0] == record
    assert result == "Emily added a health record for Simba."

def test_vet_treat_animal(vet, simba):
    result = vet.treat_animal(simba, "Bandage applied")
    assert len(simba.health_records) == 1
    assert "treated Simba" in result
    assert "Bandage applied" in str(simba.health_records[0])

def test_invalid_health_description():
    with pytest.raises(ValueError):
        HealthRecord("", "low", "2024-01-01", "rest")

def test_invalid_health_severity():
    with pytest.raises(ValueError):
        HealthRecord("desc", "", "2024-01-01", "rest")

def test_invalid_health_date():
    with pytest.raises(ValueError):
        HealthRecord("desc", "low", "", "rest")

def test_invalid_health_treatment():
    with pytest.raises(ValueError):
        HealthRecord("desc", "low", "2024-01-01", "")

def test_health_record_str():
    record = HealthRecord("cut", "low", "2024-01-01", "bandage")
    text = str(record)
    assert "2024-01-01" in text
    assert "cut" in text
    assert "low" in text
    assert "bandage" in text
