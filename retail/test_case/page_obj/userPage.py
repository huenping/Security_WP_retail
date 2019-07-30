import os
import random
import xlrd
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from .main_page import Main_Page


class UserManagement(Main_Page):
    """用户管理"""
    a = random.randint(10,99)
    # 用户名
    user_name = "t" + str(a)
    # user_name = "t1"
    # 姓名
    username = "test" + str(a)
    # 修改姓名
    username1 = "admin" + str(a)
    # 邮箱
    email = "12345678" + str(a) + "@qq.com"
    # 手机号
    phone_number = "123456789" + str(a)
    # 地址
    user_address = "科技大厦" + str(a) + "号楼"
    # 存储空间
    ROM = "2 GB"
    # 部门名称
    class_name = "test_login"
    # 修改部门名称
    modify_class_name = "test_login1"

    def user_login1(self):
        # 添加部门
        self.open()
        self.login_admin()
        return self.add_class()

    def user_login2(self):
        # 修改部门名称
        self.open()
        self.login_admin()
        return self.modify_class()

    def user_login3(self):
        # 清楚选择
        self.open()
        self.login_admin()
        return self.clear_selection()

    def user_login4(self):
        # 添加用户
        self.open()
        self.login_admin()
        return self.user_add()

    def user_login5(self):
        # 修改姓名登录
        self.open()
        self.login_admin()
        return self.modify_name()

    def user_login6(self):
        # 修改密码
        self.open()
        self.login_admin()
        return self.modify_passwd()

    def user_login7(self):
        # 修改邮箱
        self.open()
        self.login_admin()
        return self.modify_email()

    def user_login8(self):
        # 修改手机号
        self.open()
        self.login_admin()
        return self.modify_phone()

    def user_login9(self):
        # 修改地址
        self.open()
        self.login_admin()
        return self.modify_addr()

    def user_login10(self):
        # 修改存储空间
        self.open()
        self.login_admin()
        return self.modify_ROM()

    def user_login11(self):
        # 用户删除
        self.open()
        self.login_admin()
        return self.user_del()

    def user_login12(self):
        # 用户导入
        self.open()
        self.login_admin()
        return self.user_import()

    def user_login13(self):
        # 用户导出
        self.open()
        self.login_admin()
        return self.user_export()

    def user_login14(self):
        # 删除部门
        self.open()
        self.login_admin()
        return self.del_class()




    def add_class(self):
        """添加部门"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(2)
        # 点击添加部门
        self.find_element(By.XPATH, "//div[@id='content']/div/div[1]/div/div[1]/div[2]/div/button[1]")[0].click()
        sleep(1)
        # 输入部门名称
        self.find_element(By.XPATH, "//div[@id='content']/div/div[3]/div/div[2]/form/div/div/div/input")[0].send_keys(self.class_name)
        sleep(1)
        # 提交
        self.find_element(By.XPATH, "//div[@id='content']/div/div[3]/div/div[3]//div/button[2]")[0].click()
        sleep(1)
        # 检查
        # 获取所有部门名称
        class_name_xpath = self.find_elements(By.XPATH, "//div[@id='content']/div/div[1]/div/div[2]//span[2]")
        class_names = []
        for i in class_name_xpath:
            name = i.text
            class_names.append(name)

        return class_names

    def modify_class(self):
        """修改部门名称"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(2)
        # 选择要修改的部门（上次创建的部门）
        self.find_element(By.XPATH, "//div[@role='tree']//span[text()='"+ self.class_name +"']")[0].click()
        sleep(1)
        # 点击修改
        self.find_element(By.XPATH, "//div[@id='content']/div/div[1]/div/div[1]/div[2]/div/button[2]")[0].click()
        sleep(1)
        # 清空输入框
        # 选中输入框中的数据
        self.find_element(By.XPATH, "//div[@id='content']/div/div[3]/div/div[2]/form/div/div/div/input")[0].send_keys(Keys.CONTROL, 'a')
        sleep(1)
        # 剪切
        self.find_element(By.XPATH, "//div[@id='content']/div/div[3]/div/div[2]/form/div/div/div/input")[0].send_keys(Keys.CONTROL, 'x')
        sleep(1)
        # 输入名称
        self.find_element(By.XPATH, "//div[@id='content']/div/div[3]/div/div[2]/form/div/div/div/input")[0].send_keys(self.modify_class_name)
        sleep(1)
        # 提交
        self.find_element(By.XPATH, "//div[@id='content']/div/div[3]//button[2]")[0].click()
        sleep(2)
        # 检查
        # 获取所有部门名称
        class_name_xpath = self.find_elements(By.XPATH, "//div[@id='content']/div/div[1]/div/div[2]//span[2]")
        class_names = []
        for i in class_name_xpath:
            name = i.text
            class_names.append(name)

        return class_names

    def clear_selection(self):
        """清除选择"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(2)
        # 选中一个部门，获取class是否变化
        # //div[@role='tree']/@class
        self.find_element(By.XPATH, "//div[@role='tree']/div[1]")[0].click()
        sleep(1)
        class_value = self.find_element(By.XPATH, "//div[@role='tree']")[0].get_attribute("class")
        # print(class_value)

        if class_value != "el-tree el-tree--highlight-current":
            self.driver.quit()
        sleep(1)
        # 点击清除按钮
        self.find_element(By.XPATH, "//div[@id='content']/div/div[1]/div/div[1]/div[2]/div/button[5]")[0].click()
        sleep(1)
        # 再次获取class的值
        class_value_again = self.find_element(By.XPATH, "//div[@role='tree']")[0].get_attribute("class")
        print(class_value_again)
        return class_value_again

    def user_add(self):
        """用户添加"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(2)
        # 选择部门
        self.find_element(By.XPATH, "//div[@id='treeContent']/div/div/span[(text()='" + self.modify_class_name + "')]")[0].click()
        sleep(2)
        # 点击添加用户按钮
        self.find_element(By.XPATH, "//div[@id='contacts']/div/div/div/button[1]")[0].click()
        sleep(2)
        # 输入信息，用户名，姓名，密码，确认密码
        self.find_element(By.XPATH, "//form/div[1]/div/div/input")[0].send_keys(self.user_name)
        sleep(1)
        self.find_element(By.XPATH, "//form/div[3]/div/div/input")[0].send_keys(self.username)
        sleep(1)
        self.find_element(By.XPATH, "//form/div[4]/div[1]/div/div/input")[0].send_keys("123456")
        sleep(1)
        self.find_element(By.XPATH, "//form/div[4]/div[2]/div/div/input")[0].send_keys("123456")
        sleep(1)
        # 提交
        self.find_element(By.XPATH, "//*[@id='app-contacts']/div[5]/div/div[3]/div/button[2]")[0].click()
        sleep(1)
        # 刷新
        self.find_element(By.XPATH, "//div[@id='contacts']/div/div/div/button[3]")[0].click()
        sleep(1)
        # 获取所有文件名
        files_name = self.find_elements(By.XPATH, "//tbody/tr/td[2]")

        all_filename = []
        # 获取文件xpath，并获取文件名
        for i in files_name:
            name = i.text
            all_filename.append(name)
        # print(all_filename)
        return all_filename

    def modify_name(self):
        """修改姓名"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(1)
        # 选择部门
        self.find_element(By.XPATH, "//div[@id='treeContent']/div/div/span[(text()='" + self.modify_class_name + "')]")[0].click()
        sleep(1)
        # 选择需要修改的用户和需要修改的信息
        # 这个是修改名字
        self.find_element(By.XPATH, "//*[text()='"+ self.user_name +"']/parent::*/following-sibling::td[1]/div/img")[0].click()
        sleep(2)
        # 清空输入框
        # 选中输入框中的数据
        self.find_element(By.XPATH, "//form[@class='el-form']/div[3]/div/div/input")[0].send_keys(Keys.CONTROL, 'a')
        sleep(1)
        # 剪切
        self.find_element(By.XPATH, "//form[@class='el-form']/div[3]/div/div/input")[0].send_keys(Keys.CONTROL, 'x')
        sleep(1)
        # 输入修改的数据
        self.find_element(By.XPATH, "//form[@class='el-form']/div[3]/div/div/input")[0].send_keys(self.username1)
        sleep(1)
        # 确认提交
        self.find_element(By.XPATH, "//div[@id='content']/div[1]/div[5]/div[1]/div[3]/div/button[2]")[0].click()
        sleep(0.5)
        # 刷新
        self.find_element(By.XPATH, "//div[@id='contacts']/div/div/div/button[3]")[0].click()
        sleep(1)
        # 获取所有文件名
        files_name = self.find_elements(By.XPATH, "//*[text()='"+ self.user_name +"']/parent::*/following-sibling::td[1]/div/span")
        all_filename = []
        # 获取文件xpath，并获取文件名
        for i in files_name:
            name = i.text
            all_filename.append(name)
        # print(all_filename)
        return all_filename

    def modify_passwd(self):
        """修改密码"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(1)
        # 选择部门
        self.find_element(By.XPATH, "//div[@id='treeContent']/div/div/span[(text()='" + self.modify_class_name + "')]")[0].click()
        sleep(1)
        # 选择需要修改的用户和需要修改的信息
        self.find_element(By.XPATH,"//*[text()='" + self.user_name + "']/parent::*/following-sibling::td[2]/div/img")[0].click()
        sleep(1)
        # 输入修改的数据，新密码
        self.find_element(By.XPATH, "//form[@class='el-form']/div[4]/div[1]/div/div/input")[0].send_keys("123456")
        sleep(1)
        # 确认密码输入
        self.find_element(By.XPATH, "//form[@class='el-form']/div[4]/div[2]/div/div/input")[0].send_keys("123456")
        sleep(1)
        # 确认提交
        self.find_element(By.XPATH, "//div[@id='content']/div[1]/div[5]/div[1]/div[3]/div/button[2]")[0].click()
        sleep(0.5)
        # 检查
        info = self.find_elements(By.XPATH, "//div[@role='alert']/p")
        info_passwd = info[0].text
        return info_passwd

    def modify_email(self):
        """修改邮箱"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(1)
        # 选择部门
        self.find_element(By.XPATH, "//div[@id='treeContent']/div/div/span[(text()='" + self.modify_class_name + "')]")[0].click()
        sleep(1)
        # 选择修改的信息
        self.find_element(By.XPATH, "//*[text()='" + self.user_name + "']/parent::*/following-sibling::td[3]/div/img")[0].click()
        sleep(1)
        # 清空输入框
        self.find_element(By.XPATH, "//form[@class='el-form']/div[6]/div/div[1]/input")[0].clear()
        # self.driver.find_element_by_xpath("//form[@class='el-form']/div[6]/div/div[1]/input").clear()
        sleep(1)
        # 输入邮箱
        self.find_element(By.XPATH, "//form[@class='el-form']/div[6]/div/div/input")[0].send_keys(self.email)
        sleep(1)
        # 提交
        self.find_element(By.XPATH, "//div[@id='content']/div[1]/div[5]/div[1]/div[3]/div/button[2]")[0].click()
        sleep(2)
        # 检查
        files_name = self.find_elements(By.XPATH, "//*[text()='" + self.user_name + "']/parent::*/following-sibling::td[3]/div/span")
        all_filename = []
        # 获取文件xpath，并获取文件名
        for i in files_name:
            name = i.text
            all_filename.append(name)
        # print(all_filename)
        return all_filename

    def modify_phone(self):
        """修改手机号"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(1)
        # 选择部门
        self.find_element(By.XPATH, "//div[@id='treeContent']/div/div/span[(text()='" + self.modify_class_name + "')]")[0].click()
        sleep(1)
        # 选择修改的信息
        self.find_element(By.XPATH, "//*[text()='" + self.user_name + "']/parent::*/following-sibling::td[4]/div/img")[0].click()
        sleep(1)
        # 清空输入框
        self.find_element(By.XPATH, "//form[@class='el-form']/div[7]/div/div/input")[0].clear()
        sleep(1)
        # 输入手机号
        self.find_element(By.XPATH, "//form[@class='el-form']/div[7]/div/div/input")[0].send_keys(self.phone_number)
        sleep(1)
        # 提交
        self.find_element(By.XPATH, "//div[@id='content']/div[1]/div[5]/div[1]/div[3]/div/button[2]")[0].click()
        sleep(1)
        # 检查
        phone_xpath = self.find_elements(By.XPATH, "//*[text()='" + self.user_name + "']/parent::*/following-sibling::td[4]/div/span")
        phone_numbers = []
        # 获取手机xpath，并获取手机号码
        for i in phone_xpath:
            name = i.text
            phone_numbers.append(name)
        return phone_numbers

    def modify_addr(self):
        """修改地址"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(1)
        # 选择部门
        self.find_element(By.XPATH, "//div[@id='treeContent']/div/div/span[(text()='" + self.modify_class_name + "')]")[0].click()
        sleep(1)
        # 选择修改的信息
        self.find_element(By.XPATH, "//*[text()='" + self.user_name + "']/parent::*/following-sibling::td[5]/div/img")[
            0].click()
        sleep(1)
        # 清空输入框
        self.find_element(By.XPATH, "//form[@class='el-form']/div[8]/div/div/input")[0].clear()
        sleep(1)
        # 输入手机号
        self.find_element(By.XPATH, "//form[@class='el-form']/div[8]/div/div/input")[0].send_keys(self.user_address)
        sleep(1)
        # 提交
        self.find_element(By.XPATH, "//div[@id='content']/div[1]/div[5]/div[1]/div[3]/div/button[2]")[0].click()
        sleep(1)
        # 检查
        address_xpath= self.find_elements(By.XPATH, "//*[text()='" + self.user_name + "']/parent::*/following-sibling::td[5]/div/span")
        addresses = []
        # 获取地址xpath，并获取地址信息
        for i in address_xpath:
            name = i.text
            addresses.append(name)
        return addresses

    def modify_ROM(self):
        """修改存储空间"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(1)
        # 选择部门
        self.find_element(By.XPATH, "//div[@id='treeContent']/div/div/span[(text()='" + self.modify_class_name + "')]")[0].click()
        sleep(1)
        # 选择修改的信息
        self.find_element(By.XPATH, "//*[text()='" + self.user_name + "']/parent::*/following-sibling::td[6]/div/img")[
            0].click()
        sleep(1)
        # 清空输入框
        # 选中数据
        self.find_element(By.XPATH, "//form[@class='el-form']/div[5]/div/div/input")[0].send_keys(Keys.CONTROL, 'a')
        sleep(1)
        # 剪切
        self.find_element(By.XPATH, "//form[@class='el-form']/div[5]/div/div/input")[0].send_keys(Keys.CONTROL, 'x')
        sleep(1)
        # 输入存储空间大小
        self.find_element(By.XPATH, "//form[@class='el-form']/div[5]/div/div/input")[0].send_keys(self.ROM)
        sleep(1)
        # 提交
        self.find_element(By.XPATH, "//div[@id='content']/div[1]/div[5]/div[1]/div[3]/div/button[2]")[0].click()
        sleep(1)
        # 检查
        ROM_xpath = self.find_elements(By.XPATH, "//*[text()='" + self.user_name + "']/parent::*/following-sibling::td[6]/div/span")
        ROMs = []
        # 获取修改后的存储空间xpath
        for i in ROM_xpath:
            name = i.text
            ROMs.append(name)
        print(ROMs)
        return ROMs

    def user_del(self):
        """用户删除"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(1)
        # 选择部门
        self.find_element(By.XPATH, "//div[@id='treeContent']/div/div/span[(text()='" + self.modify_class_name + "')]")[0].click()
        sleep(1)
        # 选择用户
        self.find_element(By.XPATH, "//*[text()='"+ self.user_name + "']/parent::*/preceding-sibling::td")[0].click()
        sleep(1)
        # 点击删除
        self.find_element(By.XPATH, "//div[@id='contacts']/div/div/div/button[2]")[0].click()
        sleep(1)
        # 确认删除
        self.find_element(By.XPATH, "//div[@class='el-message-box']/div[3]/button[2]")[0].click()
        sleep(5)
        # 检查
        # 获取所有用户名
        files_name = self.find_elements(By.XPATH, "//tbody/tr/td[2]")
        all_names = []
        # 获取文件xpath，并获取文件名
        for i in files_name:
            name = i.text
            all_names.append(name)
        return all_names

    def user_import(self):
        """用户导入"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(2)
        # 判断是否存在usertest部门
        # 获取部门名称
        classnames_xpath = self.find_elements(By.XPATH, "//div[@role='tree']/div/div/span[2]")
        sleep(1)
        class_names = []
        for i in classnames_xpath:
            class_name = i.text
            class_names.append(class_name)

        if "usertest" not in class_names:
        # 点击添加部门
            self.find_element(By.XPATH, "//div[@id='content']/div/div[1]/div/div[1]/div[2]/div/button[1]")[0].click()
            sleep(1)
            # 输入部门名称
            self.find_element(By.XPATH, "//div[@id='content']/div/div[3]/div/div[2]/form/div/div/div/input")[0].send_keys("usertest")
            sleep(1)
            # 提交
            self.find_element(By.XPATH, "//div[@id='content']/div/div[3]/div/div[3]//div/button[2]")[0].click()
            sleep(1)
        # 选择部门
        self.find_element(By.XPATH, "//div[@id='treeContent']/div/div/span[(text()='usertest')]")[0].click()
        sleep(2)
        user_xpath = self.find_elements(By.XPATH, "//div[@id='contacts']/div[3]/div/div[3]/table/tbody/tr[1]/td[2]/div")
        sleep(1)
        # 如果存在用户，删除
        if user_xpath:
            self.find_element(By.XPATH, "//div[@id='contacts']/div[3]/div/div[2]/table/thead/tr/th[1]/div/label/span/span")[0].click()
            sleep(1)
            self.find_element(By.XPATH, "//div[@id='contacts']/div[2]/div/div/button[2]")[0].click()
            sleep(1)
            self.find_element(By.XPATH, "//div[@class='el-message-box']/div[3]/button[2]")[0].click()
            sleep(10)

        # 点击上传用户按钮
        self.find_element(By.XPATH, "//div[@id='contacts']/div/div/div/button[4]")[0].click()
        sleep(1)
        # 点击选择文件夹
        self.find_element(By.XPATH, "//form[@id='uploadForm']/input")[0].click()
        sleep(1)
        # 选择文件并（使用Autolt v3）
        os.system("E:\\网盘\\WP_retail_test_project\\retail\\data\\upload_user.exe")
        sleep(1)
        # 点击导入用户按钮
        self.find_element(By.XPATH, "//*[@id='app-contacts']/div[4]/div/div[2]/div[2]/form/div[2]/div/button")[0].click()
        sleep(10)
        # 获取导入的用户名
        file_names_xpath = self.find_elements(By.XPATH, "//tbody/tr/td[2]")
        all_names = []
        # 获取文件xpath，并获取文件名
        for i in file_names_xpath:
            name = i.text
            all_names.append(name)
        # 获取excel表中的用户名
        # 表中的数据
        excel_data = xlrd.open_workbook('E:\\网盘\\WP_retail_test_project\\retail\\data\\成员.xls')
        # 哪一张表的数据
        table = excel_data.sheet_by_name("test部门成员")
        # 哪一行
        # table.row_values(2) # 获取第三行用户名的值，返回列表
        # 哪一列
        excel_names = table.col_values(0)  # 获取第三列的值，返回列表
        sleep(1)
        # # 将导入的数据删除
        # # 点击全选按钮
        # self.find_element(By.XPATH, "//*[@id='contacts']/div[3]/div/div[2]/table/thead/tr/th[1]/div/label/span/span")[0].click()
        # sleep(1)
        # # 点击删除按钮
        # self.find_element(By.XPATH, "//div[@id='contacts']/div/div/div/button[2]")[0].click()
        # sleep(1)
        # # 确认删除
        # self.find_element(By.XPATH, "//div[@class='el-message-box']/div[3]/button[2]")[0].click()
        # sleep(15)

        return all_names, excel_names

    def user_export(self):
        # 用户导出
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(2)
        # 选择部门
        self.find_element(By.XPATH, "//div[@id='treeContent']/div/div/span[(text()='usertest')]")[
            0].click()
        sleep(2)
        # 点击导出用户按钮
        self.find_element(By.XPATH, "//div[@id='contacts']/div/div/div/button[5]")[0].click()
        sleep(5)
        file_list = os.listdir("E:/testDownload")
        # 删除文件，方便下次下载
        try:
            os.remove("E:/testDownload/usertest部门成员.xls")
        except Exception as e:
            pass
        return file_list

    def del_class(self):
        """删除部门"""
        # 点击通讯录
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[3]")[0].click()
        sleep(2)
        # 选择要删除的部门（上次创建的部门）//div[@role='tree']//span[text()='test1']
        self.find_element(By.XPATH, "//div[@role='tree']//span[text()='"+ self.modify_class_name +"']")[0].click()
        sleep(1)
        # 如果存在用户则删除用户后再删除部门
        # 点击删除
        self.find_element(By.XPATH, "//div[@id='content']/div/div[1]/div/div[1]/div[2]/div/button[3]")[0].click()
        sleep(1)
        # 提交
        self.find_element(By.XPATH, "//div[@role='dialog']/div/div[3]/button[2]")[0].click()
        sleep(1)
        # 检查
        # 获取所有部门名称
        class_name_xpath = self.find_elements(By.XPATH, "//div[@id='content']/div/div[1]/div/div[2]//span[2]")
        class_names = []
        for i in class_name_xpath:
            name = i.text
            class_names.append(name)

        return class_names





