"""Matching Brackets implementation.

https://exercism.org/tracks/python/exercises/matching-brackets
"""

CLOSE_BRACKET_PAIRS = {"}": "{", "]": "[", ")": "("}


def is_paired(input_string: str) -> bool:
    """Return True if brackets are correctly paired, otherwise False.

    >>> is_paired("[]")
    True

    >>> is_paired("[{(")
    False
    """
    stack: list[str] = []
    for character in input_string:
        if character in CLOSE_BRACKET_PAIRS.values():
            stack.append(character)
        elif character in CLOSE_BRACKET_PAIRS.keys():
            if not stack or stack.pop() != CLOSE_BRACKET_PAIRS[character]:
                return False
    return not stack
