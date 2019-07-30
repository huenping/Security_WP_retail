from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from retail.test_case.page_obj.base_whb import Page
from time import sleep


class login(Page):
    """用户登录"""

    login_username_loc = (By.XPATH, "//form//p/input[@id='user']")
    login_password_loc = (By.XPATH, "//form//p/input[@id='password']")
    login_button_loc = (By.ID, "submit-wrapper")

    # 登录用户名
    def login_username(self, username):
        self.find_element(*self.login_username_loc)[0].send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_element(*self.login_password_loc)[0].send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc)[0].click()

    # 定义登录入口
    def user_login(self, username, password):
        """获取用户名密码登录"""
        self.open()
        # self.YZF_login()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)


    # 用户名和密码错误提示
    def userAndpawd_error_hint(self):
        return self.find_element(By.XPATH, "//form//p[@class='warning']")[0].text

    # 用户名或密码为空时
    def userAndpawd_error_hint1(self):
        title = self.driver.title
        return title

    # 登录成功页面的title
    def user_login_success(self):
        title = self.driver.title
        return title
