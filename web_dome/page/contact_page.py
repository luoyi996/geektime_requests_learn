from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from geektime_requests_learn.web_dome.framework.base_page import BasePage
from geektime_requests_learn.web_dome.page.member_page import MemberPage
from geektime_requests_learn.web_dome.params_data import AddMember


class ContactPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def add_member(self, member: AddMember):
        self.click(By.LINK_TEXT, '添加成员')
        self.send_keys(By.ID, 'username', member.username)
        self.send_keys(By.ID, 'memberAdd_english_name', member.english_name)
        self.send_keys(By.ID, 'memberAdd_acctid', member.account)
        self.send_keys(By.NAME, 'biz_mail', member.biz_mail + Keys.ENTER)
        self.send_keys(By.ID, 'memberAdd_phone', member.phone)
        self.send_keys(By.ID, 'memberAdd_telephone', member.telephone)
        self.send_keys(By.ID, 'memberEdit_address', member.address)
        self.send_keys(By.ID, 'memberAdd_mail', member.member_mail)
        self.send_keys(By.ID, 'memberAdd_title', member.position)
        self.click(By.LINK_TEXT, '保存')
        return self

    def search(self):
        return MemberPage()
