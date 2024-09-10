import re

isbn_allowed_format = re.compile(r"^\d{9}[\dX]$")


def is_valid(isbn: str) -> bool:
    """Test a validity of an ISBN-10 number.

    >>> is_valid("3-598-21507-X")
    True

    >>> is_valid("3-598-21515-X"
    False
    """
    isbn = isbn.replace("-", "")
    if isbn_allowed_format.match(isbn):
        digits = [int(d) if d != "X" else 10 for d in isbn]
        result = sum(d * (10 - i) for i, d in enumerate(digits)) % 11 == 0
    else:  # invalid format
        result = False
    return result
