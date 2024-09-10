from rectangle import Rectangle
#from figure import Figure


class Square(Rectangle):

    def __init__(self, a):
        if a<=0:
            raise ValueError("Длина стороны не может быть <=0")
        self.a = a
                
    def __str__(self):
        return f"Это квадрат со стороной {self.a}"    
    
    @property
    def get_perimeter(self):
        return (self.a *4)
    
    @property
    def get_area(self):
        return self.a ** 2
