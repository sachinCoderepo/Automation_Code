# that code for fill the internal details and login input
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
# for finding any element tag have to import By
from selenium.webdriver.common.by import By



obj_service = Service("/home/sachin/Downloads/geckodriver")
driver = webdriver.Firefox(service = obj_service)
driver.get("https://www.facebook.com/")
pri= driver.title

# here you can find a element by its....
# NAME , ID , LINKTEST ,CSSselectors , CLASSNAME , XPATH
driver.find_element(By.ID , "email").send_keys("sachindiwedi4516@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("457841689")
# for xpath you have to write like that //tag name[@attribute="value"]
driver.find_element(By.XPATH, "//button[@type='submit']").click()
driver.back()
driver.find_element(By.CLASS_NAME, "_6ltj").click()
# and for css selector write like that tag name[attribute ="value"]
driver.find_element(By.CSS_SELECTOR, "input[type='text']").send_keys("7999215414")

driver.find_element(By.CSS_SELECTOR, "button[value='1'").click()
assert "sign" in pri