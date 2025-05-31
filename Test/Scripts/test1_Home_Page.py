import sys
sys.path.append(sys.path[0] + "/...")
from Src.PageObject.Elements import *
from Src.TestBase.WebDriverSetup import WebDriverSetup
import unittest
 
class Insider_HomePage(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        WebDriverSetup.init_driver()
        cls.driver = WebDriverSetup.driver

    def test_01_Home_Page(self):
        driver = self.driver

        web_page_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
 
        try:
            if driver.title == web_page_title:
                self.assertEqual(driver.title,web_page_title, "WebPage is not loaded successfully")
                print("WebPage loaded successfully")
        except Exception as error:
            print(error+"WebPage Failed to load")
            
    @classmethod
    def tearDownClass(cls):
        pass  # Let runner handle quitting the driver

 