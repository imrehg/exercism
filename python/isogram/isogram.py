def is_isogram(string: str) -> bool:
    """Return whether a string is an isogram.

    An isogram is a word or phrase without a repeating letter.

    >>> is_isogram("lumberjacks")
    True

    >>> is_isogram("isograms")
    False
    """
    found_letters: set[str] = set()
    for letter in string.lower():
        if not letter.isalpha():
            continue
        if letter in found_letters:
            return False
        found_letters.add(letter)
    return True
