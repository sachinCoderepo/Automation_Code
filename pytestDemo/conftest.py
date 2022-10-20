import pytest

@pytest.fixture(params=[("chrome","sacnin","100") , ("firefox","abd","diwedi" ), ("edge","00")])
def crossbrowser(request):
    return request.param

    


@pytest.fixture
def dataLoad():
    print("i have some data in below")

    return ["sachin" , "python" , "sachin@gmail.com"]


@pytest.fixture(scope="class")

def setup():
    a=4
    b=7
    print("i run first in program")

    yield #that helps for ending the program with msz or close operation
    print("i clculate the sum at end of program", a+b)

