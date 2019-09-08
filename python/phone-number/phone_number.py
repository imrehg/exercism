"""Phone numbers parsing according to the North American Numbering Plan"""
import string

class Phone:
    """A North American Numbering Plan-compliant phone number"""
    def __init__(self, phone_number):
        self.number, self.area_code, self.prettified_number = parse(phone_number)

    def pretty(self):
        """Return the prettified phone number"""
        return self.prettified_number

def parse(phone_number):
    """Parse a phone number

    Args:
        phone_number: a number string to parse

    Raises:
        ValueError: in case the phone number is not compliant

    Returns:
        number, area code, prettified number tuple
    """
    number = ''

    # First cleanup of punctuation
    for index, char in enumerate(phone_number):
        if char in string.digits:
            number += char
        elif (char == '+' and index > 0) or (char not in ['+', ' ', '-', '(', ')', '.']):
            print(index, char)
            raise ValueError("Invalid punctuation")

    # Check formatting requirements
    number_length = len(number)
    if number_length < 10 or number_length > 11:
        raise ValueError("Wrong phone number length")
    if number_length == 11:
        # Check validcountry code
        if number[0] != '1':
            raise ValueError("Wrong country code")
        # Remove country code
        number = number[1:]
    if number[-10] in ['0', '1'] or number[-7] in ['0', '1']:
        raise ValueError("Invalid digit")

    area_code = number[:3]
    prettified_number = f'({area_code}) {number[3:6]}-{number[6:]}'

    return number, area_code, prettified_number
