import unittest, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from retail.test_case.models import myunit_whb, function_whb
from retail.test_case.page_obj.avatarPage import ReplaceAvatar


class ChangeAvatar(myunit_whb.MyTest):
    """更换头像测试"""
    def user_login1(self):
        return ReplaceAvatar(self.driver).user_login1()

    def user_login2(self):
        return ReplaceAvatar(self.driver).user_login2()


    def test1_uploadlocal(self):
        """选择网盘本地头像"""
        url1, url2 = self.user_login1()
        self.assertNotEqual(url1, url2, ["上传网盘头像失败"])
        function_whb.insert_img(self.driver, "upload_local_success.png")

    def test2_uploadavatar(self):
        """上传头像"""
        url1, url2 = self.user_login2()
        self.assertNotEqual(url1, url2, ["上传电脑头像失败"])
        function_whb.insert_img(self.driver, "upload_acatar_success.png")


if __name__ == "__main__":
    unittest.main()





