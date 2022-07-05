from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.safari import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
from selenium import webdriver
@pytest.fixture()
def driver():
    firefox_driver_binary = "./geckodriver"
    chrome_driver_binary = "./chromedriver"
    ser_firefox = FirefoxService(firefox_driver_binary)
    firefox_options = FireFoxOptions()
    chrome_options = ChromeOptions()
    browser_name = "safari"

    if browser_name == "firefox":
        dc = {
            "browserName": "firefox",
            "platformName": "MAC"
        }
        driver = webdriver.Remote("http://localhost:4444" ,desired_capabilities=dc)

    elif browser_name == "safari":

        dc = {
            "browserName" : "safari",
            "platformName" : "MAC"
        }
        driver = webdriver.Remote("http://localhost:4444",desired_capabilities=dc)



    yield driver
    driver.close()

def test_title(driver) :
    driver.get("https://www.google.com/")
    title = driver.title
    driver.save_screenshot("testgooletitle.png")

    assert title == "Google"