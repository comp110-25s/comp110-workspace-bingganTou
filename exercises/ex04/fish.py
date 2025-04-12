"""File to define Fish class."""

"""Defines the Fish class for the river simulation."""

__author__ = "730621803"


class Fish:
    """Represents a fish in the river ecosystem."""

    def __init__(self):
        """Initialize a Fish with age 0."""
        self.age = 0

    def one_day(self):
        """Simulate one day passing for the fish (age increases)."""
        self.age += 1
