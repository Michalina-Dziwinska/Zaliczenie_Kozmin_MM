import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchFlight:
    def __init__(self, driver):
        self.driver = driver

    def choose_your_destiny_from(self):
        insert_city_value = self.driver.find_element(By.XPATH, "//input[@data-test='SearchField-input']")
        insert_city_value.send_keys('Modlin')
        insert_city_value.send_keys(Keys.RETURN)
        time.sleep(2)

        Modlin = self.driver.find_element(By.CSS_SELECTOR, "div[data-test='PlacePickerRow-wrapper'] > div:not(:last-child) > div")
        actions = ActionChains(self.driver)
        actions.move_to_element(Modlin)
        actions.click(Modlin)
        actions.perform()

    def choose_your_destiny_to(self):
        insert_city_value_to = self.driver.find_element(By.CSS_SELECTOR, 'div[data-test="PlacePickerInput-destination"] input[data-test="SearchField-input"]')
        insert_city_value_to.send_keys('Mediolan')
        insert_city_value_to.send_keys(Keys.RETURN)
        time.sleep(2)

        Mediolan = self.driver.find_element(By.CSS_SELECTOR, 'div.flex-1.overflow-hidden.text-ellipsis.whitespace-nowrap.font-medium.leading-normal' )
        actions = ActionChains(self.driver)
        actions.move_to_element(Mediolan)
        actions.click(Mediolan)
        actions.perform()

    def click_on_search_button(self):

        self.driver.find_element(By.CSS_SELECTOR, '[data-test="LandingSearchButton"]').click()
        time.sleep(6)

    def search_page_results(self):

    # Zmiana strony
        self.driver.get("https://www.kiwi.com/pl/search/results/port-lotniczy-warszawa-modlin-warszawa-polska/mediolan-wlochy")

    # Sprawdzenie tytułu strony
        assert "Podróże na trasie Warszawa WMI‎ – Mediolan‎" in self.driver.title
        print("Test passed: Tak, tytuł strony się zgadza!")

    # Czy element "Opinia" pojawia sie na stronie
        opinie = self.driver.find_element(By.CSS_SELECTOR, '[data-test="feedbackButton"]')
        assert opinie.is_displayed()
        print("Test passed: Tak, element 'Opinie' wyświetla się na stronie wyszukiwania")

    # Sprawdź url strony
        assert "search" in self.driver.current_url
        print("Test passed: Tak adres URL jest poprawny")


        print("Test passed: Wyszukiwanie najnowszych lotów zakońćzone sukcesem")






