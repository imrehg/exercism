"""Complex Numbers.
See the full description at https://exercism.org/tracks/python/exercises/complex-numbers.
"""

from __future__ import annotations

from math import cos, exp, sin, sqrt
from typing import Any, Callable


# This currently cannot be within the below class, otherwise typing
# errors will occur (even if the code itself is fine), should be the
# same issue as https://github.com/python/mypy/issues/7778
def _cast_other_to_complex_number(
    function: Callable[[ComplexNumber, ComplexNumber], Any]
) -> Callable:
    """Convert a function's second argument to ComplexNumber if applicable."""

    def wrapper_with_converted_input(
        self: ComplexNumber, other: object
    ) -> Any:
        if isinstance(other, (int, float)):
            return function(self, ComplexNumber(other, 0))
        if isinstance(other, ComplexNumber):
            return function(self, other)
        # For any other type
        return NotImplemented

    return wrapper_with_converted_input


class ComplexNumber:
    """A complex numbers implementation."""

    def __init__(self, real: float, imaginary: float) -> None:
        self.real = real
        self.imaginary = imaginary

    @_cast_other_to_complex_number
    def __eq__(self, other: ComplexNumber) -> bool:
        return self.real == other.real and self.imaginary == other.imaginary

    @_cast_other_to_complex_number
    def __radd__(self, other: ComplexNumber) -> ComplexNumber:
        return self + other

    @_cast_other_to_complex_number
    def __add__(self, other: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(
            self.real + other.real, self.imaginary + other.imaginary
        )

    @_cast_other_to_complex_number
    def __rmul__(self, other: ComplexNumber) -> ComplexNumber:
        return self * other

    @_cast_other_to_complex_number
    def __mul__(self, other: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real,
        )

    @_cast_other_to_complex_number
    def __rsub__(self, other: ComplexNumber) -> ComplexNumber:
        return other - self

    @_cast_other_to_complex_number
    def __sub__(self, other: ComplexNumber) -> ComplexNumber:
        return ComplexNumber(
            self.real - other.real, self.imaginary - other.imaginary
        )

    @_cast_other_to_complex_number
    def __rtruediv__(self, other: ComplexNumber) -> ComplexNumber:
        return other / self

    @_cast_other_to_complex_number
    def __truediv__(self, other: ComplexNumber) -> ComplexNumber:
        scaling = abs(other) ** 2
        divided_real = (
            self.real * other.real + self.imaginary * other.imaginary
        ) / scaling
        divided_imaginary = (
            self.imaginary * other.real - self.real * other.imaginary
        ) / scaling
        return ComplexNumber(divided_real, divided_imaginary)

    def __abs__(self) -> float:
        return sqrt((self.real**2) + (self.imaginary**2))

    def conjugate(self) -> ComplexNumber:
        """Calculate the complex conjugate."""
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self) -> ComplexNumber:
        """Calculate complex exponentiation."""
        return exp(self.real) * ComplexNumber(
            cos(self.imaginary), sin(self.imaginary)
        )
