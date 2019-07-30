import unittest, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from retail.test_case.models import myunit_whb, function_whb
from retail.test_case.page_obj.userPage import UserManagement


class UserTest(myunit_whb.MyTest):
    """用户管理"""

    def user_login1(self):
        # 添加部门登录入口
        return UserManagement(self.driver).user_login1()

    def user_login2(self):
        # 修改部门名称登录入口
        return UserManagement(self.driver).user_login2()

    def user_login3(self):
        # 清楚选择登录入口
        return UserManagement(self.driver).user_login3()

    def user_login4(self):
        # 添加用户登录入口
        return UserManagement(self.driver).user_login4()

    def user_login5(self):
        # 修改姓名登录入口
        return UserManagement(self.driver).user_login5()

    def user_login6(self):
        # 修改密码登录入口
        return UserManagement(self.driver).user_login6()

    def user_login7(self):
        # 修改邮箱登录入口
        return UserManagement(self.driver).user_login7()

    def user_login8(self):
        # 修改手机号登录入口
        return UserManagement(self.driver).user_login8()

    def user_login9(self):
        # 修改用户地址登录入口
        return UserManagement(self.driver).user_login9()

    def user_login10(self):
        # 修改用户存储空间登录入口
        return UserManagement(self.driver).user_login10()

    def user_login11(self):
        # 删除登录入口
        return UserManagement(self.driver).user_login11()

    def user_login12(self):
        # 导入用户登录入口
        return UserManagement(self.driver).user_login12()

    def user_login13(self):
        return UserManagement(self.driver).user_login13()

    def user_login14(self):
        # 删除部门登录入口
        return UserManagement(self.driver).user_login14()

    def test1_add_class(self):
        """添加部门"""
        class_name = UserManagement.class_name
        class_names = self.user_login1()
        self.assertIn(class_name, class_names, ["添加部门失败"])
        function_whb.insert_img(self.driver, "add_class_success.png")

    def test2_modify_class(self):
        """修改部门名称"""
        class_name = UserManagement.modify_class_name
        class_names = self.user_login2()
        self.assertIn(class_name, class_names, ["修改部门名称失败"])
        function_whb.insert_img(self.driver, "modify_classname_success.png")

    def test3_clear_selection(self):
        """清除选择"""
        class_value = self.user_login3()
        self.assertEqual("el-tree", class_value, ["清除选择失败"])
        function_whb.insert_img(self.driver, "clear_selection_success.png")

    def test4_user_add(self):
        """用户创建测试"""
        user_name = UserManagement.user_name
        # print(user_name)
        files_name = self.user_login4()
        self.assertIn(user_name, files_name, ["创建用户失败"])
        function_whb.insert_img(self.driver, "user_add_success.png")

    def test5_modify_name(self):
        """用户修改姓名"""
        user_name = UserManagement.username1
        files_name = self.user_login5()
        self.assertIn(user_name, files_name, ["修改姓名失败"])
        function_whb.insert_img(self.driver, "modify_name_success.png")

    def test6_modify_passwd(self):
        """用户修改密码"""
        info_passwd = self.user_login6()
        self.assertEqual(info_passwd, "密码修改成功")
        function_whb.insert_img(self.driver, "modify_passwd_success.png")

    def test7_modify_email(self):
        """修改用户email"""
        email_name = UserManagement.email
        emails_name = self.user_login7()
        self.assertIn(email_name, emails_name, ["修改email失败"])
        function_whb.insert_img(self.driver, "modify_email_success.png")

    def test8_modify_phone(self):
        """用户修改手机号"""
        phone_number = UserManagement.phone_number
        phone_numbers = self.user_login8()
        self.assertIn(phone_number, phone_numbers, ["修改手机号失败"])
        function_whb.insert_img(self.driver, "modify_phone_success.png")

    def test91_modify_addr(self):
        """用户修改地址"""
        user_address = UserManagement.user_address
        user_addresses = self.user_login9()
        self.assertIn(user_address, user_addresses, ["修改地址失败"])
        function_whb.insert_img(self.driver, "modify_address_success.png")

    def test92_modify_ROM(self):
        """用户修改存储空间"""
        user_ROM = UserManagement.ROM
        user_ROMs = self.user_login10()
        self.assertIn(user_ROM, user_ROMs, ["修改存储空间失败"])
        function_whb.insert_img(self.driver, "modify_ROM_success.png")

    def test93_user_del(self):
        """用户删除测试"""
        user_name = UserManagement.user_name
        files_name = self.user_login11()
        self.assertNotIn(user_name, files_name, ["删除用户失败"])
        function_whb.insert_img(self.driver, "user_del_success.png")

    def test94_user_import(self):
        """用户导入"""
        file_names, excel_names = self.user_login12()
        for i in file_names:
            if i in excel_names:
                pass
            else:
                self.assertEqual(1, 2)
        self.assertEqual(1, 1, ["用户导入失败"])
        function_whb.insert_img(self.driver, "user_import_success.png")

    def test95_user_export(self):
        """用户导出"""
        file_list = self.user_login13()
        self.assertIn("usertest部门成员.xls", file_list, ["用户导出失败"])
        function_whb.insert_img(self.driver, "user_import_success.png")

    def test96_del_class(self):
        """删除部门"""
        class_name = UserManagement.modify_class_name
        class_names = self.user_login14()
        self.assertNotIn(class_name, class_names, ["删除部门失败"])
        function_whb.insert_img(self.driver, "del_class_success.png")


if __name__ == "__main__":
    unittest.main()















