from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

def test_is_kiwi_successfully_loaded_1():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    assert "Kiwi.com | Znajdź tanie loty i odkryj nowe miejsca" in driver.title

def test_is_kiwi_successfully_loaded_2():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    assert "Kiwi.com | Znajdź tanie loty i odkryj nowe miejsca" in driver.title

def test_is_kiwi_successfully_loaded_3():
    driver = webdriver.Chrome()
    driver.get("https://www.kiwi.com/pl/")
    assert "Kiwi.com | Znajdź tanie loty i odkryj nowe miejsca" in driver.title
