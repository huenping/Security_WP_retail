from selenium import webdriver
from models.driver import WDriver
from page_obj.LoginPage import login
import unittest


class MyunitTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):  # 一个测试类(文件)执行一次打开浏览器, 节约每个用例打开一次浏览器的时间
        cls.driver = WDriver().chromeDriver()
        cls.driver.maximize_window()

    def setUp(self):
        self.login = login(self.driver)
        self.login.open()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()