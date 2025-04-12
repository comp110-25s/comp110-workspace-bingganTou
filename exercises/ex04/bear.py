"""File to define Bear class."""

__author__ = "730621803"

"""Defines the Bear class for the river simulation."""


class Bear:
    """Class for Bear"""

    def __init__(self):
        """Initialize a Bear with age 0 and hunger_score 0."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Simulate one day passing for the bear (age increases, hunger decreases)."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Increase hunger_score by the number of fish eaten."""
        self.hunger_score += num_fish
