"""Slicing strings"""
from typing import List


def slices(series: str, slice_length: int) -> List[str]:
    """Slice up a string and give all the overlapping sequences
    of a given length

    Args:
        series (string): a string to slice up
        length (int): the required slice length (0 < length <= len(series) accepted)

    Returns:
        An list of all possible string slices of the provided length
    """
    # Sanity check the slice information
    if slice_length < 0:
        raise ValueError("slice length cannot be negative")
    if slice_length == 0:
        raise ValueError("slice length cannot be zero")

    series_length = len(series)

    # Sanity check the series information
    if series_length == 0:
        raise ValueError("series cannot be empty")
    if series_length < slice_length:
        raise ValueError("slice length cannot be greater than series length")

    num_slices = len(series) - slice_length + 1
    if slice_length < 1 or num_slices < 1:
        raise ValueError("Incorrect `length` supplied, needs to be 0 < length <= length of series ")

    return [series[i : i + slice_length] for i in range(0, num_slices)]
