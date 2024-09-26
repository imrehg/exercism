def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if any([d < 0 or d >= input_base for d in digits]):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Convert the input to Base-10 for ease of use:
    base_10_value = sum([digit * input_base**index for index, digit in enumerate(digits[::-1])])

    # Convert to the output base
    output_digits: list[int] = []
    while True:
        base_10_value, remainder = divmod(base_10_value, output_base)
        output_digits.insert(0, remainder)
        if base_10_value == 0:
            break
    return output_digits
