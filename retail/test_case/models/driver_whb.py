from selenium.webdriver import Remote, DesiredCapabilities
from selenium import webdriver
import time


# 启动浏览器驱动
def browser():
    # driver = webdriver.Chrome("D:python/Scripts/chromedriver.exe")
    chromeOptions = webdriver.ChromeOptions()

    # 设定下载文件的保存目录，
    # 如果该目录不存在，将会自动创建
    prefs = {"download.default_directory": "E:\\testDownload"}
    # 将自定义设置添加到Chrome配置对象实例中
    chromeOptions.add_experimental_option("prefs", prefs)
    # 启动带有自定义设置的Chrome浏览器
    driver = webdriver.Chrome(executable_path="E:/Security_retail_test_project/driver/chromedriver.exe", options=chromeOptions)
    # print("234")
    # host = 'http://localhost:4444/wd/hub'
    return driver


if __name__ == '__main__':
    dr = browser()
    # time.sleep(10)
    # dr.quit()
