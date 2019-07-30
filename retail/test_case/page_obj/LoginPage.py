from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from page_obj.base import BasePage
from time import sleep
from selenium import webdriver
import sys


class login(BasePage):

    """用户登录界面"""

    # action

    login_username_loc = (By.XPATH, "//*[@id='user']")
    login_password_loc = (By.XPATH, "//*[@id='password']")
    login_button_loc = (By.XPATH, "//*[@id='submit']")
    quitBtn_loc = (By.XPATH, "//*[@id='expand']")
    QuitBtn_loc = (By.XPATH, "//*[@id='expanddiv']/ul/li[2]/a")

    # 登录按钮

    def clickLoginBtn(self):
        element = self.findElement(*self.login_button_loc)
        element.click()

    # 定义统一登录入口
    def loginFunc(self, username='admin', password='admin2003'):
        self.inputValue(self.login_username_loc, username)
        self.inputValue(self.login_password_loc, password)
        self.clickLoginBtn()

    def clearValue(self, element):
        empty = self.findElement(*element)
        empty.clear()

    def quit(self):
        self.findElement(*self.quitBtn_loc).click()
        sleep(2)
        self.findElement(*self.QuitBtn_loc).click()


if __name__ == '__main__':
    pass

