import time

from selenium import webdriver
from pages.home_page import HomePage
from pages.offers_page import OffersPage
import unittest


class FindOfferTest(unittest.TestCase):
    def test_find_offer(self):
        driver = webdriver.Chrome()
        driver.get("https://www.kiwi.com/pl/city/flights-from-warsaw-poland/?dealsProvider=cheapest")
        driver.maximize_window()
        home_page = HomePage(driver)
        home_page.accept_cookies_policy()
        offers_page = OffersPage(driver)
        offers_page.clean_placepicker_input()
        offers_page.korea_click()
        offers_page.floating_popup_close()
        offers_page.choose_date()
        offers_page.click_firs_month_button()
        offers_page.choose_duration()
        offers_page.save_button_click()
        offers_page.are_there_offers()
