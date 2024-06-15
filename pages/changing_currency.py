from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ChangeCurrency:

    def __init__(self, driver):
        self.driver = driver

    def click_on_currency(self):
        top_nav_region_button = (WebDriverWait(self.driver, 10).until
            (EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test= "TopNav-RegionalSettingsButton"]'))))
        top_nav_region_button.click()

        time.sleep(5)

    def select_language(self):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test= "LanguageSelect"]')))

        select = Select(dropdown)
        select.select_by_value("it")
        time.sleep(2)

        selected_option = select.first_selected_option
        assert selected_option.get_attribute("value") == "it"
        print("Test passed: The 'en' option was successfully selected.")

    def select_currency(self):
        currency = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test= "CurrencySelect"]')))

        select = Select(currency)
        select.select_by_value("eur")

        selected_option = select.first_selected_option
        assert selected_option.get_attribute("value") == "eur"
        print("Test passed: The 'EUR' option was successfully selected.")

    def click_assign_button(self):
        assign_button = (WebDriverWait(self.driver, 10).until
            (EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '[data-test= "SubmitRegionalSettingsButton"]'))))
        assign_button.click()

        time.sleep(5)
