from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


obj_1 = Service("/home/sachin/Downloads/chromedriver")
driver = webdriver.Firefox(service=obj_1)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element(By.CLASS_NAME, "inputs").send_keys("ind")
countries = driver.find_elements(By.CSS_SELECTOR, ".ui-menu-item")
for country in countries:
    if country.text == "India":
        country.click()
        break
driver.find_element(By.CSS_SELECTOR, "#ctl00_mainContent_rbtnl_Trip_1").click()

driver.find_element(By.CLASS_NAME, "red-arrow-btn").click()
driver.find_element(By.XPATH ,"//a[@value='GOI']").click()

driver.find_element(By.CLASS_NAME, "red-arrow-btn").click()
driver.find_element(By.XPATH ,"//a[@value='BHO']").click()

links = driver.find_elements(By.TAG_NAME ,"a")
for i in links:
    print(i.text)





