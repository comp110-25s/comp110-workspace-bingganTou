"""File to define River class."""

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day = 0
        self.fish = [Fish() for _ in range(num_fish)]
        self.bears = [Bear() for _ in range(num_bears)]

    def check_ages(self):
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_fish(self):
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self):
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
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
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        self.fish = self.fish[amount:]
