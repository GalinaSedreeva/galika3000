from src.rectangle import Rectangle
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
    assert cir1.perimeter == 6, "Длина окружности с радиусом 1 должна быть равна 6"


@pytest.mark.parametrize(
    "a, area",
    [
        (12, 452),
        pytest.param(5, 79, marks=pytest.mark.smoke),
        (1.73, 9),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_circle_area(a, area):
    cir2 = Circle(a)
    assert cir2.area == area, f"Площадь круга радиусом {a} должна быть равна {area}"


@pytest.mark.parametrize(
    "a, b, sum_area",
    [
        (12, 48, 7690),
        pytest.param(5, 20, 1336, marks=pytest.mark.smoke),
        (1.73, 4.5, 73),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_circle_add_circle(a, b, sum_area):
    cir3 = Circle(a)
    cir4 = Circle(b)
    assert (
        cir3.add_area(cir4) == sum_area
    ), f"Площадь двух окружностей с радиусами {a} и {b} должна быть равна {sum_area}"


@pytest.mark.parametrize(
    "s, a, b, sum_area",
    [
        (13, 5, 20, 631),
        pytest.param(11, 3, 15, 425, marks=pytest.mark.smoke),
        (0.5, 1.5, 2.6, 4.9),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_circle_add_rectangle(s, a, b, sum_area):
    cir5 = Circle(s)
    rec5 = Rectangle(a, b)
    assert cir5.add_area(rec5) == sum_area, f"Sum sq {a} and {b} must be eq {sum_area}"


def test_circle_negative():
    with pytest.raises(ValueError, match="Радиус не может быть <=0"):
        cir5 = Circle(-1)
