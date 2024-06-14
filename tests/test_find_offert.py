import time

from selenium import webdriver
from pages.home_page import HomePage
from pages.offers_page import OffersPage


def test_find_offer():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/city/flights-from-warsaw-poland/?dealsProvider=cheapest")
    driver.maximize_window()
    home_page = HomePage(driver)
    home_page.accept_cookies_policy()
    offers_page = OffersPage(driver)
    offers_page.clean_placepicker_input2()
    offers_page.search_country()
    offers_page.empty_place_click()
    time.sleep(5)