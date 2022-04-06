"""A robot with a name (but not yet with a personality)"""
import random
import string


class Robot:
    """A robot that has a name"""

    used_names: set[str] = set()
    MAX_USED_NAMES_COUNT = (
        len(string.ascii_uppercase) ** 2 + len(string.digits) ** 3
    )

    class OutOfNames(Exception):
        """In case we run out of names."""

        pass

    def __init__(self) -> None:
        """Create a robot with its name

        Args:
            None
        """
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

    def reset(self) -> None:
        """Reset the robot name.
        The format is AA111 (capital letters and digits).

        Args:
            None

        Returns:
            None
        """
        # Stop early if we've run out of names to use
        if len(Robot.used_names) == Robot.MAX_USED_NAMES_COUNT:
            raise Robot.OutOfNames

        while True:
            candidate_name = "".join(
                random.choices(string.ascii_uppercase, k=2)
                + random.choices(string.digits, k=3)
            )
            if candidate_name not in Robot.used_names:
                Robot.used_names.add(candidate_name)
                self.__name = candidate_name
                break
