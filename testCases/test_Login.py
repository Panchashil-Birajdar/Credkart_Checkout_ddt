
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from utilities.Logger import LogGenerator


class Test_credKart_Login():
    log = LogGenerator.loggen()

    def test_pageTitle_001(self,setup):
        self.driver = setup
        self.log.debug("This is debug")
        self.log.critical("This is warning")
        self.log.warning("This is warning")
        self.log.error("This is error")
        self.log.info("This is info")
        # self.log.info("Started testcase")
        # self.log.info("Opening browser")
        # self.log.info("title of page is 'Credkart'")
        # if self.driver.title == "CredKart":
        # #     self.log.info("taking screenshot")
        #     self.driver.save_screenshot(".\\ScreenShots\\test_pageTitle_001_Passed.PNG")
        #     self.driver.close()
        #     # self.log.info("Testcase is passed")
        #     assert True
        # else:
        #     self.log.info("taking screenshot")
        #     self.driver.save_screenshot(".\\ScreenShots\\test_pageTitle_001_Failed.PNG")
        #     self.log.info("Testcase is failed")
        #     self.log.info("Closing browser")
        #     self.driver.close()
        #     assert False
        # self.log.info("Testcase is completed")

    # def test_credKart_Login_002(self,setup):
    #     self.driver = setup
    #     self.lp = Login(self.driver)
    #     self.driver.get("https://automation.credence.in/login")
    #     self.lp.Enter_Email("Credenceppb3@test.com")
    #     self.lp.Enter_Password("Credence@123")
    #     self.lp.Click_Login_Button()
    #     if self.lp.Login_Status() == True:
    #         self.driver.save_screenshot(".\\ScreenShots\\test_credKart_Login_002_Passed.PNG")
    #         assert True
    #     else:
    #         self.driver.save_screenshot(".\\ScreenShots\\test_credKart_Login_002_Failed.PNG")
    #         self.driver.close()
    #         assert False



        # self.driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
        # self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credenceppb3@test.com")
        # self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # try:
        #     self.driver.find_element(By.XPATH,"//h2[normalize-space()='CredKart']")
        #     print("Login testcase is Passed")
        #     self.driver.save_screenshot(".\\ScreenShots\\test_credKart_Login_002_Passed.PNG")
        #     self.driver.close()
        #     assert True
        # except:
        #     print("Login testcase is Failed")
        #     self.driver.save_screenshot(".\\ScreenShots\\test_credKart_Login_002_Failed.PNG")
        #     self.driver.close()
        #     assert False


































































































































































































































































