def area(a, h):
    """
    Computes the area of a triangle.

    Args:
        a (number): Length of side a
        h (number): Length of height h

    Returns:
        Area (number): S = a * h / 2

    Example:
        area(3, 4) -> 6.0
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Computes the perimeter of a triangle by its three sides.

    Args:
        a (number): Length of side a
        b (number): Length of side b
        c (number): Length of side c

    Returns:
        Perimeter (number): P = a + b + c

    Example:
        perimeter(3, 4, 5) -> 12
    """
    return a + b + c