from math import pi
from figure import Figure


class Circle(Figure):
    def __init__(self, a):
        if a <= 0:
            raise ValueError("Радиус не может быть <=0")
        self.a = a

    def __str__(self):
        return f"Это круг с радиусом {self.a}"

    @property
    def perimeter(self):
        return round(self.a * 2 * pi)

    @property
    def area(self):
        return round(self.a * self.a * pi)
