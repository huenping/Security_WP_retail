import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from retail.test_case.models import myunit_whb, function_whb
from retail.test_case.page_obj.uploadPage import UploadFolder


class UploadTest(myunit_whb.MyTest):
    """上传文件测试"""

    def user_login1(self):
        # 调用登录入口,单个文件
        return UploadFolder(self.driver).user_login()

    def user_login2(self):
        # 调用登录入口,多个文件
        return UploadFolder(self.driver).user_login1()

    def user_login3(self):
        UploadFolder(self.driver).user_login2()

    def test_01upload(self):
        """上传单个文件"""
        file_names = self.user_login1()
        self.assertIn("123321", file_names, ["上传失败"])
        function_whb.insert_img(self.driver, "upload_folder_success.png")

    def test_02more_upload(self):
        """上传多个文件"""
        all_file_name = self.user_login2()
        name_list = ['test1', 'test2','test3','test4', 'test5', '2323']
        if name_list[0] in all_file_name and name_list[1] in all_file_name and name_list[2] in all_file_name and name_list[3] in all_file_name and name_list[4] in all_file_name and name_list[5] in all_file_name:
            self.assertEqual(1, 1, ["上传成功"])
            function_whb.insert_img(self.driver, "upload_more_folder_success.png")
        else:
            self.assertEqual(1, 2, ["上传失败"])

    # def test_upload_folder(self):
    #     """上传文件夹"""
    #     self.user_login3()
    #     po = UploadFolder(self.driver)
    #     self.assertIn("test_upload", po.check_folder(), ["上传失败"])



if __name__ == "__main__":
    unittest.main()


