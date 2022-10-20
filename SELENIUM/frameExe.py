from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
firefox_Option = webdriver.FirefoxOptions()

firefox_Option.add_argument("headless")
obj_2 = Service("/home/sachin/Downloads/geckodriver")
driver = webdriver.Firefox(service = obj_2 , options = firefox_Option)
# driver.get("https://the-internet.herokuapp.com/iframe")
# driver.implicitly_wait(3)

# frame = driver.switch_to.frame("mce_0_ifr")
# driver.find_element(By.CLASS_NAME ,"mce-content-body").clear()
# driver.find_element(By.CLASS_NAME ,"mce-content-body").send_keys("my first exe. on frame")
# driver.switch_to.default_content()
# print(driver.find_element(By.TAG_NAME ,"h3").text)





driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screenshot.png")
driver.switch_to.frame("courses-iframe")
print(driver.find_element(By.LINK_TEXT , "JOIN NOW").text)



