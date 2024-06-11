from selenium.webdriver.common.by import By
from faker import Faker


class CreateAccount:
    def __init__(self, driver):
        self.driver = driver

    def create_account_click(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Utwórz konto')]").click()

    def email_input_click(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").click()

    def password_input_click(self):
        self.driver.find_element(By.XPATH, "//input[@data-test='MagicLogin-Password']").click()

    def enter_email_random(self):
        email_input = self.driver.find_element(By.XPATH, "//input[@name='email']")
        email_input.send_keys(random_email)

         fake = Faker()
         random_email = fake.email()