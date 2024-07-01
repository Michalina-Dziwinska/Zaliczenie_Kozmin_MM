import time

import self
from selenium.common import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class OffersPage:
    def __init__(self, driver):
        self.driver = driver

    def clean_placepicker_input(self):
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="SearchField-input"]')))
        time.sleep(2)
        input_element.click()
        input_element.send_keys(Keys.BACKSPACE)
        input_element.send_keys(Keys.BACKSPACE)
        input_element.send_keys(Keys.BACKSPACE)
        input_element.send_keys("Korea Południowa")
        time.sleep(2)

    def korea_click(self):
        input_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="SearchField-input"]')))
        input_element.send_keys(Keys.ENTER)
        input_element.send_keys(Keys.ENTER)

    def floating_popup_close(self):
        try:

            clickable = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="FloatingCloseButton"]')))

            try:
                clickable.click()
                print("Popup zamknięty.")
            except ElementClickInterceptedException:
                print("Element zablokowany, próba zamknięcia ponownie po krótkiej przerwie.")
                time.sleep(2)
                clickable.click()
                print("Popup zamknięty po ponownej próbie.")
        except (TimeoutException, NoSuchElementException):
            print("Popup nie pojawił się lub nie znaleziono elementu zamykającego popup.")


    def choose_date(self):
        date_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="SearchFormFilters-button-date"]')))
        date_button.click()

    def click_firs_month_button(self):
        try:
            buttons = self.driver.find_elements(By.CSS_SELECTOR,
                                                "div.items-start button[data-test='DealsDatesFilterScrollButton']")
            time.sleep(3)
            if buttons:
                buttons[0].click()
                print(f"Kliknięto pierwszy button: {buttons[0].text}")
                return True
            else:
                print("Nie znaleziono żadnych przycisków do kliknięcia.")
                return False
        except Exception as e:
            print(f"Wystąpił problem podczas klikania przycisku: {e}")
            return False

    def choose_duration(self):
        time.sleep(2)
        duration_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'items-start')]//button[text()='3-5 dni']")))
        duration_button.click()

    def save_button_click(self):
        save_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '[data-test="saveButton"]')))
        save_button.click()

    def are_there_offers(self):
        try:
            no_offers_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Brak wyników')]"))
            )

        except:
            print(f"Na stronie są oferty")
