class ComplexDigits:
    def __init__(self, actual, supposed):
        self.actual = actual
        self.supposed = supposed

    def __add__(self, other):
        complex_sum = ComplexDigits(self.actual + other.actual, self.supposed + other.supposed)
        return complex_sum

    def __mul__(self, other):
        complex_multiplication = ComplexDigits(
            self.actual * other.actual - self.supposed * other.supposed,
            self.actual * other.supposed + self.supposed * other.actual
        )
        return complex_multiplication

    def __str__(self):
        return f"{self.actual} + {self.supposed}i"


complex_1 = ComplexDigits(9, 5)
complex_2 = ComplexDigits(-5, 6)


print(f"complex sum: {complex_1 + complex_2}")
print(f"complex multiplication: {complex_1 * complex_2}")
