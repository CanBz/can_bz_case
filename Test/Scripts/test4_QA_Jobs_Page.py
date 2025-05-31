import sys
sys.path.append(sys.path[0] + "/...")
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Locators import *
from Src.PageObject.Elements import *
import unittest

class Insider_QaJobsPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        WebDriverSetup.init_driver()
        cls.driver = WebDriverSetup.driver
        cls.elements = Elements(cls.driver)


    def test_01_checkDepartment_jobs(self):
        self.elements.wait_for_element(QaPageLocators.JOBS_LIST_PRESENCE)
        CheckDepartmentjobs = self.elements.checkDepartmentJobs()
        for e in range(len(CheckDepartmentjobs)):
            self.assertEqual(CheckDepartmentjobs[e].get_attribute("innerText"),"Quality Assurance", "Not Checked Department jobs")
        print("Checked Department jobs")

    def test_02_checkPosition_jobs(self):
        CheckPositionjobs = self.elements.checkPositionJobs()
        for a in range(len(CheckPositionjobs)):
            self.assertRegex(CheckPositionjobs[a].get_attribute("innerText"),"(Senior )?Software Quality Assurance Engineer", "Not Checked Position jobs")
        print("Checked Position jobs")

    def test_03_checklocation_jobs(self):
        Checklocationjobs = self.elements.checkLocationJobs()
        for b in range(len(Checklocationjobs)):
            self.assertEqual(Checklocationjobs[b].get_attribute("innerText"), "Istanbul, Turkiye", "Not Checked location jobs")
        print("Checked location jobs")

    @classmethod
    def tearDownClass(cls):
        pass  # Let runner handle quitting the driver