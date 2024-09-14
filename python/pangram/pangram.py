def is_pangram(sentence: str) -> bool:
    """Return True if the input sentence is a pangram.

    Pangram is a sentence that uses all 26 letters of the English alphabet.

    >>> is_pangram("abcdefghijklmnopqrstuvwxyz")
    True
    """
    sanitized = [char.lower() for char in sentence if char.isalpha()]
    return len(set(sanitized)) == 26
