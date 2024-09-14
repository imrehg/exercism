def square_root(number: int) -> int:
    """Calculate the square root of a number (focusing on natural numbers)."""
    x = scalar_estimate(number)
    # Bakhshali method
    while True:
        a = (number - x * x) / (2 * x)
        b = x + a
        x_new = b - a * a / (2 * b)
        if x_new == x:
            return int(x)
        x = x_new


def scalar_estimate(number: int) -> int:
    """Estimate the square root of a number using a scalar method."""
    n = 0  # the estimated exponent
    a = number
    while a > 100:
        n += 1
        a //= 100

    return (2 * 10**n) if a < 10 else (6 * 10**n)
