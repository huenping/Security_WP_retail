import os
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .main_page import Main_Page


class UploadFolder(Main_Page):
    """上传文件"""

    def user_login(self):
        # 上传单个文件，登录入口
        self.open()
        self.login_data()
        return self.upload()

    def user_login1(self):
        # 上传多个文件，登录入口
        self.open()
        self.login_data()
        return self.more_upload()

    def user_login2(self):
        # 上传文件夹，登录入口
        self.open()
        self.login_data()
        self.upload_folder()

    def upload(self):
        # 定位到上传位置
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/a")[0].click()
        sleep(2)
        # 定位到‘上传文件’并点击
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[6]/ul/li[1]")[0].click()
        sleep(2)
        # 选择文件并上传（使用Autolt v3）
        os.system("E:\\网盘\\WP_retail_test_project\\retail\\data\\upload_file.exe")
        # 等待上传成功
        sleep(5)
        # 检查文件名
        # 获取所有文件/文件夹标签
        all_file = self.find_elements(By.XPATH, "//tr/td[2]/a/span[1]/span[1]")
        # print(all_file)
        all_file_name = []
        # 获取文件/文件夹名字
        for i in all_file:
            all_name = i.text
            all_file_name.append(all_name)
        return all_file_name

    def more_upload(self):
        # 批量上传文件
        # 定位到上传位置
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/a")[0].click()
        sleep(2)
        # 定位到‘上传文件’并点击
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[6]/ul/li[1]")[0].click()
        sleep(2)
        # 选择文件并上传（使用Autolt v3）
        os.system("E:\\网盘\\WP_retail_test_project\\retail\\data\\upload_files.exe")
        sleep(5)
        # 检查文件名
        # 获取所有文件/文件夹标签
        all_file = self.find_elements(By.XPATH, "//tr/td[2]/a/span[1]/span[1]")
        # print(all_file)
        all_file_name = []
        # 获取文件/文件夹名字
        for i in all_file:
            all_name = i.text
            all_file_name.append(all_name)
        # print(all_file_name)
        # 删除上传的文件



        return all_file_name

    def upload_folder(self):
        # 上传文件夹
        # 定位到上传位置
        # self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/a")[0].click()
        sleep(1)
        # 定位到‘上传文件夹’并点击
        # self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[6]/ul/li[2]")[0].click()
        # sleep(2)
        # 选择文件夹并上传
        # os.system("E:\\网盘\\WP_retail_test_project\\retail\\data\\upload_folder.exe")
        # sleep(10)
        # 拖到确认位置确认
        applet = self.driver.find_element_by_id("controls")
        pics = applet.find_elements_by_xpath("./div[1]")

        sleep(5)
        real_pic = pics[0].find_elements_by_xpath(".//img")
        action_chains = ActionChains(self.browser)

        ActionChains(self.driver).move_to_element_with_offset(15, 0).perform()
        sleep(1)

        ActionChains(self.driver).move_by_offset(40, 0).perform()
        # 刷新一下 （点击文件）
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[2]")[0].click()




