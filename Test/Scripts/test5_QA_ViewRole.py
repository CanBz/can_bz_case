import sys
sys.path.append(sys.path[0] + "/...")
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Locators import *
from Src.PageObject.Elements import *
import unittest

class Insider_QaViewRole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        WebDriverSetup.init_driver()
        cls.driver = WebDriverSetup.driver
        cls.elements = Elements(cls.driver)


    def test_01_view_role(self):
        self.elements.wait_for_element(QaPageLocators.VIEW_ROLE)
        CheckApplyNowButton = self.elements.checkViewRole()
        for d in range(len(CheckApplyNowButton)):
            self.assertEqual(CheckApplyNowButton[d].get_attribute("innerText"), "View Role", "Not Checked ApplyNow Button")
        print("Checked ApplyNow Button")

    def test_02_click_view_role(self):
        self.elements.wait_for_element(QaPageLocators.CLICK_VIEW_ROLE)
        clickapplynow = self.elements.clickViewRole()
        self.assertTrue(clickapplynow.is_enabled(), "Not Clickable to Apply Now")
        print("Clickable to Apply Now")
        self.elements.clickScript(clickapplynow)

    def test_03_check_redirected_page(self):
        clickapplynow = self.elements.clickViewRole()
        gethref = clickapplynow.get_attribute("href")
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        currenturl = self.driver.current_url
        self.assertEqual(gethref, currenturl, "Redirect from Page was fail")
        print("Redirect from Page was checked")
        get_titleredirected = self.driver.title
        self.assertNotEqual(get_titleredirected, None, "New Web page could not open")
        print("New Web page is opened")

    @classmethod
    def tearDownClass(cls):
        pass  # Let runner handle quitting the driver
        

