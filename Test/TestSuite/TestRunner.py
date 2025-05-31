import sys
import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from unittest import TestLoader,TextTestRunner,TestSuite
from Test.Scripts.test1_Home_Page import Insider_HomePage
from Test.Scripts.test2_Careers_Page import Insider_CareersPage
from Test.Scripts.test3_QA_Page import Insider_QaPage
from Test.Scripts.test4_QA_Jobs_Page import Insider_QaJobsPage
from Test.Scripts.test5_QA_ViewRole import Insider_QaViewRole
from Src.TestBase.WebDriverSetup import WebDriverSetup

def run_all_tests():
    WebDriverSetup.init_driver()

    loader = TestLoader()
    suite = TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(Insider_HomePage))
    suite.addTests(loader.loadTestsFromTestCase(Insider_CareersPage))
    suite.addTests(loader.loadTestsFromTestCase(Insider_QaPage))
    suite.addTests(loader.loadTestsFromTestCase(Insider_QaJobsPage))
    suite.addTests(loader.loadTestsFromTestCase(Insider_QaViewRole))

    runner = TextTestRunner(verbosity=2)
    result = runner.run(suite)

    WebDriverSetup.quit_driver()

if __name__ == "__main__":
    run_all_tests()