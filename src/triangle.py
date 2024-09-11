from math import sqrt
from figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Длина стороны не может быть <=0")

        # Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Треугольник с такими сторонами не существует")

        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Это треугольник со сторонами {self.a,self.b,self.c}"

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter
        return round(sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))
