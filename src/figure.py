from abc import ABC, abstractmethod

class Figure(ABC):

    @property
    @abstractmethod
    def get_perimeter(self):
        ...

    @property
    @abstractmethod
    def get_area(self):
        ...
    
    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("аргумент {figure} должен быть объектом класса Figure")
        return self.get_area + figure.get_area

