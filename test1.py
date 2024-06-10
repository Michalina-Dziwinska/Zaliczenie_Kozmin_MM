from _pydatetime import time

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
chromedriver_autoinstaller.install()

def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    driver.find_element(By.CSS_SELECTOR, '[data-test="CookiesPopup-Accept"]').click()
    print("cookisy ok")
    #cookie_button.click()
    driver.find_element(By.CSS_SELECTOR, '[data-test="TopNav-SideNav-Open"]').click()
    print("hamburger kliknięty")

    #assert "Kiwi.com | Znajdź tanie loty i odkryj nowe miejsca" in driver.title

def test_is_kiwi_successfully_loaded_2():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    assert "Kiwi.com | Znajdź tanie loty i odkryj nowe miejsca" in driver.title

def test_click_top_nav_UWAGAnieDzialaTo():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    hamburger_button = driver.find_element(By.CSS_SELECTOR, '[data-test="TopNav-SideNav-Open"]')
    hamburger_button.click()
    assert "Udało się"

def test_click_on_login_button():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    login_button = driver.find_element(By.XPATH, '//*[@id="react-view"]/div[2]/div[2]/div/aside/div[2]/div[1]/button')
    login_button.click()
    assert "Użytkownik przeszedł do formularza logowania"

def test_click_on_alternative_login_method():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    alternative_button = driver.find_element(By.XPATH, '')
    alternative_button.click()
    assert "Użytkownik przeszedł do alternatywnej metody logowania"








