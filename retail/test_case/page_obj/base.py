from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from retail.test_case.models.log import Logger
import os
import logging
import sys

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)


class BasePage(object):
    """页面基础类，用于所有页面的继承"""

    def __init__(self, driver, url='http:192.168.0.91'):
        self.driver = driver
        self.base_url = url
        self.timeout = 30

    def _open(self, url):
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except Exception as e:
            log.logger.exception(e, exc_info=True)
            raise ValueError('%s address access error, please check！' %url)
        else:
            log.logger.info('%s is accessing address %s at line[46]' % (sys._getframe().f_code.co_name, url))

    def open(self):
        self._open(self.base_url)
        log.logger.info('%s loading successed!' % self.base_url)
        return self.base_url

    def findElement(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            log.logger.exception('finding element timeout!, details', exc_info=True)
            raise e
        else:
            log.logger.info('The page of %s had already find the element %s' % (self, loc))
            return self.driver.find_element(*loc)

    def findElements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            log.logger.exception('finding element timeout!, details', exc_info=True)
            raise e
        else:
            log.logger.info('The page of %s had already find the element %s' % (self, loc))
            return self.driver.find_elements(*loc)

    def inputValue(self, inputBox, value):
        inputB = self.findElement(*inputBox)
        try:
            inputB.clear()
            inputB.send_keys(value)
        except Exception as e:
            log.logger.exception('typing value error!', exc_info=True)
            raise e
        else:
            log.logger.info('inputValue:[%s] is receiveing value [%s]' % (inputBox, value))

    def script(self, src):
        try:
            self.driver.excute_script(src)
        except Exception as e:
            log.logger.exception('execute js script [%s] failed ' %src)
            raise e
        else:
            log.logger.info('execute js script [%s] successed ' % src)

    def isElementExist(self, element):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))
        except:
            return False
        else:
            return True

    def accept(self, *loc):
        self.findElement(*loc).click()
        log.logger.info('closed the error information fram successed!')


if __name__ == '__main__':
    pass

