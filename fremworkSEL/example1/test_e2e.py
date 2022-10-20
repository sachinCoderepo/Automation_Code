
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
                                                                            
from BaseClass import BaseClass
from HomePage import HomePage
from checkout import CheckoutPage


class TestExample(BaseClass):

    def test_e2e(self):

        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        # self.driver.find_element(By.LINK_TEXT , "Shop").click()
        # products = self.driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")

        checkOutPage = CheckoutPage(self.driver)
        products = checkOutPage.cartItem()
        for product in products:
            productname = product.find_element(By.CSS_SELECTOR, "div h4 a").text
            if productname == "Edge":
                # product.find_element(By.XPATH, "div/button").click()
                button = CheckoutPage(self.driver)
                button.CartFooterButton().click()

        products = self.driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")
        for product in products:
            productname = product.find_element(By.CSS_SELECTOR, "div h4 a").text
            if productname == "iphone X":
                    product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

        self.driver.find_element(By.CSS_SELECTOR, "#country").send_keys("ind")
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located(
                (By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()

        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-lg").click()

        text = "Success! Thank you!"
        output = self.driver.find_element(By.CLASS_NAME, "alert").text
        assert text in output
        print(text)
