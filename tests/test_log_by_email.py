from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.login_to_app import FirstLogin
import time
import unittest

class LoginNotSuccessful(unittest.TestCase):
    def test_login_not_successful(self):
        driver = webdriver.Chrome()
        driver.get("https://www.kiwi.com/pl/")
        driver.maximize_window()
        home_page = HomePage(driver)
        home_page.accept_cookies_policy()
        home_page.hamburger_open()
        manager = WebDriverWait(driver, 40).until(
            EC.element_to_be_clickable((By.XPATH, "//aside//button[./*[text()='Zaloguj się']]")))
        manager.click()
        login_to_app = FirstLogin(driver)
        login_to_app.first_login_via_email()
        login_to_app.insert_email()
        login_to_app.click_on_continue_button()
        login_to_app.insert_password()
        time.sleep(2)

        driver.quit()


