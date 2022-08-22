from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from geektime_requests_learn.web_dome.framework.base_page import BasePage
from geektime_requests_learn.web_dome.page.contact_page import ContactPage


class HomePage(BasePage):
    def __init__(self, driver: WebDriver = None):
        super().__init__(driver)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    def home_page(self):
        def loop_click():
            self.click(By.LINK_TEXT, '首页')
            return len(self.find_list(By.LINK_TEXT, '添加成员')) > 0
        WebDriverWait(self.driver, 10).until(loop_click)
        return self

    def contact_page(self):
        def loop_click(driver):
            self.click(By.LINK_TEXT, '通讯录')
            return len(self.find_list(By.LINK_TEXT, '批量设置成员信息')) > 0
        WebDriverWait(self.driver, 10).until(loop_click)
        return ContactPage(self.driver)
