'''
File: test_animal.py
Description: Pytest unit tests for the Animal and subclass behaviour.
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
from animal import Animal
from mammal import Mammal
from bird import Bird
from reptile import Reptile

# Fixtures
@pytest.fixture
def simba():
    return Animal("Simba", "Lion", 5, "meat", "roar")

@pytest.fixture
def mammal_simba():
    return Mammal("Simba", "Lion", 5, "meat")

@pytest.fixture
def polly():
    return Bird("Polly", "Parrot", 2, "seeds")

@pytest.fixture
def rex():
    return Reptile("Rex", "Lizard", 1, "insects")

# Tests
def test_animal_valid_constructor(simba):
    assert simba.name == "Simba"
    assert simba.species == "Lion"
    assert simba.age == 5
    assert simba.diet == "meat"
    assert simba.sound == "roar"

def test_animal_invalid_age():
    with pytest.raises(ValueError):
        Animal("Simba", "Lion", -1, "meat", "roar")

def test_animal_invalid_name():
    with pytest.raises(ValueError):
        Animal("", "Lion", 5, "meat", "roar")

def test_animal_eat(simba):
    assert simba.eat() == "Simba is eating meat."

def test_animal_sleep(simba):
    assert simba.sleep() == "Simba is now sleeping."

def test_animal_make_sound(simba):
    assert simba.make_sound() == "Simba makes a roar sound."

def test_mammal_sound(mammal_simba):
    assert mammal_simba.sound == "generic mammal sound"

def test_bird_sound(polly):
    assert polly.sound == "chirp"

def test_reptile_sound(rex):
    assert rex.sound == "hiss"
