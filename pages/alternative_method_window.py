import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class AlternativeMethodWindow():

    def __init__(self, driver):
        self.driver = driver

    def click_on_Login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test = "TopNav-SingInButton"]'). click()

    def click_on_alternative_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test = "MagicLogin-IncorrectEmail"]').click()

    def insert_reservation_number(self, reservation_number):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test = "MagicLogin-BookingId"]').send_keys(reservation_number)

    def insert_fake_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test = "MagicLogin-Email"]').send_keys(email)

    def insert_iata_code(self, code):
        self.driver.find_element(By.ID, "MagicLogin-IATA").send_keys(code)
        time.sleep(3)


    def cick_on_send_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test = "MagicLogin-GetSingleBookingSubmit"]').click()

    def get_error_message(self):
        error_message = self.driver.find_element(By.XPATH, "//div[@data-test='DateInput' and @data-state='error')]")
        actions = ActionChains(self.driver)
        actions.move_to_element(error_message).perform()
        time.sleep(5)
        return error_message.text














