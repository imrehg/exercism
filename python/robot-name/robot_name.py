"""A robot with a name (but not yet with a personality)"""
from random import randrange
from string import ascii_uppercase, digits

# Keeping track of all the names so there are no duplicates
# The format of names is AA111 (capital letters and digits).
ROBOT_NAME_REPOSITORY = [
    letter_1 + letter_2 + number_1 + number_2 + number_3
    for letter_1 in ascii_uppercase
    for letter_2 in ascii_uppercase
    for number_1 in digits
    for number_2 in digits
    for number_3 in digits
]


class Robot:
    """A robot that has a name"""

    def __init__(self, name_seed=None) -> None:
        """Create a robot with a new name."""
        self.reset()

    @property
    def name(self) -> str:
        """Query the name of the robot.

        Args:
            None

        Returns:
            The name string of the robot
        """
        return self.__name

    def reset(self) -> None:
        """Reset the robot name to a random value.

        Args:
            None

        Raises:
            ValueError if robots have run out of names.

        Returns:
            None
        """
        self.__name = ROBOT_NAME_REPOSITORY.pop(randrange(len(ROBOT_NAME_REPOSITORY)))
