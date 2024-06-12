import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OffersPage:
    def __init__(self, driver):
        self.driver = driver

    def clean_placepicker_input(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="PlacePickerInputPlace-close"]').click()


    def add_country_input(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="SearchField - input"]').click()


    def search_country(self):
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="SearchField-input"]'))
        )
        input_element.click()
        input_element.send_keys("Korea Południowa")
        input_element.send_keys(Keys.ENTER)