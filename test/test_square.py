from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
import pytest


@pytest.mark.parametrize(
    "a, area",
    [
        (12, 144),
        pytest.param(5, 25, marks=pytest.mark.smoke),
        (1.73, 2.9929),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_square_area(a, area):
    sq2 = Square(a)
    assert sq2.area == area, f"area should be eq {area}"


@pytest.mark.parametrize(
    "a, perimeter",
    [
        (12, 48),
        pytest.param(5, 20, marks=pytest.mark.smoke),
        (1.73, 6.92),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_square_perimeter(a, perimeter):
    sq3 = Square(a)
    assert sq3.perimeter == perimeter, f"perimeter should be eq {perimeter}"


@pytest.mark.parametrize(
    "a, b, sum_area",
    [
        (12, 48, 2448),
        pytest.param(5, 20, 425, marks=pytest.mark.smoke),
        (1.5, 2.5, 8.5),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_square_add_square(a, b, sum_area):
    sq5 = Square(a)
    sq6 = Square(b)
    assert sq6.add_area(sq5) == sum_area, f"Sum sq {a} and {b} must be eq {sum_area}"


@pytest.mark.parametrize(
    "a, b, sum_area",
    [
        (5, 20, 1282),
        pytest.param(3, 15, 716, marks=pytest.mark.smoke),
        (1.5, 2.5, 22.25),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_square_add_circle(a, b, sum_area):
    sq5 = Square(a)
    cir1 = Circle(b)
    assert sq5.add_area(cir1) == sum_area, f"Sum sq {a} and {b} must be eq {sum_area}"


@pytest.mark.parametrize(
    "s, a, b, sum_area",
    [
        (13, 5, 20, 269),
        pytest.param(11, 3, 15, 166, marks=pytest.mark.smoke),
        (0.5, 1.5, 2.6, 4.15),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_square_add_rectangle(s, a, b, sum_area):
    sq5 = Square(s)
    rec5 = Rectangle(a, b)
    assert sq5.add_area(rec5) == sum_area, f"Sum sq {a} and {b} must be eq {sum_area}"


def test_square_negative():
    with pytest.raises(ValueError, match="Длина стороны не может быть <=0"):
        sq = Square(-1)
