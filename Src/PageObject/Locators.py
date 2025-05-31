from selenium.webdriver.common.by import By

class BaseLocators(object):
    # Locators for general/common elements
    COOKIES_ACCEPT_BUTTON = (By.CSS_SELECTOR, "#wt-cli-accept-all-btn")


class HomePageLocators(object):
    # Locators for header elements like dropdowns
    COMPANY_MENU = (By.XPATH, "//a[@id='navbarDropdownMenuLink' and contains(text(), 'Company')]")
    CAREERS_BUTTON = (By.CSS_SELECTOR, "a.dropdown-sub[href='https://useinsider.com/careers/']")


class CareersPageLocators(object):
    # Locators specific to the Careers page
    LIFE_AT_INSIDER_SECTION = (By.XPATH, "//section[.//h2[contains(text(), 'Life at Insider')]]")
    OUR_LOCATIONS_SECTION = (By.XPATH, "//section[@id='career-our-location']")

class QaPageLocators(object):
    # Locators specific to the Careers page
    SEE_All_TEAM_BUTTON = (By.XPATH, "//a[@href='javascript:void(0)' and @class='btn btn-outline-secondary rounded text-medium mt-5 mx-auto py-3 loadmore']")
    JS_CLICK = "arguments[0].click()"
    QA_BUTTON = (By.CSS_SELECTOR,"#career-find-our-calling > div > div > div.col-12.d-flex.flex-wrap.p-0.career-load-more > div:nth-child(23) > div.job-title.mt-0.mt-lg-2.mt-xl-5 > a > h3")
    ALL_QA_JOBS_BUTTON = (By.CSS_SELECTOR, "#page-head > div > div > div.col-12.col-lg-7.order-2.order-lg-1 > div > div > a")
    SELECT_LOCATION = (By.CSS_SELECTOR, "#filter-by-location > option.job-location.istanbul-turkiye")
    SELECT_DEPARTMENT = (By.XPATH, "//select[@name='filter-by-department']/option[text()='Quality Assurance']")
    JOBS_LIST_PRESENCE = (By.CSS_SELECTOR, "#jobs-list")
   
   
    DEPARTMENT_JOBS = (By.XPATH, "//span[contains(@class, 'position-department') and text()='Quality Assurance']")
    POSITION_JOBS = (By.XPATH, "//p[@class='position-title font-weight-bold' and contains(text(),'Quality Assurance')]")
    LOCATION_JOBS = (By.XPATH, "//div[@class='position-location text-large' and text()='Istanbul, Turkiye']")

    VIEW_ROLE = (By.XPATH, '//*[@id="jobs-list"]/div[1]/div/a')
    CLICK_VIEW_ROLE = (By.XPATH, "//p[text()='Software Quality Assurance Engineer']/following::a[contains(text(), 'View Role')][1]")