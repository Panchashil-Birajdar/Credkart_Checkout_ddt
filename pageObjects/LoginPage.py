import time

from selenium.webdriver.common.by import By



class Login:

    Login_link_XPath  = (By.XPATH, "//a[normalize-space()='Login']") #//a[normalize-space()='Login']
    Text_Email_XPATH = (By.XPATH, "//input[@id='email']")
    Text_Password_XPATH = (By.XPATH, "//input[@id='password']")
    Click_Login_Button_XPATH = (By.XPATH, "//button[@type='submit']")
    login_status_XPath = (By.XPATH, "//h2[normalize-space()='CredKart']")
    Menu_Button_Logout_XPath  = (By.XPATH, "//a[@role='button']")
    Logout_Button_XPath  = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self,driver):
        self.driver = driver   # we are writting driver related code so driver is needed

    def Login_link_URL(self):
        self.driver.find_element(*Login.Login_link_XPath).click()

    def Enter_Email(self,email):
        self.driver.find_element(*Login.Text_Email_XPATH).send_keys(email)

    def Enter_Password(self,password):
        self.driver.find_element(*Login.Text_Password_XPATH).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(*Login.Click_Login_Button_XPATH).click()

    def Login_Status(self):
        time.sleep(4)
        try:
            self.driver.find_element(*Login.login_status_XPath)
            return True
        except:
            return False

    def Click_Menu_Button_Logout(self):
        self.driver.find_element(*Login.Menu_Button_Logout_XPath).click()

    def Click_Logout_Button(self):
        self.driver.find_element(*Login.Logout_Button_XPath).click()



































































































































































































































































