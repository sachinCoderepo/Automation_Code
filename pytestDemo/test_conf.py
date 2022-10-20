import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self ,setup):
        print("i will run after the setup1")


    # def test_fixtureDemo2(self):
    #     print("i will run after the setup2")


    # def test_fixtureDemo3(self):
    #     print("i will run after the setup3")