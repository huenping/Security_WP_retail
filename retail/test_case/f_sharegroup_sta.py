import unittest, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from retail.test_case.models import myunit_whb, function_whb
from retail.test_case.page_obj.sharedgroupPage import ShareGroup


class GroupUser(myunit_whb.MyTest):
    """共享组用户管理"""

    def user_login1(self):
        # 创建组登录入口
        return ShareGroup(self.driver).user_login1()

    def user_login2(self):
        # 删除组登录入口
        return ShareGroup(self.driver).user_login2()

    def user_login3(self):
        # 添加用户登录入口
        return ShareGroup(self.driver).user_login3()

    def user_login4(self):
        # 删除用户登录入口
        return ShareGroup(self.driver).user_login4()

    def test1_add_group(self):
        """添加组"""
        user_name = ShareGroup.group_name
        all_names = self.user_login1()
        self.assertIn(user_name, all_names, ["添加组失败"])
        function_whb.insert_img(self.driver, "add_group_success.png")

    def test4_del_group(self):
        """删除组"""
        user_name = ShareGroup.group_name
        all_names = self.user_login2()
        self.assertNotIn(user_name, all_names, ["删除组失败"])
        function_whb.insert_img(self.driver, "del_group_success.png")

    def test2_adduser(self):
        """添加组成员用户"""
        user_name, all_names = self.user_login3()
        self.assertIn(user_name, all_names, ["添加用户失败"])
        function_whb.insert_img(self.driver, "add_user_success.png")

    def test3_deluser(self):
        """删除组成员用户"""
        user_name, all_names = self.user_login4()
        self.assertNotIn(user_name, all_names, ["删除用户失败"])
        function_whb.insert_img(self.driver, "del_user_success.png")


if __name__ == "__main__":
    unittest.main()