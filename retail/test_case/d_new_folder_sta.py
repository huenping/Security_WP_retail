from time import sleep
import unittest, random, sys

sys.path.append("./models")
sys.path.append("./page_obj")
from retail.test_case.models import myunit_whb, function_whb
from retail.test_case.page_obj.newfolderPage import NewFolder


class FolderTest(myunit_whb.MyTest):
    """网盘新建文件夹测试"""

    def create1(self):
        # 登录
        return NewFolder(self.driver).user_login1()

    def more_create(self):
        # 调用登录功能
        return NewFolder(self.driver).user_login2()

    def user_login(self):
        # 新建重名文件夹
        return NewFolder(self.driver).user_login3()

    def test1_folder(self):
        """新建单个文件夹"""
        file_name = NewFolder(self.driver).file_name
        file_names = self.create1()
        self.assertIn(file_name, file_names, ["创建失败"])
        function_whb.insert_img(self.driver, "new_folder_success.png")

    def test2_folder(self):
        """多级文件夹"""
        # 接收最后创建的文件夹名， 检查是否有这个文件夹
        file_name, all_file = self.more_create()
        self.assertIn(file_name, all_file, ["创建失败"])
        function_whb.insert_img(self.driver, "more_folder_success.png")

    def test3_folder(self):
        """重名文件夹"""
        agent_name, tips = self.user_login()
        self.assertIn(agent_name, tips, ["创建同名文件夹失败"])
        function_whb.insert_img(self.driver, "again_folder_success.png")


if __name__ == '__main__':
    unittest.main()
