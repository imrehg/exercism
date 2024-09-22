def aliquot_sum(number: int) -> int:
    """Return the sum of the factors of a number.

    :param number: int a positive integer
    :return: int the sum of the factors of the input integer
    """
    return sum(f for f in range(1, number // 2 + 1) if number % f == 0)


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    asum = aliquot_sum(number)
    if asum == number:
        result = "perfect"
    elif asum < number:
        result = "deficient"
    else:
        result = "abundant"
    return result
