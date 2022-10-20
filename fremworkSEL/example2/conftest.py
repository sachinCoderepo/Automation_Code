import pytest  
from selenium.webdriver.chrome.service import Service


from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    obj_dri = Service("/home/sachin/Downloads/chromedriver")
    driver = webdriver.Chrome(service= obj_dri)


    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # driver.get("https://www.debenhams.com/page/homeware")

    driver.implicitly_wait(4)
    driver.maximize_window()



    request.cls.driver = driver
    yield
    driver.close()