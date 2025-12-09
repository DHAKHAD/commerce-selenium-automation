from selenium.webdriver.common.by import By
import logging

class LaptopPage():
    def __init__(self, driver):
        self.driver = driver
        self.hp_xpath = "//a[normalize-space()='HP LP3065']"
        logging.info("LaptopPage initialized")

    def click_hp_option(self):
        self.driver.find_element(By.XPATH, self.hp_xpath).click()
        logging.info("Clicked on HP Laptop option")
