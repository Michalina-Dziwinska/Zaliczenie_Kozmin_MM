from selenium.common import ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FirstLogin:
    def __init__(self, driver):
        self.driver = driver

    def first_login_via_email(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="MagicLogin-LoginViaEmail"]').click()

    def insert_email(self):
        email = 'martastachyra94@gmail.com'
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="MagicLogin-Email"]').send_keys(email)

    def click_on_continue_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="MagicLogin-Continue"]').click()

    def insert_password(self):
        try:
            password = 'kIWI2024@!'
            password_time_field = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='MagicLogin-Password']")))
            password_time_field.click()
            self.driver.execute_script("arguments[0].scrollIntoView(true);", password_time_field)
            time.sleep(1)
            password_time_field = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='MagicLogin-Password']")))

            password_time_field.click()
            password_time_field.send_keys(password)
        except ElementNotInteractableException:
            print("Element is not interactable")
        except TimeoutException:
            print("Timeout while waiting for the password field")
