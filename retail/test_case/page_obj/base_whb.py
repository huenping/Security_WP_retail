class Page(object):
    """所有页面的继承"""
    WP_url = 'https://192.168.0.91/index.php/login'

    def __init__(self, selenium_driver, base_url=WP_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self):
        url = self.base_url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def find_element(self, *loc):
        return self.driver.find_elements(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def open(self):
        self._open()

    def on_page(self):
        return self.driver.current_url == self.base_url

    def script(self, src):
        return self.driver.execute_script(src)
