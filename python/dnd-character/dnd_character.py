"""DnD Character Generation"""
import math
import random

ABILITIES = ['strength',
             'dexterity',
             'constitution',
             'intelligence',
             'wisdom',
             'charisma']

class Character:
    """DnD character generator"""
    # List of abilities a character can have
    def __init__(self, character_seed=None):
        self.__random_generator = random.Random(character_seed)
        for ability in ABILITIES:
            setattr(self, ability, self.ability())
        self.hitpoints = 10 + modifier(self.constitution)

    def __dice(self, sides=6):
        """A dice

        Args:
            sides: number of sides, default to good ol' regular 6-sides

        Returns:
            one dice roll value
        """
        return self.__random_generator.randint(1, sides)

    def ability(self):
        """Generate a character ability.

        Args:
            None

        Return:
            an ability value according to the dice rules
        """
        return sum(sorted([self.__dice() for _ in range(4)], reverse=True)[:3])

def modifier(ability_value):
    """Calculate a modifier from an ability's value (mainly used for Constitution)

    Args:
        ability_value: a number value

    Returns:
        the modifier value according to the conversion rules
    """
    return math.floor((ability_value - 10) / 2)
