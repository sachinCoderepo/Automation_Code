from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from BaseClass import BaseClass
from HomePage import HomePage


class TestExample2(BaseClass):

    def test_xyz(self):
        # self.driver.find_element(By.LINK_TEXT ,"Flight Booking" ).click()
        homepage = HomePage(self.driver)
        homepage.FlightBooking().send_keys("ind")

        # self.driver.find_element(By.CLASS_NAME, "inputs").send_keys("ind")
        countries = self.driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item")
        for country in countries:
            if country.text == "India":
                country.click()
                break
        self.driver.find_element(
            By.CSS_SELECTOR, "#ctl00_mainContent_rbtnl_Trip_1").click()

        self.driver.find_element(By.CLASS_NAME, "red-arrow-btn").click()
        self.driver.find_element(By.XPATH, "//a[@value='GOI']").click()

        # self.driver.find_element(By.CLASS_NAME, "red-arrow-btn").click()
        # self.driver.find_element(By.XPATH, "//a[@value='BHO']").click()
