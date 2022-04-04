"""A robot with a name (but not yet with a personality)"""
import random
import string


class Robot:
    """A robot that has a name"""

    def __init__(self, name_seed=None):
        """Create a robot with its name

        Args:
            name_seed: seed to use for name generation (optional)
        """
        self.__random_generator = random.Random(name_seed)
        self.reset()

    @property
    def name(self) -> str:
        """Query the name of the robot

        Args:
            None

        Returns:
            The name string of the robot
        """
        return self.__name

    def reset(self):
        """Reset the robot name.
        The format is AA111 (capital letters and digits).

        Args:
            None

        Returns:
            None
        """
        self.__name = "".join(
            self.__random_generator.choices(string.ascii_uppercase, k=2)
            + self.__random_generator.choices(string.digits, k=3)
        )
