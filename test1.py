from selenium import webdriver
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://www.kiwi.com/pl/")
assert "Python" in driver.title