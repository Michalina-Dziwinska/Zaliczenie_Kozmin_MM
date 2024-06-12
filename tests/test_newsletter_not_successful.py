from pages.home_page import HomePage
from selenium import webdriver

from pages.newsletter_page import Newsletter


def test_failed_assign_to_Newsletter():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    driver.maximize_window()
    home_page = HomePage(driver)
    home_page.accept_cookies_policy()
    home_page.hamburger_open()
    newsletter_page = Newsletter(driver)
    newsletter_page.click_on_order_newsletter()
    #newsletter_page.insert_airport_name()
    #newsletter_page.insert_incorrect_email()










