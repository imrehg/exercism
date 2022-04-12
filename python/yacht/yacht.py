"""A Yacht scoring calculator"""
from collections import Counter

# Score categories.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice: list[int], category: int) -> int:
    """Calculate score according to the Yacht rules

    Args:
        dice: the numbers rolled by the dice, 5-item list of integer values
        category: one scoring category entered

    Returns:
        the integer score
    """
    counts = Counter(dice)
    most_common_value, most_common_count = counts.most_common()[0]

    if category == YACHT:
        return 50 if most_common_count == 5 else 0

    if category in {ONES, TWOS, THREES, FOURS, FIVES, SIXES}:
        return category * counts[category]

    if category == FULL_HOUSE:
        return sum(dice) if sorted(counts.values()) == [2, 3] else 0

    if category == FOUR_OF_A_KIND:
        return 4 * most_common_value if most_common_count in {4, 5} else 0

    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0

    if category == CHOICE:
        return sum(dice)
