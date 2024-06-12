from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies_policy(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="CookiesPopup-Accept"]').click()

    def hamburger_open(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-test="TopNav-SideNav-Open"]').click()

    def offers_page_click(self):
        self.driver.find_element(By.CSS_SELECTOR, "div.orbit-button-primitive-content").click()
