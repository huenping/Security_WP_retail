from time import sleep
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.models.function import insert_img, F_insert_img
from selenium.webdriver.common.by import By
from page_obj.base import BasePage


class SearchTest(MyunitTest, BasePage):
    '''精确搜索功能测试'''

    search_loc = (By.XPATH, "//*[@id='searchbox']")

    def test_01searchfiles(self):
        '''搜索文件'''
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        sleep(1)
        self.findElement(*self.search_loc).click()
        sleep(0.5)
        self.findElement(*self.search_loc).send_keys("2323.png")
        sleep(2)
        # 验证搜索结果是否正确
        filesname = self.driver.find_element_by_css_selector("span.info").text
        if filesname == "1 个文件 匹配 '2323.png'":
            insert_img(self.driver, "SearchFiles_true.png")
            self.login.quit()
        else:
            F_insert_img(self.driver, "搜索文件错误.png")
            self.login.quit()
            sleep(3)

    def test_02searchfolder(self):
        '''搜索文件夹'''
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        sleep(1)
        self.findElement(*self.search_loc).click()
        sleep(0.5)
        self.findElement(*self.search_loc).send_keys("保存的分享")
        sleep(3)
        # 验证搜索结果是否正确
        foldername = self.driver.find_element_by_css_selector("span.info").text
        if foldername == "1 个文件夹 匹配 '保存的分享'":
            insert_img(self.driver, "SearchFolder_true.png")
            self.login.quit()
        else:
            F_insert_img(self.driver, "搜索文件夹错误.png")
            print(foldername)
            self.login.quit()
            sleep(3)


if __name__ == '__main__':
    pass

