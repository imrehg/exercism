def square(number: int) -> int:
    """Number of grains on a chessboard square given its order."""
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int:
    """The total number of grains on a chessboard according to the doubling rules"""
    # This sum:
    # sum([square(n) for n in range(1, 65)])
    # actually adds up to:
    return 2**64 - 1
