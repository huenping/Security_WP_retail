from time import sleep
from selenium.webdriver.common.by import By
from .base_whb import Page


class Main_Page(Page):
    """登录到主页面"""
    # 登录xpath
    login_username_loc = (By.XPATH, "//form//p/input[@id='user']")
    login_password_loc = (By.XPATH, "//form//p/input[@id='password']")
    login_button_loc = (By.ID, "submit-wrapper")

    # 登录
    def login_data(self):
        sleep(1)
        self.find_element(*self.login_username_loc)[0].send_keys("admin")
        sleep(1)
        self.find_element(*self.login_password_loc)[0].send_keys("admin2003")
        sleep(1)
        self.find_element(*self.login_button_loc)[0].click()
        sleep(2)

    def login_admin(self):
        sleep(1)
        self.find_element(*self.login_username_loc)[0].send_keys("admin")
        sleep(1)
        self.find_element(*self.login_password_loc)[0].send_keys("admin2003")
        sleep(1)
        self.find_element(*self.login_button_loc)[0].click()
        sleep(2)