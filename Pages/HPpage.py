from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import logging

class HPpage():
    def __init__(self, driver):
        self.driver = driver
        self.delivery_date_calendar_xpath = "//i[@class='fa fa-calendar']"
        self.add_to_cart_button_xpath = "//button[normalize-space()='Add to Cart']"
        self.cal_month_year_xpath = "//th[@class='picker-switch']"
        self.cal_right_arrow_xpath = "//div[@class='datepicker-days']//th[@class='next'][contains(text(),'›')]"
        self.cal_date_xpath = "//td[normalize-space()="
        logging.info("HPpage initialized")

    def scroll_to_add_to_cart_button(self):
        element = self.driver.find_element(By.XPATH, self.add_to_cart_button_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        logging.info("Scrolled to Add to Cart button")

    def click_delivery_date_calendar(self):
        self.driver.find_element(By.XPATH, self.delivery_date_calendar_xpath).click()
        logging.info("Clicked delivery date calendar")

    def change_delivery_date_calendar(self, date, month_year):
        cal_my = self.driver.find_element(By.XPATH, self.cal_month_year_xpath).text
        while month_year != cal_my:
            self.driver.find_element(By.XPATH, self.cal_right_arrow_xpath).click()
            cal_my = self.driver.find_element(By.XPATH, self.cal_month_year_xpath).text
        cal_date_xpath = self.cal_date_xpath + "'" + date + "']"
        self.driver.find_element(By.XPATH, cal_date_xpath).click()
        logging.info(f"Selected delivery date: {date} {month_year}")

    def click_add_to_cart_button(self):
        self.driver.find_element(By.XPATH, self.add_to_cart_button_xpath).click()
        logging.info("Clicked Add to Cart for HP Laptop")
