def color_code(color: str) -> int:
    """Find a single color's value."""
    return colors().index(color)


def colors() -> list[str]:
    """List all the resistor colors in value order."""
    return [
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
