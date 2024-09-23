from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle
import pytest


@pytest.mark.parametrize(
    "a, b, c, perimeter",
    [
        # (1, 2, 3, 6),
        pytest.param(5, 7, 9, 21, marks=pytest.mark.skip),
        (1.5, 2.5, 3.5, 7.5),
    ],
    ids=[
        #'first',
        "2",
        "real",
    ],
)
def test_triangle_perimeter(a, b, c, perimeter):
    tri1 = Triangle(a, b, c)
    assert tri1.perimeter == perimeter, f"perimeter should be eq {perimeter}"


@pytest.mark.parametrize(
    "a, b, c, area",
    [
        (2, 6, 5, 89),
        pytest.param(5, 7, 9, 238, marks=pytest.mark.smoke),
        (1.5, 2.5, 3.5, 30),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_triangle_area(a, b, c, area):
    tri1 = Triangle(a, b, c)
    assert tri1.area == area, f"area should be eq {area}"


def test_triangle_add_triangle():
    tri2 = Triangle(3.5, 4.5, 7.5)
    tri3 = Triangle(11, 9, 15)
    assert tri3.add_area(tri2) == 789, "Сумма площадей двух треугольников "


def test_triangle_add_circle():
    tri2 = Triangle(3.5, 4.5, 7.5)
    cir10 = Circle(10)
    assert tri2.add_area(cir10) == 442, "Сумма площадей треугольника и круга"


def test_triangle_add_square():
    tri2 = Triangle(3.5, 4.5, 7.5)
    sq10 = Square(10)
    assert tri2.add_area(sq10) == 228, "Сумма площадей треугольника и квадрата"


def test_triangle_add_rectangle():
    tri2 = Triangle(3.5, 4.5, 7.5)
    rec10 = Rectangle(10, 5)
    assert tri2.add_area(rec10) == 178, "Сумма площадей треугольника и прямоугольника"


def test_triange_negative():
    with pytest.raises(ValueError, match="Длина стороны не может быть <=0"):
        tri = Triangle(-1)


def test_triange_negative():
    with pytest.raises(
        ValueError, match="Треугольник с такими сторонами не существует"
    ):
        tri = Triangle(1, 2, 3)
