from _pydatetime import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage


def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    home_page = HomePage(driver)
    home_page.accept_cookies_policy()
    driver.find_element(By.CSS_SELECTOR, '[data-test="TopNav-SideNav-Open"]').click()
    driver.find_element(By.XPATH, "//a[contains(text(), 'Utwórz konto')]")


def test_is_kiwi_successfully_loaded_2():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    assert "Kiwi.com | Znajdź tanie loty i odkryj nowe miejsca" in driver.title


def test_click_on_login_button():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    driver.find_element(By.CSS_SELECTOR, '[data-test="CookiesPopup-Accept"]').click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="TopNav-SideNav-Open"]').click()
    manager = WebDriverWait(driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//aside//button[./*[text()='Zaloguj się']]")))
    manager.click()
    assert "Użytkownik przeszedł do formularza logowania"


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
