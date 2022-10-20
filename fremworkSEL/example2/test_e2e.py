
from selenium.webdriver.common.by import By

from BaseClass import BaseClass
from HomePage import HomePage


class TestFrermwork(BaseClass):
    def test_submitform(self):

        homePage = HomePage(self.driver)

        homePage.getname().send_keys("Sachin")
        homePage.getemail().send_keys("sachin@gamil.com")
        homePage.getPaswrd().send_keys("iamarider")
        homePage.getCheckbox().click()
        homePage.submitClick().click()









