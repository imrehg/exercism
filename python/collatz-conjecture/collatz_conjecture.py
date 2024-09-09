def steps(number: int) -> int:
    """Count the number of steps to reach 1 using the Collatz Conjecture."""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step_count = 0
    while number != 1:
        step_count += 1
        number = (number // 2) if (number % 2) == 0 else (3 * number + 1)

    return step_count
