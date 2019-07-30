import os
import random
from time import sleep
from selenium.webdriver.common.by import By
from .main_page import Main_Page


class ShareGroup(Main_Page):
    """共享组的组成员"""
    # 共享组名称
    group_name = "test1"

    def user_login1(self):
        self.open()
        self.login_data()
        return self.add_group()

    def user_login2(self):
        self.open()
        self.login_data()
        return self.del_group()

    def user_login3(self):
        self.open()
        self.login_data()
        return self.add_user()

    def user_login4(self):
        self.open()
        self.login_data()
        return self.del_user()

    def add_group(self):
        # 添加共享组
        # 选择共享组
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[4]")[0].click()
        sleep(2)
        # 点击添加
        self.find_element(By.XPATH, "//div[@id='content']/div/div[1]/div/div/div/button[1]")[0].click()
        sleep(1)
        # 输入组名称
        self.find_element(By.XPATH, "//form[@class='el-form']/div[2]/div/div/input")[0].send_keys(self.group_name)
        sleep(1)
        # 提交
        self.find_element(By.XPATH, "//div[@id='content']/div/div[4]/div/div[3]/div/button[2]")[0].click()
        sleep(1)
        # 检查
        # 获取所有共享组名称
        group_names_xpath = self.find_elements(By.XPATH, "//span[@id='galen-cs']/span")
        group_names = []
        for i in group_names_xpath:
            name = i.text
            group_names.append(name)

        return group_names

    def del_group(self):
        # 删除共享组

        # 选择共享组
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[4]")[0].click()
        sleep(2)
        # 选择要删除的组(在上面创建的)
        self.find_element(By.XPATH, "//span[@id='galen-cs']/span[contains(text(), '" + self.group_name + "')]/parent::span/parent::span/span[2]/button")[0].click()
        sleep(1)
        # 确认
        self.find_element(By.XPATH, "//div[@role='dialog']/div/div[3]/button[2]")[0].click()
        sleep(1)
        # 检查
        # 获取所有共享组名称
        group_names_xpath = self.find_elements(By.XPATH, "//span[@id='galen-cs']/span")
        group_names = []
        for i in group_names_xpath:
            name = i.text
            group_names.append(name)

        return group_names

    def add_user(self):
        # 组成员添加用户
        # 选择共享组
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[4]")[0].click()
        sleep(2)
        # 选中组
        self.find_element(By.XPATH, "//span[@id='galen-cs']/span[text()='test1']")[0].click()
        sleep(2)
        # 点击添加成员
        self.find_element(By.XPATH, "//div[@id='groupUserBtn']/div/div/button[1]")[0].click()
        sleep(2)
        # 选择成员
        self.find_element(By.XPATH, "//div[@role='tree']/div/div/span[text()='usertest (部门)']")[0].click()
        sleep(2)
        self.find_element(By.XPATH, "//div[@role='tree']/div/div/span[text()='usertest (部门)']/parent::*/parent::div/div[2]/div[3]/div/label")[0].click()
        sleep(2)
        # 获取添加的姓名
        user_name = self.find_element(By.XPATH, "//div[@role='tree']/div/div/span[text()='usertest (部门)']/parent::*/parent::div/div[2]/div[3]/div/span[2]")[0].text
        # 点击添加
        self.find_element(By.XPATH, "//div[@id='app-group']/div[3]/div/div[3]/div/button[2]")[0].click()
        sleep(2)
        # 点击刷新
        self.find_element(By.XPATH, "//div[@id='groupUserBtn']/div/div/button[3]")[0].click()
        sleep(2)
        # 检查，获取组内用户的姓名
        usernames_xpath = self.find_elements(By.XPATH, "//tr[@class='el-table__row']/td[3]")
        all_names = []
        for i in usernames_xpath:
            name = i.text
            all_names.append(name)

        return user_name, all_names

    def del_user(self):
        # 组成员删除用户
        # 选择共享组
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[4]")[0].click()
        sleep(2)
        # 选中组
        self.find_element(By.XPATH, "//span[@id='galen-cs']/span[text()='test1']")[0].click()
        sleep(2)
        # 选中添加的用户
        self.find_element(By.XPATH, "//table[@class='el-table__body']/tbody/tr/td[3]/div/span[text()='3']/parent::div/parent::td/preceding-sibling::*/preceding-sibling::*")[0].click()
        # 获取添加用户的用户名
        username = self.find_element(By.XPATH, "//table[@class='el-table__body']/tbody/tr/td[3]/div/span[text()='3']/parent::div/parent::td/preceding-sibling::*[1]")[0].text
        sleep(2)
        # 点击删除
        self.find_element(By.XPATH, "//div[@id='groupUserBtn']/div/div/button[2]")[0].click()
        sleep(2)
        # 确定
        self.find_element(By.XPATH, "//div[@role='dialog']/div/div[3]/button[2]")[0].click()
        sleep(2)
        # 点击刷新
        self.find_element(By.XPATH, "//div[@id='groupUserBtn']/div/div/button[3]")[0].click()
        sleep(2)
        # 检查
        # 获取组内所有用户名
        usernames_xpath = self.find_elements(By.XPATH, "//tr[@class='el-table__row']/td[2]")
        all_names = []
        for i in usernames_xpath:
            name = i.text
            all_names.append(name)

        return username, all_names


