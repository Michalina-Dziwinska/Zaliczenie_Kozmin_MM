from selenium.webdriver.common.by import By


class CreateAccount:
    def __init__(self, driver):
        self.driver = driver

    def create_account_click(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Utwórz konto')]").click()

    def email_input(self):
        self.driver.find_element(By.XPATH, "//input[@name='email']").click()

    def password_input(self):
        self.driver.find_element(By.XPATH, "//input[@data-test='MagicLogin-Password']").click()
