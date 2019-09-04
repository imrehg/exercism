"""Slicing strings"""

def slices(series, length):
    """Slice up a string and give all the overlapping sequences
    of a given length

    Args:
        series (string): a string to slice up
        length (int): the required slice length (0 < length <= len(series) accepted)

    Returns:
        An list of all possible string slices of the provided length
    """
    num_slices = len(series) - length + 1
    if length < 1 or num_slices < 1:
        raise ValueError("Incorrect `length` supplied, needs to be 0 < length <= length of series ")
    return [series[i:i+length] for i in range(0, num_slices)]
