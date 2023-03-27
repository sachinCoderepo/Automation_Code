from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

obj_driver = Service("/home/sachin/Downloads/chromedriver")
driver = webdriver.Chrome(service=obj_driver )

driver.get('https://google.co.in/')
links = driver.find_elements(By.CSS_SELECTOR ,("a"))
images = driver.find_elements(By.CSS_SELECTOR, ("img"))
for link in links:
    r = requests.head(link.get_attribute('href'))
    print(r.status_code == 200)
driver.close()