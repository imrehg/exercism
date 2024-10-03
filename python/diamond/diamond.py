import string

letters = string.ascii_uppercase

# Iteration 1
# def rows(letter: str) -> list[str]:
#     letter_index = letters.index(letter)

#     steps = list(range(0, letter_index + 1)) + list(reversed(range(0, letter_index)))
#     result: list[str] = []
#     for row in steps:
#         side_buffer = " " * (letter_index - row)
#         left_letter = letters[row]
#         mid_buffer = " " * ((row - 1) * 2 + 1) if row > 0 else ""
#         right_letter = left_letter if row > 0 else ""
#         result += [side_buffer + left_letter + mid_buffer + right_letter + side_buffer]
#     return result


# Iteration 2
def rows(letter: str) -> list[str]:
    letter_index = letters.index(letter)
    alphabet = letters[0:letter_index] + letters[letter_index::-1]
    column_alphabet = letters[letter_index::-1] + letters[1 : letter_index + 1]
    result = ["".join(char if char == column_char else " " for column_char in column_alphabet) for char in alphabet]
    return result
