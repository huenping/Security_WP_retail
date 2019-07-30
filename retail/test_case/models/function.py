import os


def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('test_case')[0]
    file_path = base + "report/image/pass/" + file_name
    driver.get_screenshot_as_file(file_path)


def F_insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('test_case')[0]
    file_path = base + "report/image/Fail/" + file_name
    driver.get_screenshot_as_file(file_path)
