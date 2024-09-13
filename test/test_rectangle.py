import os
import sys

sys.path.append("src")
print(os.getcwd())

from src.figure import Figure
from src.rectangle import Rectangle
import pytest


def test_rec_perimeter():
    rec1=Rectangle(10,20)
    assert rec1.perimeter == 60

def test_rec_area():
    rec2=Rectangle(2,4)
    assert rec2.area == 8

def test_rec_add():
    rec3=Rectangle(5,6)
    rec4=Rectangle(7,8)
    assert rec3.add_area(rec4) == 86