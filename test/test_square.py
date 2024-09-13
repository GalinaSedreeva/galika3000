import os
import sys

sys.path.append("src")
print(os.getcwd())


from square import Square


def test_square_area():
    sq2 = Square(2)
    assert sq2.area == 4, "Square side=2, area=4"


def test_square_perimeter():
    sq3 = Square(3)
    assert sq3.perimeter == 12, "Square side=3, perimeter=12"


def test_square_add():
    sq5 = Square(5)
    sq6 = Square(6)
    assert sq6.add_area(sq5) == 61, "Sum sq 5 and 6 must be 61"
