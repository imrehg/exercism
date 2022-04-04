def leap_year(year: int) -> bool:
    """Is a year a leap year? Let's ask our experts!"""
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
