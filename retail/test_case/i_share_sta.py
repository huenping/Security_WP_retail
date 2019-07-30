from time import sleep
from retail.test_case.models.myunit import MyunitTest
from retail.test_case.models.function import insert_img, F_insert_img
from selenium.webdriver.common.by import By
from page_obj.base import BasePage


class ShareTest(MyunitTest, BasePage):
    """共享功能测试"""

    shareBtn_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/div[1]/div[4]")
    shareInput_loc = (By.XPATH, "//*[@id='shareWith-view17']")
    shareSelect_loc = (By.CSS_SELECTOR, ".share-autocomplete-item")
    # 用户分享
    files1_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[4]/td[1]/label")
    # 用户组分享
    files2_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[5]/td[1]/label")
    shareSelect1_loc = (By.XPATH, "/html/body/ul/li[2]/a/div")
    # 部门分享
    files3_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[6]/td[1]/label")
    # 树形分享
    Treeshare_loc = (By.XPATH, "//*[@id='shareWithRemoteInfo']")
    openTree_loc = (By.XPATH, "//*[@id='treeDemo_1_switch']")
    openDemo1_loc = (By.XPATH, "//*[@id='treeDemo_2_switch']")
    switch1_loc = (By.XPATH, "//*[@id='treeDemo_4_span']")
    submit_loc = (By.XPATH, "//*[@id='shareAdd']")
    # 取消分享
    Nsendmeaum_loc = (By.XPATH, "/html/body/div[3]/div/div[1]/ul/li[3]/a")
    CshareBtn_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[8]/table/tbody/tr[1]/td[1]/a/span[2]/a[1]")
    menuBtn_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[7]/div[2]/div/div/div/div/div[3]/ul/li/span[2]/a/span")
    CLBtn_loc = (By.XPATH, "//*[@id='shareWithList']/li/span[2]/div/ul/li[2]/a")
    Cshare_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[8]/table/tfoot/tr/td[1]/span/span[3]")
    # 撤销编辑权限
    undoshare_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[6]/td[2]/a/span[2]/a[1]/span[2]")
    undoedit_loc = (By.CSS_SELECTOR, ".sharingOptionsGroup>span:nth-child(1)>label:nth-child(2)")
    # 复制直接链接
    files4_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/table/tbody/tr[9]/td[1]/label")
    Clink_loc = (By.XPATH, "/html/body/div[3]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/a")

    def test_01shareuser(self):
        '''分享文件给用户'''
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.files1_loc).click()
        self.findElement(*self.shareBtn_loc).click()
        sleep(0.5)
        self.findElement(*self.shareInput_loc).send_keys("userdemo")
        sleep(1)
        self.findElement(*self.shareSelect_loc).click()
        self.driver.implicitly_wait(10)
        sharetext = self.driver.find_element_by_css_selector(".username").text
        if sharetext == "userdemo":
            insert_img(self.driver, "ShareFiles_true.png")
            self.login.quit()
        else:
            self.driver.implicitly_wait(30)
            F_insert_img(self.driver, "分享文件给用户未成功.png")
            self.login.quit()
        sleep(3)

    def test_02sharegroup(self):
        """分享给用户组"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.files2_loc).click()
        self.findElement(*self.shareBtn_loc).click()
        sleep(0.5)
        self.findElement(*self.shareInput_loc).send_keys("admin")
        sleep(1)
        self.findElement(*self.shareSelect_loc).click()
        self.driver.implicitly_wait(10)
        Gsharetext = self.driver.find_element_by_css_selector(".username").text
        if Gsharetext == "admin (群组)":
            insert_img(self.driver, "ShareGroup_true.png")
            self.login.quit()
        else:
            self.driver.implicitly_wait(30)
            F_insert_img(self.driver, "分享文件夹给共享组未成功.png")
            self.login.quit()
        sleep(3)

    def test_03sharedepartment(self):
        """分享文件给部门"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.files3_loc).click()
        self.findElement(*self.shareBtn_loc).click()
        sleep(0.5)
        self.findElement(*self.shareInput_loc).send_keys("login")
        sleep(1)
        self.findElement(*self.shareSelect_loc).click()
        self.driver.implicitly_wait(10)
        Dsharetext = self.driver.find_element_by_css_selector(".username").text
        if Dsharetext == "login (部门)":
            insert_img(self.driver, "ShareDepartment_true.png")
            self.login.quit()
        else:
            self.driver.implicitly_wait(30)
            F_insert_img(self.driver, "分享文件给部门未成功.png")
            self.login.quit()
        sleep(3)

    def test_04treeshare(self):
        """树形分享给内部用户"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.files4_loc).click()
        sleep(0.5)
        self.findElement(*self.shareBtn_loc).click()
        sleep(0.5)
        self.findElement(*self.Treeshare_loc).click()
        sleep(0.5)
        self.findElement(*self.openTree_loc).click()
        sleep(0.5)
        self.findElement(*self.openDemo1_loc).click()
        sleep(0.5)
        self.findElement(*self.switch1_loc).click()
        sleep(0.5)
        self.findElement(*self.submit_loc).click()
        self.driver.implicitly_wait(10)
        Treesharetext = self.driver.find_element_by_css_selector(".username").text
        if Treesharetext == "1":
            insert_img(self.driver, "TreeSharingInternal_true.png")
            self.login.quit()
        else:
            self.driver.implicitly_wait(30)
            F_insert_img(self.driver, "文件树形分享给内部用户未成功.png")
            self.login.quit()
        sleep(3)

    def test_05sharecancel(self):
        """取消分享"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.Nsendmeaum_loc).click()
        for i in range(3):
            self.findElement(*self.CshareBtn_loc).click()
            sleep(0.5)
            self.findElement(*self.menuBtn_loc).click()
            sleep(0.5)
            self.findElement(*self.CLBtn_loc).click()
            sleep(1)
            self.driver.refresh()
        sleep(1)
        Cancelsharetext = self.driver.find_element_by_xpath("//*[@id='emptycontent']/h2").text
        if Cancelsharetext == "还没有发送过文件":
            insert_img(self.driver, "CancelShare_true.png")
            self.login.quit()
        else:
            self.driver.implicitly_wait(30)
            F_insert_img(self.driver, "取消所有分享未成功.png")
            self.login.quit()
        sleep(3)

    def test_06cplink(self):
        """复制直接链接"""
        self.login.loginFunc()
        self.driver.implicitly_wait(30)
        self.findElement(*self.files4_loc).click()
        self.findElement(*self.shareBtn_loc).click()
        sleep(0.5)
        self.findElement(*self.Clink_loc).click()
        insert_img(self.driver, "CpLink_true.png")
        self.login.quit()
        sleep(3)


if __name__ == '__main__':
    pass


















        


