"""Resistor Color Duo.
Full description is at https://exercism.org/tracks/python/exercises/resistor-color-duo.
"""

# Explicit form

RESISTOR_COLOR_MAPPING = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}


def value(colors: list[str]) -> int:
    """Calculate resistor value based on the first two color bands."""
    return RESISTOR_COLOR_MAPPING[colors[0]] * 10 + RESISTOR_COLOR_MAPPING[colors[1]]


# Implicit form

# RESISTOR_COLORS = [
#     "black",
#     "brown",
#     "red",
#     "orange",
#     "yellow",
#     "green",
#     "blue",
#     "violet",
#     "grey",
#     "white",
# ]


# def single_value(color: str) -> int:
#     """Calculate the numeric value of a single color."""
#     return RESISTOR_COLORS.index(color)


# def value(colors: list[str]) -> int:
#     """Calculate resistor value based on the first two color bands."""
#     return single_value(colors[0]) * 10 + single_value(colors[1])
