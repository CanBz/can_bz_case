import sys
import os
sys.path.append(sys.path[0] + "/...")
sys.path.append(os.getcwd())
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Locators import *
from Src.PageObject.Elements import *
import unittest
 
class Insider_CareersPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        WebDriverSetup.init_driver()
        cls.driver = WebDriverSetup.driver
        cls.elements = Elements(cls.driver)

    def test_01_company_menu(self):
        self.elements.wait_for_element(HomePageLocators.COMPANY_MENU)
        self.elements.companyMenu().click()
 
    def test_02_careers_button(self):
        self.elements.wait_for_element(HomePageLocators.CAREERS_BUTTON)
        careers_button = self.elements.careersButton()
        self.assertTrue(careers_button.is_enabled(), " Not Clickable to Careers Button")
        print("Clickable to Careers Button")
        careers_button.click()
    
    def test_03_careers_button(self): 
        self.elements.wait_for_element(CareersPageLocators.LIFE_AT_INSIDER_SECTION)
        lifeatinsider_block = self.elements.checkInsiderSection()
        self.assertTrue(lifeatinsider_block.is_displayed(), "lifeatinsider block does not exist")
        print("lifeatinsider block exists")
      
    def test_04_careers_button(self):
        self.elements.wait_for_element(CareersPageLocators.OUR_LOCATIONS_SECTION)
        ourlocations_block = self.elements.checkOurLocations()
        self.assertTrue(ourlocations_block.is_displayed(), "OurLocations block does not exist")
        print("OurLocations block exists")

    @classmethod
    def tearDownClass(cls):
        pass  # Let runner handle quitting the driver

