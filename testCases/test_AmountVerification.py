import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Test_CredKart_CheckOut:


    def test_checkout(self,setup):
        self.driver = setup
        self.driver.get("https://automation.credence.in/login")
        # self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Credenceppb3@test.com")

        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("Credence@123")

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Adding Items to cart
        # click on Macbook Pro
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[3]/div[1]/div[1]/a[2]/h3[1]").click()
        # Click on add to cart
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
        # Click on continue shopping
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[1]").click()
        # Click on headphones
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[2]/h3[1]").click()
        # Click on add to cart
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()
        # Click on continue shopping
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/a[1]").click()
        # click on iPad
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[4]/div[1]/div[1]/a[2]/h3[1]").click()
        # Click on add to cart
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/input[5]").click()

        time.sleep(3)

        # Select quantity from drop down

        l = len(self.driver.find_elements(By.XPATH, '//tbody/tr/td[4]'))
        l = 6

        product_price_list = []

        for r in range(1, l - 2):
            var1 = self.driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            product_price = (var1[1:])
            product_price_list.append(float(product_price))
        subtotal = round((sum(product_price_list)), 2)
        print(product_price_list)
        print('subtotal =' + str(subtotal))

        time.sleep(3)

        system_value_list = []

        for r in range(l - 2, l + 1):
            var2 = self.driver.find_element(By.XPATH, "//tbody/tr[" + str(r) + "]/td[4]").text
            var3 = var2.replace(',', '')
            system_price = var3[1:]
            system_value_list.append(float(system_price))
        # your_total = (sum(system_value_list))
        print(system_value_list)
        # print('your_total =' + str(your_total))

        if subtotal == system_value_list[0]:
            print('Subtotal is matched')
        else:
            print('Subtotal is not matched')

































































































































































































































































