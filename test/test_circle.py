import os
import sys

sys.path.append("src")
print(os.getcwd())


from src.figure import Figure
from src.circle import Circle
import pytest


@pytest.fixture
def prepare_to_det():
    print("\n Начало тестирования вычисления периметра треугольника")

    yield

    print("\n Тестирование вычисления периметра треугольника завершено")


@pytest.fixture
def before_circle_area():
    print("Готовимся к вычислению площади круга")


def test_circle_perimeter(prepare_to_det):
    cir1 = Circle(1)
    assert cir1.perimeter == 6, f"Длина окружности с радиусом 1 должна быть равна 6"


def test_circle_area(before_circle_area):
    cir2 = Circle(2)
    assert cir2.area == 13, f"Площадь круга радиусом 2 должна быть равна 13"

def test_circle_add():
    cir3 = Circle(3)
    cir4 = Circle(4)
    assert cir3.add_area(cir4) == 78, f"Площадь двух окружностей с радиусами 3 и 4 должна быть равна 78"
