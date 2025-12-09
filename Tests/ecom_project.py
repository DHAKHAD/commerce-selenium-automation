import unittest
import time
import csv
import os
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import HtmlTestRunner

from Pages.HomePage import HomePage
from Pages.PhonePDAPage import PhonePDAPage
from Pages.iPhonePage import iPhonePage
from Pages.LaptopPage import LaptopPage
from Pages.HPpage import HPpage
from Pages.CheckoutPage import CheckoutPage
from Pages.SuccessPage import SuccessPage
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup logging
log_folder = "Logs"
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

logging.basicConfig(
    filename=os.path.join(log_folder, f"ecom_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Screenshots folder
screenshots_folder = "Screenshots"
if not os.path.exists(screenshots_folder):
    os.makedirs(screenshots_folder)


class EcomTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Cross-browser option
        browser = os.getenv("BROWSER", "chrome").lower()
        if browser == "firefox":
            cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        logging.info(f"Browser {browser} launched")

    def capture_screenshot(self, name):
        path = os.path.join(screenshots_folder, f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
        self.driver.save_screenshot(path)
        logging.info(f"Screenshot saved: {path}")

    def test_ecommerce_flow(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)

        # Read test data
        with open("data.csv", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            data = next(reader)  # Only one row for simplicity

        try:
            driver.get("http://tutorialsninja.com/demo/")
            logging.info("Opened e-commerce website")

            # Home Page
            home = HomePage(driver)
            home.click_phone_pda_option()

            # Phone & PDA Page
            phone_pda = PhonePDAPage(driver)
            phone_pda.click_iphone_option()

            # iPhone Page
            iphone = iPhonePage(driver)
            iphone.click_iphone_image()
            time.sleep(1)
            for _ in range(5):
                iphone.click_next_arrow()
                time.sleep(0.5)
            iphone.input_quantity(data["iphone_qty"])
            iphone.click_add_to_cart_button()

            # Laptop + HP
            home.hover_laptop_notebook_option()
            time.sleep(1)
            home.click_show_all_laptop_notebook_option()

            lap = LaptopPage(driver)
            lap.click_hp_option()

            hp = HPpage(driver)
            hp.scroll_to_add_to_cart_button()
            hp.click_delivery_date_calendar()
            hp.change_delivery_date_calendar(data["hp_date"], data["hp_month_year"])
            hp.click_add_to_cart_button()

            # Checkout
            wait.until(EC.element_to_be_clickable((By.XPATH, home.cart_button_xpath))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, home.checkout_button_xpath))).click()

            cp = CheckoutPage(driver)
            cp.complete_checkout_options()
            cp.complete_billing_details(
                data["fname"], data["lname"], data["email"], data["telephone"],
                data["address"], data["city"], data["postcode"], data["country"], data["state"]
            )
            cp.complete_delivery_method()
            cp.complete_payment_method()
            cp.confirm_order_method()

            # Success Page
            sp = SuccessPage(driver)
            sp.print_message()

        except Exception as e:
            logging.error(f"Error occurred: {e}")
            self.capture_screenshot("error")
            raise

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info("Test Completed")


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="Reports",
            report_title="Ecommerce Automation Test Report",
            combine_reports=True
        )
    )
