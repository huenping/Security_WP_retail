from time import sleep
import unittest, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from retail.test_case.models import myunit_whb, function_whb
from retail.test_case.page_obj.loginoutPage import LoginOut


class LoginOutTest(myunit_whb.MyTest):
    """网盘用户注销测试"""
    def login_out(self):
        # 注销
        LoginOut(self.driver).user_login()

    def test_cancel1(self):
        """用户注销"""
        # 验证
        self.login_out()
        sleep(5)
        po = LoginOut(self.driver)
        self.assertEqual(po.loginout_success(), "文件管理系统内网", "注销失败")
        function_whb.insert_img(self.driver, "cancel_success.png")


if __name__ == "__main__":
    unittest.main()
    sleep(5)

