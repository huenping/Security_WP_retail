import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .main_page import Main_Page


class NewFolder(Main_Page):
    """新建文件夹"""

    def user_login1(self):
        # 新建单个文件夹登录入口
        self.open()
        self.login_data()
        # 测试入口
        return self.new_folder()

    def user_login2(self):
        # 新建多个文件夹登录入口
        self.open()
        self.login_data()
        # 测试入口
        data = self.more_folder()
        return data

    def user_login3(self):
        # 新建重名文件夹
        self.open()
        self.login_data()
        return self.again_folder()

    # 文件名
    file_name = "atest" + str(random.randint(0, 100))

    def new_folder(self):
        # 新建单个文件夹
        # 定位到创建文件夹输入框位置，直接输入
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[1]/label/span[2]/input")[0].send_keys(self.file_name)
        sleep(1)
        # 点击确定
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[1]/label/span[2]/button")[0].click()
        sleep(5)
        # 获取所有文件夹标签
        all_file = self.find_elements(By.XPATH, "//tbody/tr")
        all_file_name = []
        # 获取文件夹名字
        for i in all_file:
            all_name = i.get_attribute("data-file")
            all_file_name.append(all_name)
        # print(all_file_name)
        return all_file_name

    def more_folder(self):
        # 创建多层级文件夹
        # 文件名
        file_name = "test" + str(random.randint(0, 100))
        # # 定位到+位置点击
        # self.find_element(By.XPATH, "//div[@id='controls']/div[2]/a")[0].click()
        # # 定位到新建文件夹按钮点击
        # self.find_element(By.XPATH, "//div//a[@class='menuitem']")[0].click()
        # sleep(1)
        # 定位到创建文件夹输入框位置，直接输入
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[1]/label/span[2]/input")[0].send_keys(file_name)
        sleep(1)
        # 点击确定
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[1]/label/span[2]/button")[0].click()
        sleep(1)
        # 刷新一下 （点击文件）
        # self.find_element(By.XPATH, "//ul[@id='appmenu']/li[1]")[0].click()
        # 按照时间排序
        # self.find_element(By.XPATH, "//div/div/div[2]/div[3]/table/thead/tr/th[4]/a")[0].click()
        # 创建多级目录
        a = 1
        while True:
            # 点击进入当前文件夹
            # print(file_name)
            now_folder = "//tbody/tr[@data-file='" + file_name + "']/td[2]/a/span[1]"
            self.find_element(By.XPATH, now_folder)[0].click()
            sleep(2)
            # # 定位到+位置点击
            # self.find_element(By.XPATH, "//div[@id='controls']/div[2]/a")[0].click()
            # sleep(1)
            # # 定位到新建文件夹按钮点击
            # self.find_element(By.XPATH, "//div//a[@class='menuitem']")[0].click()
            # sleep(1)
            file_name1 = "test" + str(a)
            # 定位到创建文件夹输入框位置，直接输入
            self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[1]/label/span[2]/input")[0].send_keys(file_name1)
            sleep(1)
            # 点击确定
            self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[1]/label/span[2]/button")[0].click()
            sleep(1)
            # 换成当前文件夹名
            file_name = file_name1
            sleep(2)
            # 控制循环创建文件夹层级数
            if a == 5:
                all_file = self.find_elements(By.XPATH, "//a[@class='name']/span[1]")[0].text
                break
            a += 1
        # # 回到主页
        # self.find_element(By.XPATH, "//ul[@id='appmenu']/li[1]/a")[0].click()
        # sleep(1)
        # # 删除创建的文件夹
        # self.find_element(By.XPATH, "//tr[@data-file='" + file_name + "']/td[1]/label")[0].click()
        # sleep(1)
        # self.find_element(By.XPATH, "//table[@id='filestable']/thead/tr/th[4]/span/a")[0].click()
        # sleep(1)

        return file_name, all_file

    def again_folder(self):
        # 新建重名文件夹
        # 与创建单个文件夹相同的文件夹名
        # 定位到创建文件夹输入框位置，直接输入
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[1]/label/span[2]/input")[0].send_keys(
            self.file_name)
        sleep(1)
        # 点击确定
        self.find_element(By.XPATH, "//div[@id='my_style']/div[1]/div[1]/label/span[2]/button")[0].click()
        sleep(1)

        again_name = self.file_name + " (2)"
        # 验证
        # 获取信息
        all_file = self.find_elements(By.XPATH, "//tbody/tr")
        all_file_name = []
        # 获取文件夹名字
        for i in all_file:
            all_name = i.get_attribute("data-file")
            all_file_name.append(all_name)
        # 删除创建的文件夹
        self.find_element(By.XPATH, "//tr[@data-file='"+ self.file_name +"']/td[1]/label")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//tr[@data-file='"+ again_name +"']/td[1]/label")[0].click()
        sleep(1)
        self.find_element(By.XPATH, "//table[@id='filestable']/thead/tr/th[4]/span/a")[0].click()
        sleep(1)


        return again_name, all_file_name

