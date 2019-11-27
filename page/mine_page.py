"""
我的页面
"""
import page
from base.base_page import BasePage


class MinePage(BasePage):
    login = page.login
    def click_login(self):
        """点击登录/注册页面"""
        self.click_func(self.login)