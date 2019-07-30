from time import sleep
from selenium.webdriver.common.by import By
from .main_page import Main_Page
# from .base import Page


class LoginOut(Main_Page):
    """注销"""
    def user_login(self):
        # 登录
        self.open()
        self.loginout()
        sleep(1)

    def loginout(self):
        self.login_data()
        self.find_element(By.XPATH, "//div[@id='expand']/div/img")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//div[@id='expanddiv']//li[2]")[0].click()

    # 检查文本
    def loginout_success(self):
        title = self.driver.title
        # print(title)
        return title
