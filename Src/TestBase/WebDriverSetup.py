import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Src.PageObject.Elements import *
from Src.PageObject.Locators import *


class WebDriverSetup:
    driver = None

    @classmethod
    def init_driver(cls):
        if cls.driver is None:
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            prefs = {"profile.default_content_setting_values.notifications": 2}
            options.add_experimental_option("prefs", prefs)
            options.add_experimental_option("excludeSwitches", ["enable-popup-blocking"])
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            options.add_argument("--disable-notifications")
            options.add_argument("--enable-popup-blocking")
            cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            cls.driver.implicitly_wait(10)
            cls.driver.set_page_load_timeout(30)
            cls.driver.get("https://useinsider.com/")

            try:
                cls.driver.find_element(*BaseLocators.COOKIES_ACCEPT_BUTTON).click()
            except:
                print("Cookies button not found or already accepted")


    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None


"""
class WebDriverSetup(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("start-maximized")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-popup-blocking"])
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--enable-popup-blocking")

        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.set_page_load_timeout(30)
        cls.driver.get("https://useinsider.com/")
        cls.home_page = Elements(cls.driver)

        # Accept cookies once
        try:
            cls.driver.find_element(*BaseLocators.COOKIES_ACCEPT_BUTTON).click()
        except:
            print("Cookies button not found or already accepted")

    @classmethod
    def tearDownClass(cls):
        print("Closing browser after all tests")
        cls.driver.quit()
"""