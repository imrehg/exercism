def rotate_char(char: str, key: int) -> str:
    """Return the rotated character given a rotation key.

    >>> rotate_char('A', 25)
    'X'

    >>> rotate_char('!', 13)
    '!'
    """
    if not char.isalpha():
        return char
    range_start = ord("a") if char.islower() else ord("A")
    return chr((ord(char) - range_start + key) % 26 + range_start)


def rotate(text: str, key: int) -> str:
    """Return the rotation-cipher "encrypted" text.

    >>> rotate("omg", 5)
    trl
    """
    return "".join([rotate_char(char, key) for char in text])
