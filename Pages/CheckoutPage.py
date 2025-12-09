from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Guest Checkout
        self.guest_checkout_radiobutton_xpath = "//input[@value='guest']"
        self.continue1_xpath = "//input[@id='button-account']"

        # Billing details
        self.firstname_xpath = "//input[@id='input-payment-firstname']"
        self.lastname_xpath = "//input[@id='input-payment-lastname']"
        self.email_xpath = "//input[@id='input-payment-email']"
        self.telephone_xpath = "//input[@id='input-payment-telephone']"
        self.address1_xpath = "//input[@id='input-payment-address-1']"
        self.city_xpath = "//input[@id='input-payment-city']"
        self.postcode_xpath = "//input[@id='input-payment-postcode']"
        self.country_xpath = "//select[@id='input-payment-country']"
        self.region_xpath = "//select[@id='input-payment-zone']"
        self.continue2_xpath = "//input[@id='button-guest']"

        # Delivery & Payment
        self.continue4_xpath = "//input[@id='button-shipping-method']"
        self.tnc_xpath = "//input[@name='agree']"
        self.continue5_xpath = "//input[@id='button-payment-method']"

        # Confirm order
        self.confirmorder_xpath = "//input[@id='button-confirm']"

    def complete_checkout_options(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.guest_checkout_radiobutton_xpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue1_xpath))).click()

    def enter_billing_details(self, fname, lname, email, tele, add1, city, pcode, country, state):
        self.driver.find_element(By.XPATH, self.firstname_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstname_xpath).send_keys(fname)

        self.driver.find_element(By.XPATH, self.lastname_xpath).clear()
        self.driver.find_element(By.XPATH, self.lastname_xpath).send_keys(lname)

        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

        self.driver.find_element(By.XPATH, self.telephone_xpath).clear()
        self.driver.find_element(By.XPATH, self.telephone_xpath).send_keys(tele)

        self.driver.find_element(By.XPATH, self.address1_xpath).clear()
        self.driver.find_element(By.XPATH, self.address1_xpath).send_keys(add1)

        self.driver.find_element(By.XPATH, self.city_xpath).clear()
        self.driver.find_element(By.XPATH, self.city_xpath).send_keys(city)

        self.driver.find_element(By.XPATH, self.postcode_xpath).clear()
        self.driver.find_element(By.XPATH, self.postcode_xpath).send_keys(pcode)

        Select(self.driver.find_element(By.XPATH, self.country_xpath)).select_by_visible_text(country)
        Select(self.driver.find_element(By.XPATH, self.region_xpath)).select_by_visible_text(state)

    def complete_billing_details(self, fname, lname, email, tele, add1, city, pcode, country, state):
        self.enter_billing_details(fname, lname, email, tele, add1, city, pcode, country, state)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue2_xpath))).click()

    def complete_delivery_method(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue4_xpath))).click()

    def complete_payment_method(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.tnc_xpath))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.continue5_xpath))).click()

    def confirm_order_method(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.confirmorder_xpath))).click()
