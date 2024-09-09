from typing import TypeAlias

TriangleSides: TypeAlias = list[float]


def equilateral(sides: TriangleSides) -> bool:
    """Check if the set of side lengths can form an equilateral triangle.

    All sides are the same length.
    """
    a, b, c = sides
    return is_triangle(sides) and (a == b == c)


def isosceles(sides: TriangleSides) -> bool:
    """Check if the set of side lengths can form an isosceles triangle.

    At least two sides are the same length.)
    """
    a, b, c = sides
    return is_triangle(sides) and ((a == b) or (b == c) or (a == c))


def scalene(sides: TriangleSides) -> bool:
    """Check if the set of side lengths can form a scalene triangle.

    All sides are different lengths.)
    """
    a, b, c = sides
    return is_triangle(sides) and (a != b != c != a)


def is_triangle(sides: TriangleSides) -> bool:
    """Check if the set of side lengths can form a (non-degenerate) triangle."""
    a, b, c = sides
    return (
        (a > 0)
        and (b > 0)
        and (c > 0)
        and (a + b >= c)
        and (b + c >= a)
        and (a + c >= b)
    )
