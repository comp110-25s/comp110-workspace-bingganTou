"""File to define Bear class."""

__author__ = "730621803"


class Bear:

    def __init__(self):
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        self.hunger_score += num_fish
