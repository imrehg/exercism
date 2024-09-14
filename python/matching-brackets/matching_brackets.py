CLOSE_BRACKET_PAIRS = {"}": "{", "]": "[", ")": "("}


def is_paired(input_string: str) -> bool:
    """Matching them brackets."""
    stack: list[str] = []
    for character in input_string:
        if character in CLOSE_BRACKET_PAIRS.values():
            stack.append(character)
        elif character in CLOSE_BRACKET_PAIRS.keys():
            if not stack or stack.pop() != CLOSE_BRACKET_PAIRS[character]:
                return False
    return not stack
