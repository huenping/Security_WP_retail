from time import sleep
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.models.function import insert_img, F_insert_img
from selenium.webdriver.common.by import By
from page_obj.base import BasePage


class MoverTest(MyunitTest, BasePage):
    """移动文件功能测试"""

    # 勾选文件移动到当前目录
    selectfile2_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[4]/td[1]/label")
    moveBtn2_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/thead/tr/th[2]/div/span/a[3]")
    move_loc = (By.XPATH, "//*[@id='body-user']/div[8]/div[2]/button[2]")

    def test_01movefileslocal(self):
        """文件移动到当前目录"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.selectfile2_loc).click()
        self.findElement(*self.moveBtn2_loc).click()
        sleep(0.5)
        self.findElement(*self.move_loc).click()
        moved = self.driver.find_element_by_xpath('//*[@id="notification"]/div').text
        if moved == '无法移动 "test4.txt", 目标已存在':
            insert_img(self.driver, "MovefilesLocal_true.png")
            self.login.quit()
            sleep(3)
        else:
            F_insert_img(self.driver, "移动文件到当前目录错误.png")
            self.login.quit()
            sleep(3)


if __name__ == '__main__':
    pass
