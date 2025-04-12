"""File to define River class."""

__author__ = "730621803"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """Simulates a river ecosystem with bears and fish."""

    def __init__(self, num_fish: int, num_bears: int):
        """Initialize the river with a given number of fish and bears."""
        self.day = 0
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]

    def check_ages(self):
        """Remove fish older than 3 and bears older than 5 from the river."""
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def bears_eating(self):
        """Each bear eats 3 fish if there are at least 5 fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Remove bears with a hunger score below 0."""
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_fish(self):
        """Repopulate the river: every pair of fish produces 4 new fish."""
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """Repopulate the river: every pair of bears produces 1 new bear."""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())

    def view_river(self):
        """Print the current state of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of activity in the river."""
        self.day += 1
        for bear in self.bears:
            bear.one_day()
        for fish in self.fish:
            fish.one_day()
        self.bears_eating()
        self.check_hunger()
        self.check_ages()
        self.repopulate_fish()
        self.repopulate_bears()
        self.view_river()

    def one_river_week(self):
        """Simulate one week in the river ecosystem."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        """Remove a specified number of fish from the start of the list."""
        self.fish = self.fish[amount:]
