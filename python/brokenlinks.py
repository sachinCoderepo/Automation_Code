from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_driver = Service("/home/sachin/Downloads/chromedriver")
driver = webdriver.Chrome(service=obj_driver )# options=chrome_opt)
driver.get("https://www.rahulshettyacademy.com/angularpractice/shop")