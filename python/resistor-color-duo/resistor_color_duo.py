"""Resistor Color Duo.
Full description is at https://exercism.org/tracks/python/exercises/resistor-color-duo.
"""


RESISTOR_COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def single_value(color: str) -> int:
    """Calculate the numeric value of a single color."""
    return RESISTOR_COLORS.index(color)


def value(colors: list[str]) -> int:
    """Calculate resistor value based on the first two color bands."""
    return single_value(colors[0]) * 10 + single_value(colors[1])
