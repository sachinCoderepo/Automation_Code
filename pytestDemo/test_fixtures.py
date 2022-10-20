# we also run a single file by his name like that(py.test file name.py -s)
import pytest

@pytest.fixture()

def setup():
    a=4
    b=7
    print("i run first in program")

    yield #that helps for ending the program with msz or close operation
    print("i clculate the sum at end of program", a+b)

def test_fixtureDemo(setup):
    print("i will run after the setup")