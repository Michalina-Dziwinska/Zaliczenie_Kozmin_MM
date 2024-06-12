from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Newsletter:
    def __init__(self,driver):
        self.driver = driver

    def click_on_order_newsletter(self, driver):
        newsletter_li = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH,
                                            "//li[contains(concat(' ', @class, ' '), ' orbit-text-link ') and .//a[text()='Zamów newsletter']]"))
        )

    #def insert_airport_name(self):

    #def check_the_checkbox(self):

    #def insert_incorrect_email(self):




