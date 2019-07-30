from selenium import webdriver
from time import sleep
import sys

# 定义浏览器驱动


class WDriver(object):

    def chromeDriver(self):
        self.driver = webdriver.Chrome()
        return self.driver


if __name__ == '__main__':
    WDrive=WDriver()
    WDrive.chromeDriver()