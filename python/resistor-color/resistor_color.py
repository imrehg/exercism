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


def color_code(color: str) -> int:
    """Find a single color's value."""
    return RESISTOR_COLORS.index(color)


def colors() -> list[str]:
    """List all the resistor colors in value order."""
    return RESISTOR_COLORS
