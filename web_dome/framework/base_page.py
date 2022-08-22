from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from geektime_requests_learn.web_dome.utils.get_cookie import GetCookieLogin


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver is not None:
            self.driver = driver
        else:
            _addr = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
            self.driver = webdriver.Chrome()
            GetCookieLogin(self.driver, _addr).get_cookies()

    def wait(self, by: By, value):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((by, value)))

    def find(self, by, value):
        self.wait(by, value)
        return self.driver.find_element(by, value)

    def find_list(self, by, value):
        self.wait(by, value)
        return self.driver.find_elements(by, value)

    def click(self, by, value):
        self.find(by, value).click()

    def send_keys(self, by, value, content):
        self.find(by, value).clear()
        self.find(by, value).send_keys(content)

    def iframe(self):
        ...

    def close(self):
        return self.driver.close()
