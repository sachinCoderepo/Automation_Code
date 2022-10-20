from selenium.webdriver.common.by import By
class CheckoutPage:
    # self.driver.find_elements(By.CSS_SELECTOR, "div[class='card h-100']")
    cart = (By.CSS_SELECTOR ,"div[class='card h-100']")
    # product.find_element(By.XPATH, "div/button").click()
    cartButton = (By.XPATH, "div/button")

    def __init__(self ,driver):
        self.driver = driver

    def cartItem(self):
        return self.driver.find_elements(*CheckoutPage.cart)

    def CartFooterButton(self):
        return self.driver.find_element(*CheckoutPage.cartButton)