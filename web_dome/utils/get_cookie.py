import os
from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def savefile_path(filename):
    path_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', filename)
    return path_dir


class GetCookieLogin:
    def __init__(self, driver: WebDriver, address):
        """
        :param driver: 传入一个driver
        :param address: 访问登录页面的地址
        """
        self.driver = driver
        self.path = savefile_path('cookie.yaml')
        self.addr = address

    def save_cookies(self):
        """ 保存cookie的方法 """
        self.driver.get(self.addr)
        sleep(20)
        cookie = self.driver.get_cookies()
        with open(self.path, 'w') as f:
            yaml.safe_dump(cookie, f)

    def get_cookies(self):
        """ 加载cookie的方法 """
        self.driver.get(self.addr)
        cookie = yaml.safe_load(open(self.path))
        for c in cookie:
            self.driver.add_cookie(c)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    GetCookieLogin(driver, 'https://work.weixin.qq.com/wework_admin/frame#index').save_cookies()
