import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CredKart_Checkout:
    Click_Product_Macbook_XPATH = (By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']")
    Click_AddToKart_XPATH = (By.XPATH, "//input[@value='Add to Cart']")
    Click_ProceedToCheckout_XPATH = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    Enter_First_Name_XPATH = (By.XPATH, "//input[@id='first_name']")
    Enter_Last_Name_XPATH = (By.XPATH, "//input[@id='last_name']")
    Enter_Phone_XPATH = (By.XPATH, "//input[@id='phone']")
    Enter_Address_XPATH = (By.XPATH, "//textarea[@id='address']")
    Enter_ZIP_XPATH = (By.XPATH, "//input[@id='zip']")
    Dropdown_State_XPATH = (By.XPATH, "//select[@id='state']")
    Enter_Owner_Name_XPATH = (By.XPATH, "//input[@id='owner']")
    Enter_CVV_XPATH = (By.XPATH, "//input[@id='cvv']")
    Enter_Card_Number_XPATH = (By.XPATH, "//input[@id='cardNumber']")
    Dropdown_Year_XPATH = (By.XPATH, "//select[@id='exp_year']")
    Dropdown_Month_XPATH = (By.XPATH, "//select[@id='exp_month']")
    Click_Checkout_XPATH = (By.XPATH, "//button[@id='confirm-purchase']")
    Success_Message_XPATH = (By.XPATH, "/html/body/div/div[1]/p[1]")  # Your order has been placed successfully
    Order_Number_CSS = (By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > p:nth-child(3) > a:nth-child(1)")
    Click_HomePage_XPATH = (By.XPATH, "//a[@class='navbar-brand']")

    def __init__(self, driver):
        self.driver = driver

    def click_macbook(self):
        self.driver.find_element(*CredKart_Checkout.Click_Product_Macbook_XPATH).click()

    def click_addtocart(self):
        self.driver.find_element(*CredKart_Checkout.Click_AddToKart_XPATH).click()

    def click_proceedtocheckout(self):
        self.driver.find_element(*CredKart_Checkout.Click_ProceedToCheckout_XPATH).click()

    def enter_firstname(self, FirstName):
        self.driver.find_element(*CredKart_Checkout.Enter_First_Name_XPATH).send_keys(FirstName)

    def enter_lastname(self, lname):
        self.driver.find_element(*CredKart_Checkout.Enter_Last_Name_XPATH).send_keys(lname)

    def enter_phone(self, mob):
        self.driver.find_element(*CredKart_Checkout.Enter_Phone_XPATH).send_keys(mob)

    def enter_address(self, add):
        self.driver.find_element(*CredKart_Checkout.Enter_Address_XPATH).send_keys(add)

    def enter_zip(self, pincode):
        self.driver.find_element(*CredKart_Checkout.Enter_ZIP_XPATH).send_keys(pincode)

    def dropdown_state(self, cityname):
        city = Select(self.driver.find_element(*CredKart_Checkout.Dropdown_State_XPATH))
        city.select_by_visible_text(cityname)

    def enter_ownername(self, oname):
        self.driver.find_element(*CredKart_Checkout.Enter_Owner_Name_XPATH).send_keys(oname)

    def enter_cvv(self, cvvno):
        self.driver.find_element(*CredKart_Checkout.Enter_CVV_XPATH).send_keys(cvvno)

    def enter_cardnumber(self, cardno):
        self.driver.find_element(*CredKart_Checkout.Enter_Card_Number_XPATH).send_keys(cardno)

    def dropdown_year(self, decade):
        Year = Select(self.driver.find_element(*CredKart_Checkout.Dropdown_Year_XPATH))
        Year.select_by_visible_text(decade)

    def dropdown_month(self, monthly):
        Month = Select(self.driver.find_element(*CredKart_Checkout.Dropdown_Month_XPATH))
        Month.select_by_visible_text(monthly)

    def click_checkout(self):
        self.driver.find_element(*CredKart_Checkout.Click_Checkout_XPATH).click()

    def order_status(self):
        try:
            OrderNumber = self.driver.find_element(*CredKart_Checkout.Order_Number_CSS)
            return True
        except NoSuchElementException:
            return False

    def get_order_number(self):
        try:
            OrderNumber = self.driver.find_element(*CredKart_Checkout.Order_Number_CSS).text
            return OrderNumber
        except NoSuchElementException:
            pass

    def click_HomePage(self):
        self.driver.find_element(*CredKart_Checkout.Click_HomePage_XPATH).click()
