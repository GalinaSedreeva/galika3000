from figure import Figure

class Rectangle (Figure):

    def __init__(self, a,b):
        if a<=0 or b<=0:
            raise ValueError("Длина стороны не может быть <=0")
        self.a = a
        self.b = b        
        
    def __str__(self):
        return f"Это прямоугольник со сторонами {self.a,self.b}"    
    
    @property
    def get_perimeter(self):
        return (self.a + self.b) *2
    
    @property
    def get_area(self):
        return self.a*self.b
