'''
File: test_enclosure.py
Description: Pytest unit tests for Enclosure functionality.
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
from enclosure import Enclosure
from mammal import Mammal
from bird import Bird

# Fixtures
@pytest.fixture
def simba():
    return Mammal("Simba", "Lion", 5, "meat")

@pytest.fixture
def polly():
    return Bird("Polly", "Parrot", 2, "seeds")

@pytest.fixture
def savannah_enclosure():
    return Enclosure("Savannah", "dry", 500, 80, [Mammal])

@pytest.fixture
def aviary():
    return Enclosure("Aviary", "forest", 200, 90, [Bird])

# Tests
def test_valid_enclosure_constructor(savannah_enclosure):
    assert savannah_enclosure.name == "Savannah"
    assert savannah_enclosure.environment_type == "dry"
    assert savannah_enclosure.size == 500
    assert savannah_enclosure.cleanliness_level == 80
    assert savannah_enclosure.allowed_animal_types == [Mammal]
    assert savannah_enclosure.animals == []

def test_invalid_enclosure_name():
    with pytest.raises(ValueError):
        Enclosure("", "dry", 500, 80, [Mammal])

def test_add_valid_animal(savannah_enclosure, simba):
    result = savannah_enclosure.add_animal(simba)
    assert simba in savannah_enclosure.animals
    assert result == "Simba has been added to Savannah."

def test_add_invalid_animal(savannah_enclosure, polly):
    with pytest.raises(ValueError):
        savannah_enclosure.add_animal(polly)

def test_remove_animal(savannah_enclosure, simba):
    savannah_enclosure.add_animal(simba)
    result = savannah_enclosure.remove_animal(simba)
    assert simba not in savannah_enclosure.animals
    assert result == "Simba has been removed from Savannah."

def test_clean_enclosure(savannah_enclosure):
    savannah_enclosure.cleanliness_level = 20
    msg = savannah_enclosure.clean()
    assert savannah_enclosure.cleanliness_level == 100
    assert msg == "Savannah has been cleaned."

def test_get_status(savannah_enclosure, simba):
    savannah_enclosure.add_animal(simba)
    status = savannah_enclosure.get_status()
    assert "Savannah" in status
    assert "dry" in status
    assert "100" not in status        # cleanliness not forced here
    assert "Simba" in status
