"""Runs the river simulation by creating and simulating a River object."""

__author__ = "730621803"

from exercises.EX04.river import River

my_river = River(num_fish=10, num_bears=2)
my_river.view_river()
my_river.one_river_week()
