from time import sleep
import unittest, random, sys

sys.path.append("./models")
sys.path.append("./page_obj")
from retail.test_case.models import myunit_whb, function_whb
from retail.test_case.page_obj.loginPage_whb import login


class LoginTest(myunit_whb.MyTest):
    """网盘登录测试"""
    # admin用户登录

    def user_login_verify(self, username="", password=""):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        """用户名、密码为空"""
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.userAndpawd_error_hint1(), "文件管理系统内网")
        function_whb.insert_img(self.driver, "user_empty.png")

    def test_login2(self):
        """用户名正确，密码为空"""
        self.user_login_verify(username="admin")
        po = login(self.driver)
        self.assertEqual(po.userAndpawd_error_hint1(), "文件管理系统内网")
        function_whb.insert_img(self.driver, "pawd_empty.png")

    def test_login3(self):
        '''用户名为空，密码正确'''
        self.user_login_verify(password="admin2003")
        po = login(self.driver)
        self.assertEqual(po.userAndpawd_error_hint1(), "文件管理系统内网")
        function_whb.insert_img(self.driver, "user_empty.png")

    def test_login4(self):
        '''用户名与密码不匹配'''
        character = random.choice('zyxwvutsrqponmlkjihgfedcba')
        username = "admin" + character
        self.user_login_verify(username=username, password="admin2003")
        po = login(self.driver)
        self.assertEqual(po.userAndpawd_error_hint(), "用户名或密码错误")
        function_whb.insert_img(self.driver, "user_pawd_error.png")

    def test_login5(self):
        '''用户名和密码正确'''
        self.user_login_verify(username="admin", password="admin2003")
        sleep(5)
        po = login(self.driver)
        self.assertEqual(po.user_login_success(), '文件 - 文件管理系统内网', "登陆失败")
        function_whb.insert_img(self.driver, "user_pawd_ture.png")


if __name__ == "__main__":
    unittest.main()