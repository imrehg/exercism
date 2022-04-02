"""Calculating darts scores 🎯"""

import math

"""Darts circle radii and score settings"""
DARTS_RADIUS_SCORE = [{"radius": 1, "score": 10}, {"radius": 5, "score": 5}, {"radius": 10, "score": 1}]


def score(x, y):
    """
    Calculate darts score based on hit location

    Args:
        x, y: hit location carthesian coordinates

    Constants:
        DARTS_RADIUS_SCORE: storing radii and
            corresponding scores

    Return:
        Score relevant to the circle being hit
    """
    distance = math.sqrt(x * x + y * y)
    for circle in DARTS_RADIUS_SCORE:
        if distance <= circle["radius"]:
            return circle["score"]
    # We've missed
    return 0
