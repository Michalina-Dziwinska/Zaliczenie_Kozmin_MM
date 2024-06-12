import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class OffersPage:
    def __init__(self, driver):
        self.driver = driver

    def clean_placepicker_input(self):
        place_picker_wait = (WebDriverWait(self.driver, 10).until
         (EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="PlacePickerInputPlace-close"]'))))
        place_picker_wait.click()

    def clean_placepicker_input2(self):
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="SearchField-input"]')))
        input_element.send_keys(Keys.CONTROL + 'a')
        input_element.send_keys(Keys.BACKSPACE)
        input_element.send_keys(Keys.BACKSPACE)


    def add_country_input(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="SearchField - input"]').click()

    def search_country(self):
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="SearchField-input"]'))
        )
        input_element.click()
        input_element.send_keys("Korea Południowa")


    def empty_place_click(self):
        empty_space = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="newSearchForm"]')))
        empty_space.click()
