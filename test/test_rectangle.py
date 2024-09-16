from src.rectangle import Rectangle
import pytest


@pytest.mark.parametrize(
    "a, b, perimeter",
    [
        (12, 4, 32),
        pytest.param(5, 7, 24, marks=pytest.mark.smoke),
        (1.73, 2.54, 8.54),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_rec_perimeter(a, b, perimeter):
    rec1 = Rectangle(a, b)
    assert rec1.perimeter == perimeter, f"perimeter should be eq {perimeter}"


@pytest.mark.parametrize(
    "a, b, area",
    [
        (12, 4, 48),
        pytest.param(5, 7, 35, marks=pytest.mark.smoke),
        (1.73, 2.54, 4.3942),
    ],
    ids=[
        "integer",
        "smoke",
        "real",
    ],
)
def test_rec_area(a, b, area):
    rec2 = Rectangle(a, b)
    assert rec2.area == area, f"area should be eq {area}"


def test_rec_add():
    rec3 = Rectangle(5, 6)
    rec4 = Rectangle(7, 8)
    assert rec3.add_area(rec4) == 86, "area should be eq 86"


def test_rectangle_negative():
    with pytest.raises(ValueError, match="Длина стороны не может быть <=0"):
        rec = Rectangle(0, 1)
