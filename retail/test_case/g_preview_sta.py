from time import sleep
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.models.function import insert_img, F_insert_img
from selenium.webdriver.common.by import By
from page_obj.base import BasePage


class PreviewTest(MyunitTest, BasePage):
    '''预览功能测试'''

    txtpre_loc = (By.XPATH, "//*[@id='fileList']/tr[5]/td[2]/a/span[1]")
    txtpreclosed_loc = (By.CSS_SELECTOR, "#editor_close")
    pngpre_loc = (By.XPATH, "//*[@id='fileList']/tr[3]/td[2]/a/span[1]")
    pngpreclosed_loc = (By.CSS_SELECTOR, "input.menuItem:nth-child(6)")

    def test_01previewPNGfiles(self):
        # 搜索Preview.png文件并预览
        '''预览.png文件'''
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        sleep(1)
        self.findElement(*self.pngpre_loc).click()
        sleep(5)
        now_title = self.driver.find_element_by_xpath("/html/body/div[8]/div[5]/div").text
        if now_title == "2323.png":
            insert_img(self.driver, "PreviewPNG_true.png")
            self.findElement(*self.pngpreclosed_loc).click()
            self.driver.implicitly_wait(30)
            self.login.quit()
        else:
            F_insert_img(self.driver, "预览PNG错误.png")
            self.findElement(*self.pngpreclosed_loc).click()
            self.driver.implicitly_wait(30)
            self.login.quit()
            sleep(3)

    def test_02previewTXTfiles(self):
        # 搜索预览.txt文件并预览
        '''预览.txt文件'''
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        sleep(1)
        self.findElement(*self.txtpre_loc).click()
        sleep(3)
        now_title = self.driver.title
        if now_title == "test5.txt - 文件 - 文件管理系统内网":
            insert_img(self.driver, "PreviewTXT_true.png")
            self.findElement(*self.txtpreclosed_loc).click()
            self.driver.implicitly_wait(30)
            self.login.quit()
        else:
            F_insert_img(self.driver, "预览TXT错误.png")
            self.findElement(*self.txtpreclosed_loc).click()
            self.driver.implicitly_wait(30)
            self.login.quit()
            sleep(3)


if __name__ == '__main__':
    pass
