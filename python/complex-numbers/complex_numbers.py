from math import cos, exp, sin, sqrt


class ComplexNumber:
    def __init__(self, real: float, imaginary: float) -> None:
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        if isinstance(other, int) or isinstance(other, float):
            return self == ComplexNumber(other, 0)
        # For any other type
        return NotImplemented

    def __radd__(self, other: object) -> "ComplexNumber":
        return self.__add__(other)

    def __add__(self, other: object) -> "ComplexNumber":
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        if isinstance(other, int) or isinstance(other, float):
            return self + ComplexNumber(other, 0)
        # For any other type
        return NotImplemented

    def __rmul__(self, other: object) -> "ComplexNumber":
        return self.__mul__(other)

    def __mul__(self, other: object) -> "ComplexNumber":
        if isinstance(other, ComplexNumber):
            return ComplexNumber(
                self.real * other.real - self.imaginary * other.imaginary,
                self.real * other.imaginary + self.imaginary * other.real,
            )
        if isinstance(other, int) or isinstance(other, float):
            return self * ComplexNumber(other, 0)
        # For any other type
        return NotImplemented

    def __rsub__(self, other: object) -> "ComplexNumber":
        if isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(other, 0) - self
        # For any other type
        return NotImplemented

    def __sub__(self, other: object) -> "ComplexNumber":
        if isinstance(other, ComplexNumber):
            return self.__add__(-1 * other)
        if isinstance(other, int) or isinstance(other, float):
            return self - ComplexNumber(other, 0)
        # For any other type
        return NotImplemented

    def __rtruediv__(self, other: object) -> "ComplexNumber":
        if isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(other, 0) / self
        # For any other type
        return NotImplemented

    def __truediv__(self, other: object) -> "ComplexNumber":
        if isinstance(other, ComplexNumber):
            scaling = abs(other) ** 2
            print(scaling)
            new_real = (self.real * other.real + self.imaginary * other.imaginary) / scaling
            new_imaginary = (self.imaginary * other.real - self.real * other.imaginary) / scaling
            return ComplexNumber(new_real, new_imaginary)
        if isinstance(other, int) or isinstance(other, float):
            return self / ComplexNumber(other, 0)
        # For any other type
        return NotImplemented

    def __abs__(self) -> float:
        return sqrt((self.real**2) + (self.imaginary**2))

    def conjugate(self) -> "ComplexNumber":
        """Calculate the complex conjugate."""
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self) -> "ComplexNumber":
        """Calculate complex exponentiation."""
        return exp(self.real) * ComplexNumber(cos(self.imaginary), sin(self.imaginary))
