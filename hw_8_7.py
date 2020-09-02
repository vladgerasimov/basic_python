"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real: int, imaginary: int):
        self.real = real
        self.imaginary = imaginary
        self.complex_num = (real, imaginary)

    def __str__(self):
        return f'{self.real} + {self.imaginary}i'

    def __add__(self, other: 'ComplexNumber'):
        return ComplexNumber((self.real + other.real), (self.imaginary + other.imaginary))

    def __mul__(self, other: 'ComplexNumber'):
        return ComplexNumber((self.real * other.real - self.imaginary * other.imaginary),
                             (self.real * other.imaginary + self.imaginary * other.real))


x1 = ComplexNumber(1, -1)

x2 = ComplexNumber(3, 6)

print(x1)
print(x2)

print(x1 + x2)
print(x1 * x2)
