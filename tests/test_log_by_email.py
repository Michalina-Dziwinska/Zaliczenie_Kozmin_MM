from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.create_account import CreateAccount
from pages.login_to_app import FirstLogin


def test_login_via_email():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    home_page = HomePage(driver)
    home_page.accept_cookies_policy()
    home_page.hamburger_open()
    manager = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, "//aside//button[./*[text()='Zaloguj się']]")))
    manager.click()
    login_to_app = FirstLogin(driver)
    login_to_app.first_login_via_email()
    login_to_app.insert_email()
    login_to_app.insert


def test_click_on_alternative_login_method():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    driver.find_element(By.CSS_SELECTOR, '[data-test="CookiesPopup-Accept"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="TopNav-SideNav-Open"]').click()
    manager = WebDriverWait(driver, 40).until(
        EC.element_to_be_clickable((By.XPATH, "//aside//button[./*[text()='Zaloguj się']]")))
    manager.click()
    alternative_button = driver.find_element(By.XPATH, "//a[@data-test='MagicLogin-IncorrectEmail']")
    alternative_button.click()
    assert "Użytkownik przeszedł do alternatywnej metody logowania"
