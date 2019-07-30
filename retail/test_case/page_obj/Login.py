from selenium import webdriver


class Login():
    dr = webdriver.Chrome()

    def login(self):
        self.dr.get("http://192.168.0.91")
        self.dr.maximize_window()
        self.dr.find_element_by_xpath("//*[@id='user']").send_keys("admin")
        self.dr.find_element_by_xpath("//*[@id='password']").send_keys("admin2003")
        self.dr.find_element_by_xpath("//*[@id='submit']").click()