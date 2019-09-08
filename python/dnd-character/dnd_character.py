"""DnD Character Generation"""
import math
import random

class Character:
    """DnD character generator"""
    # List of abilities a character can have
    abilities = ['strength',
                 'dexterity',
                 'constitution',
                 'intelligence',
                 'wisdom',
                 'charisma']
    def __init__(self, character_seed=None):
        self.__random_generator = random.Random(character_seed)
        for ability in self.abilities:
            self.__dict__[ability] = self.__generate_ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def __dice(self, sides=6):
        return self.__random_generator.randint(1, sides)

    def __generate_ability(self):
        return sum(sorted([self.__dice() for i in range(4)], reverse=True)[:3])

    def ability(self, ability_name=None):
        """Get a character ability.
        [Aside: this function's role is not clear from the test file, thus
        some assumptions were made]

        Args:
            ability_name: the name of ability to get (optional)

        Return:
            the ability value if name was provided, or the value of a random
            ability if not
        """
        if not ability_name:
            ability_name = random.choice(self.abilities)
        return self.__dict__[ability_name]

def modifier(ability_value):
    """Calculate a modifier from an ability's value (mainly used for Constitution)

    Args:
        ability_value: a number value

    Returns:
        the modifier value according to the conversion rules
    """
    return math.floor((ability_value - 10) / 2)
