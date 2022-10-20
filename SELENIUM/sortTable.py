from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

new_list = []
test_obj = Service("/home/sachin/Downloads/chromedriver")
driver = webdriver.Chrome(service = test_obj)
driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR , "th[role = 'columnheader'").click()
table_list = driver.find_elements(By.CSS_SELECTOR , "tbody tr td:nth-child(1)")
for listtable in table_list:
    new_list.append(listtable.text)
com_list = new_list
new_list.sort()
assert new_list == com_list
print("done")
