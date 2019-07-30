import os
import zipfile
from time import sleep
from selenium.webdriver.common.by import By
from .main_page import Main_Page


class DownFolder(Main_Page):
    """下载文件/文件夹"""
    def user_login1(self):
        # 打开网页
        self.open()
        # 输入密码登录
        self.login_data()
        # 调用下载，并且返回文件名
        return self.download_file()

    def user_login2(self):
        self.open()
        # 输入密码登录
        self.login_data()
        # 调用下载，并且返回文件名
        return self.download_folder()

    def download_file(self):
        """下载文件"""
        #TODO 根据文件名选择下载文件，如需下载其他文件，只要在这里修改文件名就可以
        file_xpath = "//td//span[@class='nametext']/span[contains(text(),'123321')]"
        # 选择文件
        self.find_element(By.XPATH, file_xpath)
        # 文件名
        file_name = self.find_element(By.XPATH, file_xpath + "/parent::span")[0].text
        sleep(2)
        # 点击操作
        self.find_element(By.XPATH, file_xpath + "/parent::span/following-sibling::span/a[2]")[0].click()
        sleep(2)
        # 定位下载按钮点击下载
        self.find_element(By.XPATH, "//td/div//li[5]")[0].click()
        sleep(10)
        # 获取之后删除，方便下次上传
        self.find_element(By.XPATH, "//tr[@data-file='123321.txt']/td[1]/label")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//span[@class='nametext']/span[text()='123321']/parent::*/parent::*/span[2]/a[2]")[
            0].click()
        sleep(1)
        self.find_element(By.XPATH, "//tr[@data-file='123321.txt']/td[2]/div/ul/li[6]")[0].click()
        sleep(1)

        # 在电脑中获取下载的所有文件
        name_list = os.listdir("E:\\testDownload")
        # 从电脑中删除下载的文件
        for file in os.listdir("E:\\testDownload"):
            if file == file_name:
                os.remove("E:\\testDownload\\" + file)
        return file_name, name_list

    def download_folder(self):
        """下载文件和文件夹"""
        folder_name = "test(测试文件夹)"
        # 定位到创建文件夹输入框位置，直接输入
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[1]/label/span[2]/input")[0].send_keys(folder_name)
        sleep(1)
        # 点击确定
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[1]/label/span[2]/button")[0].click()
        sleep(1)
        # 选择文件夹
        self.find_element(By.XPATH, "//td//span[@class='nametext']/span[text()='"+ folder_name + "']/ancestor::*/td/label")[0].click()
        sleep(1)
        # 选择文件
        self.find_element(By.XPATH, "//td//span[@class='nametext']/span[text()='test1']/ancestor::*/td/label")[0].click()
        sleep(1)
        # 点击下载
        self.find_element(By.XPATH, "//th[@id='headerName']/div//a[@class='download']")[0].click()
        sleep(10)
        # 获取文件名
        file_name = self.find_element(By.XPATH, "//td//span[@class='nametext']/span[text()='test1']/ancestor::*/td/label/parent::*/parent::*")[0].get_attribute("data-file")
        # print(file_name)
        # 解压下载的压缩包
        f = zipfile.ZipFile("E:/testDownload/download.zip", 'r')
        # file_list = f.namelist()
        # 解压到当前文件夹
        for file in f.namelist():
            f.extract(file,"E:/testDownload")
        # 获取当前文件夹内的文件
        file_list = os.listdir("E:\\testDownload")
        # 删除创建的文件夹
        # 选择文件夹
        sleep(1)
        self.find_element(By.XPATH,"//td//span[@class='nametext']/span[text()='test1']/ancestor::*/td/label")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//table[@id='filestable']/thead/tr/th[4]/span/a")[0].click()
        sleep(1)


        return folder_name, file_name, file_list
