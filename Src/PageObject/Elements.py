
import sys
sys.path.append(sys.path[0] + "/....")
from Src.PageObject.Locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Elements:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element))

    def companyMenu(self):
        return self.driver.find_element(*HomePageLocators.COMPANY_MENU)
 
    def careersButton(self):
        return self.driver.find_element(*HomePageLocators.CAREERS_BUTTON)
    
    def checkInsiderSection(self):
        return self.driver.find_element(*CareersPageLocators.LIFE_AT_INSIDER_SECTION)
    
    def checkOurLocations(self):
        return self.driver.find_element(*CareersPageLocators.OUR_LOCATIONS_SECTION)
    
    def checkSeeAllTeams(self):
        return self.driver.find_element(*QaPageLocators.SEE_All_TEAM_BUTTON)
    
    def clickScript(self,element):
        return self.driver.execute_script(QaPageLocators.JS_CLICK, element)
    
    def checkQA(self):
        return self.driver.find_element(*QaPageLocators.QA_BUTTON)
    
    def checkAllQaJobs(self):
        return self.driver.find_element(*QaPageLocators.ALL_QA_JOBS_BUTTON)
    
    def selectLocation(self):
        return self.driver.find_element(*QaPageLocators.SELECT_LOCATION)
    
    def selectDepartment(self):
        return self.driver.find_element(*QaPageLocators.SELECT_DEPARTMENT)
    
    def checkJobsList(self):
        return self.driver.find_element(*QaPageLocators.JOBS_LIST_PRESENCE)
    
    def checkDepartmentJobs(self):
        return self.driver.find_elements(*QaPageLocators.DEPARTMENT_JOBS)

    def checkLocationJobs(self):
        return self.driver.find_elements(*QaPageLocators.LOCATION_JOBS)

    def checkPositionJobs(self):
        return self.driver.find_elements(*QaPageLocators.POSITION_JOBS)
    
    def checkViewRole(self):
        return self.driver.find_elements(*QaPageLocators.VIEW_ROLE)
    
    def clickViewRole(self):
        return self.driver.find_element(*QaPageLocators.CLICK_VIEW_ROLE)