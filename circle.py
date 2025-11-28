import math


def area(r):
    """
    Computes the area of a circle by its radius.

    Args:
        r (number): Circle radius

    Returns:
        Area (number): S = π * r * r

    Example:
        area(3) -> 28.274333882308138
    """
    return math.pi * r * r


def perimeter(r):
    """
    Computes the circumference (perimeter) of a circle by its radius.

    Args:
        r (number): Circle radius

    Returns:
        Perimeter (number): P = 2 * π * r

    Example:
        perimeter(3) -> 18.84955592153876
    """
    return 2 * math.pi * r

