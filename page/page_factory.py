"""
工厂方法
"""
from page.home_page import HomePage
from page.login_page import LoginPage
from page.mine_page import MinePage


class PageFactory(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def home_page(self):
        """主页页面"""
        return HomePage(self.driver)

    @property
    def mine_page(self):
        """我的页面"""
        return MinePage(self.driver)

    @property
    def login_page(self):
        """登录页面"""
        return LoginPage(self.driver)
