from math import sqrt
from figure import Figure

class Triangle(Figure):

    def __init__(self, a,b,c):
        if a<=0 or b<=0 or c<=0:
            raise ValueError("Длина стороны не может быть <=0")
        
        # Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
        if a + b <= c or a + c <= b or b + c <= a:
            print("Треугольник не существует \n")
        
        self.a = a
        self.b = b
        self.c = c
                
    def __str__(self):
        return f"Это треугольник со сторонами {self.a,self.b,self.c}"    
    
    @property
    def get_perimeter(self):
        return (self.a + self.b + self.c)
    
    @property
    def get_area(self):
        p = self.get_perimeter
        return round(sqrt(p*(p-self.a)*(p-self.b)*(p-self.c)))
    