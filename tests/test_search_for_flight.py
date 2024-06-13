from selenium import webdriver
from pages.search_flight import SearchFlight
from pages.home_page import HomePage

import time



def test_insert_from_value():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    driver.maximize_window()
    home_page = HomePage(driver)
    home_page.accept_cookies_policy()
    search_flight = SearchFlight(driver)
    search_flight.choose_your_destiny_from()
    search_flight.choose_your_destiny_to()
    time.sleep(3)

    # search_flight.insert_dates()


















