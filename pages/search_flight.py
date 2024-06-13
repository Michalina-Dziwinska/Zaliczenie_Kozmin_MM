import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class SearchFlight:
    def __init__(self, driver):
        self.driver = driver

    #def click_on_find_button(self):
        #self.driver.find_element(By.CSS_SELECTOR, '[data-test="LandingSearchButton"]').click()



    def choose_your_destiny_from(self):
        insert_city_value = self.driver.find_element(By.XPATH, "//input[@data-test='SearchField-input']")
        insert_city_value.send_keys('Modlin')
        insert_city_value.send_keys(Keys.RETURN)
        time.sleep(4)

        Modlin = self.driver.find_element(By.CSS_SELECTOR, "div[data-test='PlacePickerRow-wrapper'] > div:not(:last-child) > div")
        actions = ActionChains(self.driver)
        actions.move_to_element(Modlin)
        actions.click(Modlin)
        actions.perform()

    def choose_your_destiny_to(self):
        insert_city_value_to = self.driver.find_element(By.CSS_SELECTOR, 'div[data-test="PlacePickerInput-destination"] input[data-test="SearchField-input"]')
        insert_city_value_to.send_keys('Mediolan')
        insert_city_value_to.send_keys(Keys.RETURN)
        time.sleep(4)

        Mediolan = self.driver.find_element(By.CSS_SELECTOR, 'div.flex-1.overflow-hidden.text-ellipsis.whitespace-nowrap.font-medium.leading-normal' )
        actions = ActionChains(self.driver)
        actions.move_to_element(Mediolan)
        actions.click(Mediolan)
        actions.perform()

    def insert_dates(self):




"""


        self.driver.find_element(By.CSS_SELECTOR, 'input[data-test="SearchFieldDateInput"]').click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div[role='button'][data-type='DayContainer'][data-value='2024-08-18'][data-test='CalendarDay']").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "div[role='button'][data-type='DayContainer'][data-value='2024-09-17'][data-test='CalendarDay']").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '[data-test = "SearchFormDoneButton"]')

"""



