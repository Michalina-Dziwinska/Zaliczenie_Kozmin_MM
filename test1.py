from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

def registration():
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

def click_top_nav():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    hamburger_button = element_by_attribute = driver.find_element(By.CSS_SELECTOR, '[data-test="TopNav-SideNav-Open"]')
    hamburger_button.click()
    assert "Udało się"