def rotate_char(char: str, key: int) -> str:
    """Return the rotated character given a rotation key.

    >>> rotate_char('A', 25)
    'X'

    >>> rotate_char('!', 13)
    '!'
    """
    if not char.isalpha():
        return char
    range_lower, range_upper = ("a", "z") if char.islower() else ("A", "Z")
    return chr((ord(char) - ord(range_lower) + key) % (ord(range_upper) - ord(range_lower) + 1) + ord(range_lower))


def rotate(text: str, key: int) -> str:
    """Return the rotation-cipher "encrypted" text.

    >>> rotate("omg", 5)
    trl
    """
    return "".join([rotate_char(char, key) for char in text])
