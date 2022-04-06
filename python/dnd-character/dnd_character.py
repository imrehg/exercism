"""DnD Character Generation"""
import math
import random


class Character:
    """DnD character generator"""

    def __init__(self, character_seed=None) -> None:
        self.__random_generator = random.Random(character_seed)
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def __dice(self, sides: int = 6) -> int:
        """Roll a dice

        Args:
            sides: number of sides, default to good ol' regular 6-sides

        Returns:
            one dice roll value
        """
        return self.__random_generator.randint(1, sides)

    def ability(self) -> int:
        """Generate a character ability.

        Args:
            None

        Return:
            an ability value according to the dice rules
        """
        return sum(sorted([self.__dice() for _ in range(4)], reverse=True)[:3])


def modifier(ability_value: int) -> int:
    """Calculate a modifier from an ability's value (mainly used for Constitution)

    Args:
        ability_value: a number value

    Returns:
        the modifier value according to the conversion rules
    """
    return math.floor((ability_value - 10) / 2)
