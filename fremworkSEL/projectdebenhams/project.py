

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj = Service("/home/sachin/Downloads/chromedriver")
driver = webdriver.Chrome(service= obj)
driver.get("https://www.debenhams.com/page/homeware")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, "button[data-test-id='cookie-accept-all']").click()
# driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("sachindwivedi772@gmail.com")
# driver.find_element(By.CSS_SELECTOR, "button[class='button'").click()


driver.find_element(By.CLASS_NAME, "button__Btn-d2s7uk-0.bogQfB").click()
driver.find_element(By.XPATH, "//button[@data-test-id='p8-Kids']").click()
driver.find_element(By.CSS_SELECTOR, "button[data-test-id='p8:s1-Clothing']").click()
driver.find_element(By.LINK_TEXT, "Baby Boy Clothes").click()

dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select[name='sort']"))
dropdown.select_by_index(1)

driver.find_element(By.CSS_SELECTOR, "input[data-test-id='search-text-input']").send_keys("und")
brands = driver.find_elements(By.CSS_SELECTOR, "div[data-test-id='autocomplete-suggestion']")

for brand in brands:
    if brand.text == "under armour":
        brand.click()

driver.find_element(By.LINK_TEXT, "Pursuit 3 Trainers").click()
driver.find_element(By.CSS_SELECTOR, "div[data-test-id='10-variant-instock']").click()
driver.find_element(By.CSS_SELECTOR, "button[data-test-id='add-to-basket-button-default']").click()
driver.find_element(By.LINK_TEXT, "Checkout").click()







