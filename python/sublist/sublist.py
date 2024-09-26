"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

from typing import Any

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


# def _contains(list_one: list[Any], list_two: list[Any]) -> bool:


def sublist(list_one: list[Any], list_two: list[Any]) -> int:
    if list_one == list_two:
        return EQUAL

    len_one, len_two = len(list_one), len(list_two)
    flipped = False
    # Flip things around, so that the first string is always the longer
    if len_two > len_one:
        list_one, len_one, list_two, len_two = list_two, len_two, list_one, len_one
        flipped = True

    if len_two == 0:
        return SUPERLIST if not flipped else SUBLIST
    for start_index in range(0, len_one - len_two + 1):
        if list_one[start_index : start_index + len_two] == list_two:
            return SUPERLIST if not flipped else SUBLIST

    return UNEQUAL
