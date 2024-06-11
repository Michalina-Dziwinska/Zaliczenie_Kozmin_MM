from selenium.webdriver.common.by import By
from faker import Faker


class CreateAccount:
    def __init__(self, driver):
        self.driver = driver

    def create_account_click(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Utwórz konto')]").click()

    def email_input(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']")

    def password_input(self):
        self.driver.find_element(By.XPATH, "//input[@data-test='MagicLogin-Password']")

    def enter_email_random(self):
        email_input = self.driver.find_element(By.XPATH, "//input[@name='email']")
        fake = Faker()
        random_email = fake.email()
        email_input.send_keys(random_email)

    def enter_password_random(self):
        password_input = self.driver.find_element(By.XPATH, "//input[@data-test='MagicLogin-Password']")
        fake = Faker()
        random_password = fake.password()
        password_input.send_keys(random_password)

    def create_account_button_click(self):
        self.driver.find_element(By.XPATH, "//button[@data-test='MagicLogin-Submit']").click()
