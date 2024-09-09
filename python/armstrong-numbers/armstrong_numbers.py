def is_armstrong_number(number: int) -> bool:
    """Check if a number is an Armstrong number."""
    digits = [int(digit) for digit in str(number)]
    exponent = len(digits)
    return sum([digit**exponent for digit in digits]) == number
