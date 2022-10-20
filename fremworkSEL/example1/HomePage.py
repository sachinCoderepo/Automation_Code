
from selenium.webdriver.common.by import By

class HomePage:
    # flight = (By.CLASS_NAME , "inputs")

    shop = (By.LINK_TEXT , "Shop")

    def __init__(self, driver):
        self.driver = driver
        

    # def FlightBooking(self):
    #     return self.driver.find_element(*HomePage.flight)


    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)
    