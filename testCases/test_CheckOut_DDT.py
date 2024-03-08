import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckOutPage import CredKart_Checkout
from pageObjects.LoginPage import Login
from utilities import XLutils


class Test_CredKart_CheckOut:
    excel_path = "D:\\Credence\\Assignments\\My Assignments\\Final Revision\\CredKart_Pytest_Project\\testCases\\TestData\\CheckOutTestData.xlsx"

    def test_checkout_DDT(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.driver.get("https://automation.credence.in/login")
        self.lp.Enter_Email("Credenceppb3@test.com")
        self.lp.Enter_Password("Credence@123")
        self.lp.Click_Login_Button()
        self.cop = CredKart_Checkout(self.driver)

        Order_Number = []
        self.row = XLutils.RowCount(self.excel_path, "Sheet1")

        for r in range(2, self.row + 1):
            self.FirstName = XLutils.ReadData(self.excel_path, "Sheet1", r, 2)
            self.LastName = XLutils.ReadData(self.excel_path, "Sheet1", r, 3)
            self.Phone = XLutils.ReadData(self.excel_path, "Sheet1", r, 4)
            self.Address = XLutils.ReadData(self.excel_path, "Sheet1", r, 5)
            self.Zip = XLutils.ReadData(self.excel_path, "Sheet1", r, 6)
            self.State = XLutils.ReadData(self.excel_path, "Sheet1", r, 7)
            self.Owner = XLutils.ReadData(self.excel_path, "Sheet1", r, 8)

            self.cop.click_macbook()
            self.cop.click_addtocart()
            self.cop.click_proceedtocheckout()
            self.cop.enter_firstname(self.FirstName)
            self.cop.enter_lastname(self.LastName)
            self.cop.enter_phone(self.Phone)
            self.cop.enter_address(self.Address)
            self.cop.enter_zip(self.Zip)
            self.cop.dropdown_state(self.State)
            self.cop.enter_ownername(self.Owner)
            self.cop.enter_cvv("043")
            self.cop.enter_cardnumber("5281")
            self.cop.enter_cardnumber("0370")
            self.cop.enter_cardnumber("4891")
            self.cop.enter_cardnumber("6168")
            self.cop.dropdown_year("2025")
            self.cop.dropdown_month("May")
            self.cop.click_checkout()

            if self.cop.order_status() == True:
                Order_Number.append(self.cop.get_order_number())
                XLutils.WriteData(self.excel_path, "Sheet1", r, 9, self.cop.get_order_number())
            else:
                pass

            self.cop.click_HomePage()
        print(len(Order_Number))
        print(Order_Number)
        if len(Order_Number) == (self.row-1):
            assert True
        else:
            assert False









        #
        # self.driver.get("https://automation.credence.in/login")
        # self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credenceppb3@test.com")
        # self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")
        # self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        #
        # self.driver.find_element(By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']").click()
        # self.driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # self.driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        #
        # self.driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys("Panchashil")
        # self.driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Birajdar")
        # self.driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9456787878")
        # self.driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Lakshmi Kunj, Narayan Nagar, Latur")
        # self.driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("413512")
        # state = Select(self.driver.find_element(By.XPATH, "//select[@id='state']"))
        # state.select_by_visible_text("Pune")
        #
        # self.driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Panchashil Birajdar")
        # self.driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")
        # time.sleep(5)
        # # Credit card number = 5281 0370 4891 6168
        # self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
        # self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
        # self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
        # self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")
        # time.sleep(5)
        # Exp_Year = Select(self.driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        # Exp_Year.select_by_visible_text("2025")
        # time.sleep(2)
        # Exp_Month = Select(self.driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        # Exp_Month.select_by_visible_text("May")
        #
        # self.driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
        #
        # print(self.driver.find_element(By.XPATH, "//p[@class='w-lg-50 mx-auto']").text)
































































































































































































































































