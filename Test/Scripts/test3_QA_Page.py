import sys
sys.path.append(sys.path[0] + "/...")
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Locators import *
from Src.PageObject.Elements import *
import unittest
 
class Insider_QaPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        WebDriverSetup.init_driver()
        cls.driver = WebDriverSetup.driver
        cls.elements = Elements(cls.driver)
        
    def test_01_goQaPage(self):
        new_qa_url = "https://useinsider.com/careers/quality-assurance/"
        self.driver.get(new_qa_url)
        currenturl = self.driver.current_url
        self.assertEqual(new_qa_url, currenturl, "Not Redirected to QA Page")
        print("Redirected to QA Page")

    def test_02_clickallqajobs(self):
        clickallqajobs = self.elements.checkAllQaJobs()
        self.assertTrue(clickallqajobs.is_enabled(), " Not Clickable to Select all QA jobs")
        print("Clickable to Select all QA jobs")
        self.elements.clickScript(clickallqajobs)

    def test_03_selectlocation(self):
        selectlocation = self.elements.selectLocation()
        self.assertTrue(selectlocation.is_displayed(), "Not Selected Istanbul, Turkey")
        print("Selected Istanbul, Turkey")
        selectlocation.click()

    def test_04_selectdepartment(self):
        selectdepartment = self.elements.selectDepartment()
        self.assertTrue(selectdepartment.is_displayed(), "Not Selected Quality Assurance")
        print("Selected Quality Assurance")
        selectdepartment.click()

    def test_05_jobslist(self):
        self.elements.wait_for_element(QaPageLocators.JOBS_LIST_PRESENCE)
        jobslist = self.elements.checkJobsList()
        self.assertTrue(jobslist.is_displayed(), "Not Presented the Job List")
        print("Presented the Job List")
    
    @classmethod
    def tearDownClass(cls):
        pass  # Let runner handle quitting the driver
