from selenium import webdriver
from pages.search_flight import SearchFlight
from pages.home_page import HomePage
import time
import unittest


class InsertFromValueTest(unittest.TestCase):
    def test_insert_from_value(self):
        driver = webdriver.Chrome()
        driver.get("https://www.kiwi.com/pl/")
        driver.maximize_window()
        home_page = HomePage(driver)
        home_page.accept_cookies_policy()
        search_flight = SearchFlight(driver)
        search_flight.choose_your_destiny_from()
        search_flight.choose_your_destiny_to()
        time.sleep(2)
        search_flight.click_on_search_button()
        search_flight.search_page_results()



















