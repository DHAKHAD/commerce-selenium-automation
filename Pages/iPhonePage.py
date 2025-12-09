from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class iPhonePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        logging.info("iPhonePage initialized")

        self.iphone_image_xpath = "//ul[@class='thumbnails']//li[1]//a[1]"
        self.next_arrow_xpath = "//button[contains(@title,'Next')]"
        self.close_button_xpath = "//button[normalize-space()='×']"
        self.input_quantity_textbox_xpath = "//input[@id='input-quantity']"
        self.add_to_cart_xpath = "//button[@id='button-cart']"

    def click_iphone_image(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.iphone_image_xpath))).click()
        logging.info("Clicked on iPhone image")

    def click_next_arrow(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.next_arrow_xpath))).click()
            logging.info("Clicked Next arrow in slideshow")
        except:
            logging.info("Next arrow not visible")

    def click_close_button(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH, self.close_button_xpath))).click()
            logging.info("Closed slideshow")
        except:
            logging.info("Close button not visible")

    def input_quantity(self, quantity):
        self.click_close_button()
        box = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.input_quantity_textbox_xpath)))
        box.clear()
        box.send_keys(quantity)
        logging.info(f"Entered quantity: {quantity}")

    def click_add_to_cart_button(self):
        box = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_xpath)))
        box.click()
        logging.info("Clicked Add to Cart for iPhone")
