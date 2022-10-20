from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# chrome_opt = webdriver.ChromeOptions()
# chrome_opt.add_argument("headless")

obj_driver = Service("/home/sachin/Downloads/chromedriver")
driver = webdriver.Chrome(service=obj_driver )# options=chrome_opt)
driver.get("https://www.rahulshettyacademy.com/angularpractice/shop")
driver.implicitly_wait(4)
driver.maximize_window()

products = driver.find_elements(By.CSS_SELECTOR ,"div[class='card h-100']")
for product in products:
    productname = product.find_element(By.CSS_SELECTOR , "div h4 a").text
    if productname == "2222222222222Edge":
        product.find_element(By.XPATH , "div/button").click()

products = driver.find_elements(By.CSS_SELECTOR ,"div[class='card h-100']")
for product in products:
    productname = product.find_element(By.CSS_SELECTOR , "div h4 a").text
    if productname == "iphone X":
        product.find_element(By.XPATH , "div/button").click()

driver.find_element(By.CSS_SELECTOR ,".btn-primary").click()
driver.find_element(By.CSS_SELECTOR, ".btn-success").click()

driver.find_element(By.CSS_SELECTOR , "#country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.XPATH ,"//label[@for='checkbox2']").click()
driver.find_element(By.CSS_SELECTOR ,".btn-lg").click()

text = "Success! Thank you!"
output = driver.find_element(By.CLASS_NAME,"alert").text
assert text in output
print(text)


linksWeb = driver.find_elements(By.TAG_NAME, "a")
for i in linksWeb:
    print(i.text)


