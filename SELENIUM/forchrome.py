# for selenium import that pkg
from selenium.webdriver.common.by import By
from selenium import webdriver
# for any browser import that pkg by its name
from selenium.webdriver.chrome.service import Service
# then you have to create a obj for it and give path of your browser driver
obj_service = Service("/home/sachin/Downloads/chromedriver")
# then call it by webdriver browser
driver = webdriver.Chrome(service=obj_service)
# here you have to a url for testing
driver.get("https://www.facebook.com/")

# and thats are the basic operation which you can perform on it
print(driver.title)
driver.minimize_window()
driver.get("https://www.hotstar.com/")
driver.maximize_window()
driver.back()
driver.forward()
driver.back()
print(driver.current_url)
driver.maximize_window()
# driver.close()


# that code for fill the internal details and login input
# for finding any element tag have to import By


obj_service = Service("/home/sachin/Downloads/chromedriver")
driver = webdriver.Chrome(service=obj_service)
driver.get("https://www.rahulshettyacademy.com/client/")
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(
    "sachin@123654.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("@123654")
driver.find_element(By.ID, "login").click()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

pri = driver.title
