import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class OffersPage:
    def __init__(self, driver):
        self.driver = driver

    def clean_placepicker_input(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="PlacePickerInputPlace-close"]').click()


    def add_country_input(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="SearchField - input"]').click()


    def search_country(self):
        input_element = self.driver.find_element(By.CSS_SELECTOR, '[data-test="SearchField - input"]').click()
        input_element.send_keys("Korea Południowa")
        time.sleep(4)
        #input_element.send_keys(Keys.ENTER)