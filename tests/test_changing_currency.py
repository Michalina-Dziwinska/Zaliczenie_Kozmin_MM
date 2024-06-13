from pages.changing_currency import ChangeCurrency
from pages.home_page import HomePage
from selenium import webdriver
def test_choose_language_and_ccy():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    driver.maximize_window()
    home_page = HomePage(driver)
    home_page.accept_cookies_policy()
    changing_currency = ChangeCurrency(driver)
    changing_currency.click_on_currency()
    changing_currency.select_language()
    changing_currency.select_currency()
    changing_currency.click_assign_button()


