from selenium.webdriver.common.by import By


class FirstLogin:
    def __init__(self, driver):
        self.driver = driver

    def first_login_via_email(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="MagicLogin-LoginViaEmail"]').click()

    def insert_email(self):
        email = 'martastachyra94@gmail.com'
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="MagicLogin-Email"]').send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="MagicLogin-Continue"]').click()

    def insert_password(self):
        password = 'kIWI2024@!'
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="MagicLogin-PasswordInput"]').send_keys(password)
