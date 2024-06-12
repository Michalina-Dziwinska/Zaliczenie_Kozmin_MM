import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.offers_page import OffersPage


def test_find_offer():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/city/flights-from-warsaw-poland/?dealsProvider=cheapest")
    home_page = HomePage(driver)
    home_page.accept_cookies_policy()
    offers_page = OffersPage(driver)
    offers_page.clean_placepicker_input()
    offers_page.search_country()