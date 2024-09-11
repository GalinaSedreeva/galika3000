from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def perimeter(self): ...

    @property
    @abstractmethod
    def area(self): ...

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("аргумент {figure} должен быть объектом класса Figure")
        return self.area + figure.area
