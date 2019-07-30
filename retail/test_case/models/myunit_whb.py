from retail.test_case.models.driver_whb import browser
import unittest


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()