from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.create_account import CreateAccount


def test_registration():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    home_page = HomePage(driver)
    home_page.accept_cookies_policy()
    home_page.hamburger_open()
    create_account_form = (WebDriverWait(driver, 10).until
                           (EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Utwórz konto')]"))))
    create_account = CreateAccount(driver)
    create_account.create_account_click()
    create_account.enter_email_random()
    create_account.enter_password_random()
    create_account.create_account_button_click()
    confirmation_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,
             "//div[contains(@class, 'mt-md') and contains(@class, 'de:[&_.orbit-modal-heading]:p-0')]//h2[contains(text(), 'Potwierdź adres e-mail')]")))
    assert 'Potwierdź adres e-mail' in confirmation_message.text



