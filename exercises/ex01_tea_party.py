""" Exercise one tea party COMP 110 HW """

__author__: str = "730621803"


def main_planner(guests: int) -> None:
    """It prints out the number of tea bags and treats needed, as well as the
    total cost, for the given number of guests."""
    print("A Cozy Tea Party for", guests, "People!")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        ),
    )


def tea_bags(people: int) -> int:
    """Function that used to count tea bags for the tea party"""
    return people * 2


def treats(people: int) -> int:
    """Compute the total number of treats needed for the given number of people."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """The cost of the tea party(tea bags and treats combined)"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
