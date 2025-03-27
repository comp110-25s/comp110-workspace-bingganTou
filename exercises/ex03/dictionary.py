"""Dictionary utility functions for EX03."""

__author__ = "730621803"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary, swapping keys and values. Raise KeyError if duplicate values found."""
    result: dict[str, str] = {}
    for key in input_dict:
        value = input_dict[key]
        if value in result:
            raise KeyError(f"Duplicate key found when inverting: {value}")
        result[value] = key
    return result


def count(items: list[str]) -> dict[str, int]:
    """Count how many times each string appears in the list."""
    result: dict[str, int] = {}
    for item in items:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Return the most frequently mentioned color in the dictionary of favorite colors."""
    color_counts: dict[str, int] = count(list(favorites.values()))

    max_color: str = ""
    max_count: int = -1

    for color in color_counts:
        if color_counts[color] > max_count:
            max_color = color
            max_count = color_counts[color]

    return max_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Group words into sets by their length."""
    result: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}
    return result
