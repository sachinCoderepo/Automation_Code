# that are run by the name as credit card by (-k method name)
import pytest


def testr_Credit_card():
    print("i am print by the mathod name")

# that is run by py.test -m smoke -v -s
@pytest.mark.smoke
def test_sum():
    a=5
    b=8
    print("sum = ",a+b)


def test_sbiCredit_card():
    print("i am print by the mathod name")


@pytest.mark.skip
def test_skiped():
    print("i am skiped by the user")


@pytest.mark.xfail
def test_errorfile():
    print("i have bug in program")
    a = 5
    b= 6
    assert a == b





def test_crossbrowser(crossbrowser):
    print(crossbrowser)