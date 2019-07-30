import os
from time import sleep
from selenium.webdriver.common.by import By

from .main_page import Main_Page


class ReplaceAvatar(Main_Page):
    """更换头像"""
    def user_login1(self):
        self.open()
        self.login_data()
        return self.local_acatar()

    def user_login2(self):
        self.open()
        self.login_data()
        return self.upload_acatar()

    def local_acatar(self):
        # TODO
        """上传网盘中的图片"""
        # 点击进去个人设置页面
        self.find_element(By.XPATH, "//div[@id='settings']/div[1]/div[1]")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//div[@id='settings']/div[2]/ul/li[1]")[0].click()
        sleep(1)
        # 获取当前账户头像的src
        url1 = self.find_element(By.XPATH, "//div[@id='displayavatar']/div[1]/img")[0].get_attribute("src")
        sleep(1)
        # 点击在网盘中寻找头像
        self.find_element(By.XPATH, "//div[@id='displayavatar']/div[3]")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//div[@id='oc-dialog-filepicker-content']/span/div/a")[0].click()
        sleep(1)
        # 选中图片
        self.find_element(By.XPATH, "//table[@id='filestable']/tbody/tr[@data-entryname='2323.png']")[0].click()
        sleep(1)
        # 点击选择按钮
        self.find_element(By.XPATH, "//div/button[@class='primary']")[0].click()
        sleep(10)
        # 点击选择个人头像
        self.find_element(By.XPATH, "//div[@id='cropper']/div/div[3]")[0].click()
        sleep(10)
        # 再次获取图片的src
        url2 = self.find_element(By.XPATH, "//div[@id='displayavatar']/div[1]/img")[0].get_attribute("src")
        # 上传后删除之前上传的文件
        # 回到文件主页
        self.find_element(By.XPATH, "//ul[@id='appmenu']/li[1]/a")[0].click()
        sleep(2)
        # 选择之前上传的文件
        '''self.find_element(By.XPATH, "//tr[@data-file='2323.png']/td[1]/label")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//tr[@data-file='test1.txt']/td[1]/label")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//tr[@data-file='test2.txt']/td[1]/label")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//tr[@data-file='test3.txt']/td[1]/label")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//tr[@data-file='test4.txt']/td[1]/label")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//tr[@data-file='test5.txt']/td[1]/label")[0].click()
        sleep(1)'''
        # 删除
        '''self.find_element(By.XPATH, "//table[@id='filestable']/thead/tr/th[4]/span/a")[0].click()
        sleep(1)'''

        return url1, url2

    def upload_acatar(self):
        """上传电脑中的图片"""
        # 点击进去个人设置页面
        self.find_element(By.XPATH, "//div[@id='settings']/div[1]/div[1]")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//div[@id='settings']/div[2]/ul/li[1]")[0].click()
        sleep(1)
        # 获取当前账户头像的src
        url1 = self.find_element(By.XPATH, "//div[@id='displayavatar']/div[1]/img")[0].get_attribute("src")
        sleep(1)
        # 点击在电脑中寻找头像
        self.find_element(By.XPATH, "//div[@id='displayavatar']/label")[0].click()
        sleep(1)
        # 选中图片 打开
        os.system("E:\\网盘\\WP_retail_test_project\\retail\\data\\upload_picture.exe")
        sleep(2)
        # 点击选择个人头像
        self.find_element(By.XPATH, "//div[@id='cropper']/div/div[3]")[0].click()
        sleep(5)
        # 获取图片的src
        url2 = self.find_element(By.XPATH, "//div[@id='displayavatar']/div[1]/img")[0].get_attribute("src")


        return url1, url2









