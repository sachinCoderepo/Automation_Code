from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--egnor-certificate-error")
chromedriverpath = Service("/home/sachin/Downloads/chromedriver")
driver = webdriver.Chrome(service = chromedriverpath ,options = chrome_options)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
print(driver.title)