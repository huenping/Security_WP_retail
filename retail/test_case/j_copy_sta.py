from time import sleep
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.models.function import insert_img, F_insert_img
from selenium.webdriver.common.by import By
from page_obj.base import BasePage


class CopyTest(MyunitTest, BasePage):
    """复制文件功能测试"""

    # 勾选文件复制到当前目录
    selectfile1_loc = (By.XPATH, "//*[@id='fileList']/tr[4]/td[1]/label")
    copyBtn_loc = (By.XPATH, "//*[@id='selectedActionsList']/a[3]")
    clickBtn_loc = (By.XPATH, "//*[@id='searchresults']/table/tbody/tr[2]/td[2]")
    copy_loc = (By.XPATH, "//*[@id='body-user']/div[8]/div[2]/button[1]")

    def test_01copyfiles(self):
        """文件复制到当前目录"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.selectfile1_loc).click()
        self.findElement(*self.copyBtn_loc).click()
        sleep(0.5)
        self.findElement(*self.copy_loc).click()
        sleep(1)
        copyd = self.driver.find_element_by_xpath('//*[@id="notification"]/div').text
        if copyd == '无法复制 "test4.txt", 目标存在':
            insert_img(self.driver, "CopyFiles_true.png")
            self.login.quit()
            sleep(3)
        else:
            F_insert_img(self.driver, "复制文件到当前目录错误.png")
            self.login.quit()
            sleep(3)


if __name__ == '__main__':
    pass
