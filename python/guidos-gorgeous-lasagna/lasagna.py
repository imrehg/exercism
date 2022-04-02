"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME = 2  # in minutes, per lasagna layer


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the lasagna preparation time.

    :param number_of_layers: int - number of lasagna layers to prepare.
    :return: int - the preparation time derived from 'PREPARATION_TIME'.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the elapsed time for a given preparation and bake time so far.

    :param number_of_layers: int - number of lasagna layers to prepare.
    :param elapsed_bake_time: int - time the lasagna already spent in the oven
    :return: int - total elapsed time so far.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
