"""Phone numbers parsing according to the North American Numbering Plan"""
import string


class PhoneNumber:
    """A North American Numbering Plan-compliant phone number"""

    def __init__(self, phone_number: str):
        self.number, self.area_code, self.prettified_number = parse(phone_number)

    def pretty(self) -> str:
        """Return the prettified phone number"""
        return self.prettified_number


def parse(phone_number: str) -> tuple[str, str, str]:
    """Parse a phone number

    Args:
        phone_number: a number string to parse

    Raises:
        ValueError: in case the phone number is not compliant

    Returns:
        number, area code, prettified number tuple
    """
    number = ""

    # First cleanup of punctuation
    for index, char in enumerate(phone_number):
        if char in string.digits:
            number += char
        elif char in string.ascii_letters:
            raise ValueError("letters not permitted")
        elif (char == "+" and index > 0) or (char not in ["+", " ", "-", "(", ")", "."]):
            raise ValueError("punctuations not permitted")

    # Check formatting requirements
    number_length = len(number)
    if number_length < 10:
        raise ValueError("incorrect number of digits")
    elif number_length > 11:
        raise ValueError("more than 11 digits")
    if number_length == 11:
        # Check valid country code
        if number[0] != "1":
            raise ValueError("11 digits must start with 1")
        # Remove country code
        number = number[1:]

    area_code = number[:3]
    exchange_code = number[3:6]
    local_number = number[6:]

    if exchange_code.startswith("0"):
        raise ValueError("exchange code cannot start with zero")
    if exchange_code.startswith("1"):
        raise ValueError("exchange code cannot start with one")
    if area_code.startswith("0"):
        raise ValueError("area code cannot start with zero")
    if area_code.startswith("1"):
        raise ValueError("area code cannot start with one")

    prettified_number = f"({area_code})-{exchange_code}-{local_number}"

    return number, area_code, prettified_number
