from time import sleep
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.models.function import insert_img, F_insert_img
from selenium.webdriver.common.by import By
from page_obj.base import BasePage
from selenium.webdriver.common.keys import Keys


class RenameTest(MyunitTest, BasePage):
    """重命名功能测试"""

    # 重命名文件
    renamefiles_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[4]/td[1]/label")
    renameBtn_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/thead/tr/th[2]/div/span/a[1]")
    renameInp_loc = (By.XPATH, "//*[@id='fileList']/tr[4]/td[2]/form/input")
    # 重命名文件重名
    renamefiles2_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[5]/td[1]/label")
    renameInp2_loc = (By.XPATH, "//*[@id='fileList']/tr[20]/td[2]/form/input")
    # 重命名文件与文件夹重名
    renamefiles3_loc = (By.XPATH, ".has-controls > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > a:nth-child(1) > span:nth-child(3) > a:nth-child(2)")
    renameInp3_loc = (By.XPATH, "//*[@id='fileList']/tr[1]/td[2]/form/input")
    clearBtn_loc = (By.XPATH, "//*[@id='header']/div[2]/form/button")
    # 重命名文件夹
    renamefolder_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[2]/td[1]/label")
    renameInp4_loc = (By.XPATH, "//*[@id='fileList']/tr[2]/td[2]/form/input")
    # 重命名文件夹与父文件夹重名
    menu5_loc = (By.XPATH, "//*[@id='fileList']/tr/td[2]/a/span[3]/a[2]")
    renameInp5_loc = (By.XPATH, "//*[@id='fileList']/tr/td[2]/form/input")
    # 重命名文件夹与同级文件夹重名
    menu6_loc = (By.XPATH, "//*[@id='fileList']/tr[9]/td[2]/a/span[3]/a[2]")
    renameInp6_loc = (By.XPATH, "//*[@id='fileList']/tr[9]/td[2]/form/input")

    def test_01renamefiles(self):
        """文件重命名"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.renamefiles_loc).click()
        self.findElement(*self.renameBtn_loc).click()
        sleep(1)
        self.findElement(*self.renameInp_loc).send_keys("HEP文件", Keys.ENTER)
        sleep(1)
        namefile = self.driver.find_element_by_css_selector(".has-controls > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2) > a:nth-child(1) > span:nth-child(2) > span:nth-child(1)").text
        if namefile == "HEP文件":
            insert_img(self.driver, "RenameFiles_true.png")
            self.login.quit()
        else:
            F_insert_img(self.driver, "重命名文件错误.png")
            self.driver.implicitly_wait(30)
            self.login.quit()
            sleep(3)

    '''def test_renamefilesrepeat(self):
        """重命名文件与其他文件重名"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.menu2_loc).click()
        self.findElement(*self.renameBtn_loc).click()
        self.findElement(*self.renameInp2_loc).send_keys("重命名文件成功", Keys.ENTER)
        repeatname = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[89]/td[2]/form/div/div[2]").text
        if repeatname == ' "重命名文件成功.docx" 已经存在':
            insert_img(self.driver, "RenameFilesRepeat_true.png")
            self.login.quit()
        else:
            F_insert_img(self.driver, "重命名文件重名错误.png")
            self.driver.implicitly_wait(30)
            self.login.quit()
            sleep(3)

    def test_renamefilesfolder(self):
        """重命名文件与文件夹重名"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.search_loc).click()
        self.findElement(*self.search_loc).send_keys("6366.docx")
        sleep(0.5)
        self.findElement(*self.menu3_loc).click()
        self.findElement(*self.renameBtn_loc).click()
        self.findElement(*self.renameInp3_loc).send_keys("omg", Keys.ENTER)
        sleep(1)
        self.findElement(*self.search_loc).click()
        self.findElement(*self.clearBtn_loc).click()
        sleep(0.5)
        self.findElement(*self.search_loc).send_keys("omg")
        sleep(1)
        Dname = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/table/tfoot/tr/td[2]").text
        if Dname == " 1 个文件夹 和 1 个文件 匹配 'omg'":
            insert_img(self.driver, "RenameFilesFolder_true.png")
            self.login.quit()
        else:
            F_insert_img(self.driver, "重命名文件与文件夹名重名错误.png")
            self.driver.implicitly_wait(30)
            self.login.quit()
            sleep(3)'''

    def test_02renamefolders(self):
        """重命名文件夹"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.renamefolder_loc).click()
        sleep(1)
        self.findElement(*self.renameBtn_loc).click()
        sleep(1)
        self.findElement(*self.renameInp4_loc).send_keys("hep文件夹", Keys.ENTER)
        sleep(1)
        Folrename = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[2]/td[2]/a/span[1]/span").text
        if Folrename == "hep文件夹":
            insert_img(self.driver, "RenameFolders_true.png")
            self.login.quit()
        else:
            F_insert_img(self.driver, "重命名文件夹错误.png")
            self.driver.implicitly_wait(30)
            self.login.quit()
            sleep(3)

    '''def test_renamefolderfather(self):
        """重命名文件夹与父文件夹重名"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.search_loc).click()
        self.findElement(*self.search_loc).send_keys("nice儿")
        sleep(0.5)
        self.findElement(*self.menu5_loc).click()
        self.findElement(*self.renameBtn_loc).click()
        self.findElement(*self.renameInp5_loc).send_keys("莫妮卡文件夹", Keys.ENTER)
        sleep(1)
        insert_img(self.driver, "RenameFolderfather_true.png")
        self.login.quit()
        sleep(3)

    def test_renamefolderrepeat(self):
        """重命名文件夹与同级文件夹重名"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.search_loc).click()
        self.findElement(*self.search_loc).send_keys("马尔扎哈文件夹")
        sleep(0.5)
        self.findElement(*self.menu6_loc).click()
        self.findElement(*self.renameBtn_loc).click()
        self.findElement(*self.renameInp6_loc).send_keys("迪丽热巴文件夹", Keys.ENTER)
        sleep(1)
        Folderrepeatname = self.driver.find_element_by_xpath("//*[@id='tooltip305053']/div[2]").text
        if Folderrepeatname == ' "迪丽热巴文件夹" 已经存在':
            insert_img(self.driver, "RenameFolderRepeat_true.png")
            self.login.quit()
        else:
            F_insert_img(self.driver, "重命名文件夹与同级文件夹重名错误.png")
            self.driver.implicitly_wait(30)
            self.login.quit()
            sleep(3)'''


if __name__ == '__main__':
    pass
