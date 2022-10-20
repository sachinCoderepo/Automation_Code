from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests

obj_driver = Service("/home/sachin/Downloads/chromedriver")
driver = webdriver.Chrome(service=obj_driver )# options=chrome_opt)
driver.get("https://www.rahulshettyacademy.com/angularpractice/shop")
# links = driver.find_elements(By.TAG_NAME , "a")

# for link in links:
#     url = link.get_attribute("href")
#     r = requests.head(url)
#     if r.status_code > 400: 
#         print(f"brokenlink ,{url}, stetuscode{(r.status_code)}")