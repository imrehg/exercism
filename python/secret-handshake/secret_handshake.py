options = ("wink", "double blink", "close your eyes", "jump")


def commands(binary_str: str):
    binary_str = binary_str[::-1]
    steps = [options[digit] for digit in range(0, len(options)) if binary_str[digit] == "1"]
    if binary_str[len(options)] == "1":
        steps = steps[::-1]
    return steps
