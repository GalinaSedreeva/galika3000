from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle

# rect = Rectangle(4, 5)
# square = Square(3)

# print("1 Площадь прямоугольника:", rect.area)  # Вывод: 20
# print("2 Периметр прямоугольника:", rect.perimeter, "\n")  # Вывод: 18

# print("3 Площадь квадрата:", square.area)  # Вывод: 9
# print("4 Периметр квадрата:", square.perimeter, "\n")  # Вывод: 12

# total_area = rect.add_area(square)
# print("5 Сумма площадей прямоугольника и квадрата:", total_area, "\n")

tri1 = Triangle(3.5, 4.5, 7.5)
print("6 Периметр первого треугольника ", tri1.perimeter)
print("7 Площадь первого треугольника ", tri1.area, "\n")

tri2 = Triangle(11, 9, 15)

print("8 Периметр второго треугольника ", tri2.perimeter)
print("9 Площадь второго треугольника ", tri2.area, "\n")

# tri3 = Triangle(1,2,3)

total_area_tri = tri1.add_area(tri2)
print("10 Сумма площадей первого и второго треугольников: ", total_area_tri, "\n")

# cir3 = Circle(3)
# cir4 = Circle(4)
# print("Площадь круга 3 ", cir3.area)
# print("Площадь круга 4 ", cir4.area)
# #print("12 Длина окружности ", cir.perimeter)
# print("Сумма площадей круг: ", cir3.add_area(cir4), "\n")