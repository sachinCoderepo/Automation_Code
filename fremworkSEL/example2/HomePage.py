from selenium.webdriver.common.by import By
class HomePage:
    
    Name = (By.CSS_SELECTOR , "input[minlength='2']")
    Email = (By.XPATH , "//input[@name='email']")
    Paswrd = (By.XPATH , "//input[@type='password']")
    Checkbox = (By.XPATH , "//input[@type='checkbox']")
    Submitform = (By.CSS_SELECTOR , "input[value = 'Submit']")

    def __init__(self ,driver):
        self.driver = driver


    def getname(self):
        return self.driver.find_element(*HomePage.Name)
    
    def getemail(self):
        return self.driver.find_element(*HomePage.Email)
        
    def getPaswrd(self):
        return self.driver.find_element(*HomePage.Paswrd)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.Checkbox)

    def submitClick(self):
        return self.driver.find_element(*HomePage.Submitform)