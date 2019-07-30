import os
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from retail.test_case.models import myunit_whb, function_whb
from retail.test_case.page_obj.downloadPage import DownFolder


class DownTest(myunit_whb.MyTest):
    """下载文件"""

    def user_login1(self):
        # 登录
        return DownFolder(self.driver).user_login1()

    def user_login2(self):
        return DownFolder(self.driver).user_login2()

    def test_downfile1(self):
        """下载文件"""
        file_name, files_list = self.user_login1()
        self.assertIn(file_name, files_list, ["下载失败"])
        function_whb.insert_img(self.driver, "download_file_success.png")

    def test_downfolder2(self):
        """下载文件和文件夹"""
        folder_name, file_name, file_list = self.user_login2()
        if folder_name and file_name in file_list:
            self.assertEqual(1, 1, ["下载失败"])
            function_whb.insert_img(self.driver, "download_folder_success.png")
        else:
            self.assertEqual(1, 2, ["下载失败"])


if __name__ == "__main__":
    unittest.main()