

class ComplexNumber:

    def __init__(self, re: int = 0, im: int = 0) -> None:
        self.re = re
        self.im = im

    def __add__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(re=self.re + other.re, im=self.im + other.im)

    def __sub__(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(re=self.re - other.re, im=self.im - other.im)

    def __mul__(self, other: "ComplexNumber") -> "ComplexNumber":
        mul_re = self.re * other.re - self.im * other.im
        mul_im = self.re * other.im + self.im * other.re

        return ComplexNumber(re=mul_re, im=mul_im)

    def __truediv__(self, other: "ComplexNumber") -> "ComplexNumber":
        div_re = (self.re * other.re + self.im * other.im) / (other.re ** 2 + other.im**2)
        div_im = (self.im * other.re - self.re * other.im) / (other.re ** 2 + other.im**2)

        return ComplexNumber(re=div_re, im=div_im)

    def __str__(self) -> str:
        return f"{self.re} + {self.im}i" if self.im >= 0 else f"{self.re} - {-self.im}i"

if __name__ == "__main__":
    c = ComplexNumber(2, 2)
    c1 = ComplexNumber(2, 3)

    print(c)
    print(c1)
    print(c + c1)
    print(c - c1)
    print(c * c1)
    print(c / c1)