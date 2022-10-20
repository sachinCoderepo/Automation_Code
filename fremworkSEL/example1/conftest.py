import pytest  

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service





def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        
        driver = webdriver.Chrome(executable_path="/home/sachin/Downloads/chromedriver" ) 

    elif browser_name == "firefox":
        
        driver = webdriver.Firefox(executable_path= "/home/sachin/Downloads/geckodriver") 

    elif browser_name == "microsoft edge":
        print("microsoft edge")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(4)
    driver.maximize_window()

    # driver.get("https://rahulshettyacademy.com/dropdownsPractise/")


    request.cls.driver = driver
    yield
    driver.close()
   
