import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.CheckOutPage import CredKart_Checkout
from pageObjects.LoginPage import Login


class Test_CredKart_CheckOut:


    def test_checkout(self,setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.driver.get("https://automation.credence.in/login")
        self.lp.Enter_Email("Credenceppb3@test.com")
        self.lp.Enter_Password("Credence@123")
        self.lp.Click_Login_Button()
        self.cop = CredKart_Checkout(self.driver)
        self.cop.click_macbook()
        self.cop.click_addtocart()
        self.cop.click_proceedtocheckout()
        self.cop.enter_firstname("Panchashil")
        self.cop.enter_lastname("Birajdar")
        self.cop.enter_phone("9456787878")
        self.cop.enter_address("Lakshmi Kunj, Narayan Nagar, Latur")
        self.cop.enter_zip("413512")
        self.cop.dropdown_state("Pune")
        self.cop.enter_ownername("Panchashil Birajdar")
        self.cop.enter_cvv("043")
        self.cop.enter_cardnumber("5281")
        self.cop.enter_cardnumber("0370")
        self.cop.enter_cardnumber("4891")
        self.cop.enter_cardnumber("6168")
        self.cop.dropdown_year("2025")
        self.cop.dropdown_month("May")
        self.cop.click_checkout()
        self.cop.dis_successmessage()






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
































































































































































































































































