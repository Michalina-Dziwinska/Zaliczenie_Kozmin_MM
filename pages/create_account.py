from selenium.webdriver.common.by import By


class CreateAccount:
    def __init__(self, driver):
        self.driver = driver

    def create_account_click(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Utwórz konto')]")