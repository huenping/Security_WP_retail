from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

# 发送邮件


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("文件管理系统自动化测试报告", 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect("smtp.goldensecurity.com.cn")
    smtp.login("huep@goldensecurity.com.cn", "absenSXD0115")
    smtp.sendmail("huep@goldensecurity.com.cn", "huep@goldensecurity.com.cn", msg.as_string())
    smtp.quit()
    print('email has send success!')


# 查找最新的测试报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './retail/report/' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='文件管理系统(4.2.2版本）UI自动化测试报告',
                            description='版本：Windows 10 专业版 内存：16G 浏览器：Chrome')
    discover = unittest.defaultTestLoader.discover('./retail/test_case',
                                                   pattern='*_sta.py')
    runner.run(discover)
    fp.close()       # 关闭生成的报告
    file_path = new_report('./retail/report/')     # 查找新生成的报告
    send_mail(file_path)                          # 调用发邮件模块