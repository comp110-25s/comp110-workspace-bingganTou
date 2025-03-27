"""Dictionary utility functions for EX03."""

__author__ = "730621803"

import pytest
from exercises.ex03.dictionary import invert


def test_invert_normal_case():
    """Test invert with simple key-value pairs."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_single_pair():
    """Test invert with one key-value pair."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_invert_duplicate_value_raises_keyerror():
    """Test invert raises KeyError when duplicate values are present."""
    with pytest.raises(KeyError):
        invert({"kris": "jordan", "michael": "jordan"})


from exercises.ex03.dictionary import count


def test_count_typical_case():
    """Test count with repeated elements."""
    assert count(["apple", "banana", "apple", "cherry"]) == {
        "apple": 2,
        "banana": 1,
        "cherry": 1,
    }


def test_count_all_unique():
    """Test count with all unique items."""
    assert count(["red", "blue", "green"]) == {"red": 1, "blue": 1, "green": 1}


def test_count_empty_list():
    """Test count with an empty list."""
    assert count([]) == {}


from exercises.ex03.dictionary import favorite_color


def test_favorite_color_typical():
    """Test favorite_color with a clear winner."""
    input_data = {"Alice": "blue", "Bob": "blue", "Charlie": "green"}
    assert favorite_color(input_data) == "blue"


def test_favorite_color_all_unique():
    """Test favorite_color when all colors appear once."""
    input_data = {"Amy": "red", "Ben": "blue", "Cody": "green"}
    assert favorite_color(input_data) == "red"  # First encountered


def test_favorite_color_tie_with_first():
    """Test tie case where the first color should be returned."""
    input_data = {"X": "yellow", "Y": "green", "Z": "yellow", "W": "green"}
    assert favorite_color(input_data) == "yellow"


from exercises.ex03.dictionary import bin_len


def test_bin_len_typical():
    """Test bin_len with varied word lengths."""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_with_duplicates():
    """Test bin_len where some words are repeated."""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_empty_list():
    """Test bin_len with an empty list."""
    assert bin_len([]) == {}
