
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Baseclass import BaseClass


class TestProject1(BaseClass):
    def test_works(self):

        

        self.driver.find_element(By.CSS_SELECTOR, "button[data-test-id='cookie-accept-all']").click()
        # self..find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("sachindwivedi772@gmail.com")
        # self..find_element(By.CSS_SELECTOR, "button[class='button'").click()


        self.driver.find_element(By.CLASS_NAME, "button__Btn-d2s7uk-0.bogQfB").click()
        self.driver.find_element(By.XPATH, "//button[@data-test-id='p8-Kids']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[data-test-id='p8:s1-Clothing']").click()
        self.driver.find_element(By.LINK_TEXT, "Baby Boy Clothes").click()

        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "select[name='sort']"))
        dropdown.select_by_index(1)

        self.driver.find_element(By.CSS_SELECTOR, "input[data-test-id='search-text-input']").send_keys("und")
        brands = self.driver.find_elements(By.CSS_SELECTOR, "div[data-test-id='autocomplete-suggestion']")

        for brand in brands:
            if brand.text == "under armour":
                brand.click()

        self.driver.find_element(By.LINK_TEXT, "Pursuit 3 Trainers").click()
        self.driver.find_element(By.CSS_SELECTOR, "div[data-test-id='10-variant-instock']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[data-test-id='add-to-basket-button-default']").click()
        self.driver.find_element(By.LINK_TEXT, "Checkout").click()







