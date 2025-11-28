def area(a, b):
    """
    Computes the area of a rectangle by its sides.

    Args:
        a (number): Length of side a
        b (number): Length of side b

    Returns:
        Area (number): S = a * b

    Example:
        area(3, 5) -> 15
    """
    return a * b


def perimeter(a, b):
    """
    Computes the perimeter of a rectangle by its sides.

    Args:
        a (number): Length of side a
        b (number): Length of side b

    Returns:
        Perimeter (number): P = 2 * (a + b)

    Example:
        perimeter(3, 5) -> 16
    """
    return 2 * (a + b)