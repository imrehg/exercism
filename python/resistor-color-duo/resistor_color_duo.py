"""Resistor Color Duo

https://exercism.org/tracks/python/exercises/resistor-color-duo
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


def value(colors: list[str]) -> int:
    """Calculate resistor value based on the first two color bands"""
    return int(
        "".join([str(RESISTOR_COLORS.index(color)) for color in colors[:2]])
    )
