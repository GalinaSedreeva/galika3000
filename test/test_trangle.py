import os
import sys

sys.path.append("src")
print(os.getcwd())


from triangle import Triangle
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


def test_triangle_add():
    tri2 = Triangle(3.5, 4.5, 7.5)
    tri3 = Triangle(11, 9, 15)
    assert tri3.add_area(tri2) == 789
