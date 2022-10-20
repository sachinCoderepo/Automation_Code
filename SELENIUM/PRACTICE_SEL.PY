
from selenium.webdriver import ActionChains
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument("headless")

obj_driver = Service("/home/sachin/Downloads/geckodriver")
driver = webdriver.Chrome(service=obj_driver , options=chrome_opt)
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()



# if you did not know where the button actul have then go for with it
radio_buttons = driver.find_elements(By.CSS_SELECTOR , "input[type='radio']")
for button in radio_buttons:
    if button.get_attribute("value") == "radio2":
        button.click()
        button.is_selected()
        break

# if you know where the button has the you can direct click on it
radio_buttons[2].click()
assert radio_buttons[2].is_selected()



# if we did not know where the checkbox come and no name and id attribute there so 
# you have to go with like that
checkboxs = driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
for checkbox in checkboxs:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        break
assert checkbox.is_selected()


# Static dropdown with select method
dropdown = Select(driver.find_element(By.ID ,"dropdown-class-example"))
dropdown.select_by_index(3)

# .is_displayed() function is used to check text is displayed or not
assert driver.find_element(By.ID ,"displayed-text").is_displayed()

# when you  have a java script popup button or alert then that way you can click on it
name = "sachin dwivedi"
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
# using .switch_to.alert function you can switch 
alert = driver.switch_to.alert
alert_text = alert.text
alert.accept()
assert name in alert_text
print(alert_text)

# that is for cancle
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
assert name in alert_text
print(alert_text)
alert.dismiss()


driver.find_element(By.ID , "autocomplete").send_keys("ind")
time.sleep(2)

countries = driver.find_elements(By.CSS_SELECTOR , "ul[id ='ui-id-1'] li")
print(countries)
for country in countries:
    if country.text == "India":
        country.click()
        break


action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID , "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()