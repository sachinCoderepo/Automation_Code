from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

obj_driver = Service("/home/sachin/Downloads/chromedriver")
driver = webdriver.Chrome(service=obj_driver )

driver.get('https://facebook.com')
links = driver.find_elements(By.CSS_SELECTOR ,("a"))
images = driver.find_elements(By.CSS_SELECTOR, ("img"))

for link in links:
    url = link.get_attribute("href")
    r = requests.head(url)
    if r.status_code > 400: 
        print(f"brokenlink ,{url}, stetuscode{(r.status_code)}")
    print(r)

