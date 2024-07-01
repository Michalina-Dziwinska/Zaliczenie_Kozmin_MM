from pages.alternative_method_window import AlternativeMethodWindow
from test_data.alternative_login_method import AlternativeLoginMethodData
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from ddt import data, unpack, ddt
import test_data.alternative_login_method
import time
import unittest

@ddt
class AlternativeMethodLoginTest(unittest.TestCase):
    """
    Alternative Method Login Test
    """

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)
        self.alternative_method_window = None


    def setUp(self):
        super().setUp()
        self.driver = webdriver.Chrome()
        self.test_data = AlternativeLoginMethodData()

    def test_no_date_entered(self):
        """
        TC1_1: User does not enter departure date
        """
    # Steps:
    # 1. Accept the cookies
        driver = webdriver.Chrome()
        driver.get("https://www.kiwi.com/pl/")
        driver.maximize_window()
        home_page = HomePage(driver)
        home_page.accept_cookies_policy()
    # 2. Click on Login button
        alternative_method_window = AlternativeMethodWindow(driver)
        alternative_method_window.click_on_Login_button()
    # 3. Click on "Rezerwacja na niepoprawny adres e-mail?"
        alternative_method_window.click_on_alternative_login_button()
    # 4. Insert reservation number
        alternative_method_window.insert_reservation_number(self.test_data.alternative_reservation_number)
    # 5. Insert fake e-mail adress
        alternative_method_window.insert_fake_email(self.test_data.alternative_email)
    # 6. Enter IATA code
        alternative_method_window.insert_iata_code(self.test_data.alternative_iata_code)
    # 7. Click on "Send" button
        #alternative_method_window.cick_on_send_button()

    # Verify if IATA code has 3 digits
        iata_code_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "MagicLogin-IATA"))
        )
        # Take value
        iata_code_value = iata_code_element.get_attribute("value")

        # Check if it has 3 digits
        self.assertEqual(len(iata_code_value), 3,
                f"Expected IATA code to have 3 characters, but got '{iata_code_value}' with length {len(iata_code_value)}")
        print("Test passed: The field has 3 digits")





    @data(*test_data.alternative_login_method.get_csv_data("../test_data/zaliczenie.csv"))
    @unpack
    def test_no_departure_date_ddt(self, ReservationNumber, Email, DepartureDateDay, CodeIata):
            driver = webdriver.Chrome()
            try:
                driver.get("https://www.kiwi.com/pl/")
                driver.maximize_window()
                home_page = HomePage(driver)
                home_page.accept_cookies_policy()

                alternative_method_window = AlternativeMethodWindow(driver)
                alternative_method_window.click_on_Login_button()
                alternative_method_window.click_on_alternative_login_button()
                alternative_method_window.insert_reservation_number(ReservationNumber)
                alternative_method_window.insert_fake_email(Email)
                alternative_method_window.insert_iata_code(CodeIata)

                # Czy wartosc pola iata to "JFK"

                iata_code_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, "MagicLogin-IATA"))
                )
                iata_code_value = iata_code_element.get_attribute("value")
                self.assertEqual(iata_code_value, "JFK", f"Expected IATA code to be 'JFK', but got '{iata_code_value}'")
            except Exception as e:
                print(f"Exception occurred: {str(e)}")


            finally:
                driver.quit()







