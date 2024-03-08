
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import Login
from utilities import XLutils


class Test_credKart_Login():

    XlPath = "D:\\Credence\\Assignments\\My Assignments\\Final Revision\\CredKart_Pytest_Project\\testCases\\TestData\\LoginTest.xlsx"
#
#     def test_pageTitle_001(self,setup):
#         self.driver = setup
#         if self.driver.title == "CredKart":
#             self.driver.save_screenshot(".\\ScreenShots\\test_pageTitle_001_Passed.PNG")
#             self.driver.close()
#             assert True
#         else:
#             self.driver.save_screenshot(".\\ScreenShots\\test_pageTitle_001_Failed.PNG")
#             self.driver.close()
#             assert False

    def test_credKart_Login_ddt_006(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        time.sleep(3)
        self.lp.Login_link_URL()
        time.sleep(3)
        # self.lp.Click_Login_Button()
        # time.sleep(3)
        self.row = XLutils.RowCount(self.XlPath,"Sheet1")
        print("Number of rows in excel is" + str(self.row))

        Login_Status_List = []
        for r in range(2,self.row+1):
            self.email = XLutils.ReadData(self.XlPath,"Sheet1",r,2)
            self.password = XLutils.ReadData(self.XlPath,"Sheet1",r,3)
            self.exp_result = XLutils.ReadData(self.XlPath,"Sheet1",r,4)

            self.lp.Login_link_URL()
            self.lp.Enter_Email(self.email)
            self.lp.Enter_Password(self.password)
            self.lp.Click_Login_Button()
            # print(self.lp.Login_Status())


            if self.lp.Login_Status() == True:
                if self.exp_result == "Pass":
                    Login_Status_List.append("Pass")
                    time.sleep(3)
                    self.driver.save_screenshot(".\\ScreenShots\\test_credKart_Login_002_Passed.PNG")
                    self.lp.Click_Menu_Button_Logout()
                    time.sleep(3)
                    self.lp.Click_Logout_Button()
                    time.sleep(3)
                elif self.exp_result == "Fail":
                    Login_Status_List.append("Fail")
                    time.sleep(3)
                    self.driver.save_screenshot(".\\ScreenShots\\test_credKart_Login_002_Passed.PNG")
                    self.lp.Click_Menu_Button_Logout()
                    time.sleep(3)
                    self.lp.Click_Logout_Button()
                    time.sleep(3)
                # assert True

            if self.lp.Login_Status() == False:
                if self.exp_result == "Pass":
                    Login_Status_List.append("Fail")
                    self.driver.save_screenshot(".\\ScreenShots\\test_credKart_Login_002_Failed.PNG")
                    time.sleep(3)
                elif self.exp_result =="Fail":
                    Login_Status_List.append("Pass")
                    # self.lp.Login_link_URL()
                    # self.driver.close()
                    # assert False
        print(Login_Status_List)

        if "Fail" not in Login_Status_List:
            assert True
        else:
            print("The testcase is failed - please check expected results & actual results")
            assert False






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


































































































































































































































































