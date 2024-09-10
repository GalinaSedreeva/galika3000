from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle

rect = Rectangle(4, 5)
square = Square(3)

print("1 Площадь прямоугольника:", rect.get_area)  # Вывод: 20
print("2 Периметр прямоугольника:", rect.get_perimeter, '\n')  # Вывод: 18

print("3 Площадь квадрата:", square.get_area)  # Вывод: 9
print("4 Периметр квадрата:", square.get_perimeter, '\n')  # Вывод: 12

total_area = rect.add_area(square)
print("5 Сумма площадей прямоугольника и квадрата:", total_area, '\n') 

tri1 = Triangle(6,2,5)
print ("6 Периметр первого треугольника ", tri1.get_perimeter)
print ("7 Площадь первого треугольника ",  tri1.get_area, '\n')

tri2 = Triangle(10,22,31)

print ("8 Периметр второго треугольника ", tri2.get_perimeter)
print("9 Площадь второго треугольника ",  tri2.get_area, '\n')

tri3 = Triangle(1,2,3)

total_area_tri = tri1.add_area(tri2)
print("10 Сумма площадей первого и второго треугольников: ", total_area_tri, '\n') 

cir = Circle(10)
print("11 Площадь круга ", cir.get_area)
print ("12 Длина окружности ", cir.get_perimeter)
print("13 Сумма площадей треугольника и круга: ", tri1.add_area(cir), '\n') 
