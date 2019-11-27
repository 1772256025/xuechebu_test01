"""
登录页面
"""
import page
from base.base_page import BasePage


class LoginPage(BasePage):
    username = page.username
    password = page.passsword
    login_btn = page.login_btn
    con_btn = page.con_btn
    nick_name = page.nick_name
    toast = page.toast
    def input_username(self,name):
        """输入用户名"""
        self.input_func(self.username,name)

    def input_password(self,pwd):
        """输入密码"""
        self.input_func(self.password,pwd)

    def click_login_btn(self):
        """点击登录按钮"""
        self.click_func(self.login_btn)

    def click_con_btn(self):
        """点击签到提示确定按钮"""
        self.click_func(self.con_btn)

    def get_nick_name(self):
        """获取昵称"""
        return self.get_text_func(self.nick_name)
    def get_toast(self):
        """获取toast信息"""
        return self.get_toast_message(self.toast)
