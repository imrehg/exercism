"""Space age calculation, your age on different planets"""

EARTH_YEAR = 31557600
YEAR_LENGTH = {
    "mercury": EARTH_YEAR * 0.2408467,
    "venus": EARTH_YEAR * 0.61519726,
    "earth": EARTH_YEAR,
    "mars": EARTH_YEAR * 1.8808158,
    "jupiter": EARTH_YEAR * 11.862615,
    "saturn": EARTH_YEAR * 29.447498,
    "uranus": EARTH_YEAR * 84.016846,
    "neptune": EARTH_YEAR * 164.79132,
}

class SpaceAge:
    """Space age calculation on different planets"""

    def __init__(self, seconds):
        self._seconds = seconds
        for planet in YEAR_LENGTH:
            setattr(self, f'on_{planet}', self.__age_on_planet(planet))

    @property
    def seconds(self):
        """The age in original seconds."""
        return self._seconds

    def __age_on_planet(self, planet):
        """Method generation to calculate the age on a specific planet.

        Args:
            planet: the planet's name

        Return:
            function to return age on that particular planet
        """
        return lambda: round(self.seconds / YEAR_LENGTH[planet], 2)
