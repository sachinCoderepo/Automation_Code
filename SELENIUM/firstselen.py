# for selenium import that pkg
from selenium import webdriver
# for any browser import that pkg by its name
from selenium.webdriver.firefox.service import Service
# then you have to create a obj for it and give path of your browser driver
# obj_service = Service("/home/sachin/Downloads/geckodriver")
# then call it by webdriver browser
driver = webdriver.Firefox(executable_path="/home/sachin/Downloads/geckodriver")
# here you have to give  a url for testing
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