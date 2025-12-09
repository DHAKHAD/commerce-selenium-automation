from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
        self.actions = ActionChains(driver)
        logging.info("HomePage initialized")

        self.phone_pda_option_xpath = "//a[normalize-space()='Phones & PDAs']"
        self.laptop_notebook_option_xpath = "//a[normalize-space()='Laptops & Notebooks']"
        self.show_all_laptop_notebook_xpath = "//a[normalize-space()='Show All Laptops & Notebooks']"
        self.cart_button_xpath = "//button[@data-toggle='dropdown']"
        self.checkout_button_xpath = "//strong[normalize-space()='Checkout']"

    def click_phone_pda_option(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.phone_pda_option_xpath))).click()
        logging.info("Clicked on Phones & PDAs option")

    def hover_laptop_notebook_option(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.laptop_notebook_option_xpath)))
        self.actions.move_to_element(element).perform()
        logging.info("Hovered over Laptop & Notebooks menu")

    def click_show_all_laptop_notebook_option(self):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.laptop_notebook_option_xpath)))
        for attempt in range(3):
            try:
                self.actions.move_to_element(element).perform()
                time.sleep(1)
                submenu = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.show_all_laptop_notebook_xpath)))
                submenu.click()
                logging.info("Clicked on 'Show All Laptops & Notebooks'")
                break
            except:
                logging.warning(f"Attempt {attempt+1} failed, retrying...")
                time.sleep(1)
