from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SuccessPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.message_xpath = "//h1[normalize-space()='Your order has been placed!']"

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, self.message_xpath))).text

    def print_message(self):
        msg = self.get_success_message()
        print(f"Order Success Message: {msg}")
