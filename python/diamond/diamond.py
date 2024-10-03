import string

letters = string.ascii_uppercase


def rows(letter: str) -> list[str]:
    letter_index = letters.index(letter)

    steps = list(range(0, letter_index + 1)) + list(reversed(range(0, letter_index)))
    result: list[str] = []
    for row in steps:
        side_buffer = " " * (letter_index - row)
        left_letter = letters[row]
        mid_buffer = " " * ((row - 1) * 2 + 1) if row > 0 else ""
        right_letter = left_letter if row > 0 else ""
        result += [side_buffer + left_letter + mid_buffer + right_letter + side_buffer]

    return result
