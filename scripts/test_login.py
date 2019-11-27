"""
登录测试用例
"""
import pytest

from common.utils import init_driver
from page.page_factory import PageFactory


class TestLogin(object):
    """登录测试类"""

    def setup_class(self):
        self.driver = init_driver()  # 获取驱动对象
        self.page_factory = PageFactory(self.driver)  # 工厂实例化

    def teardown_class(self):
        self.driver.quit()  # 退出驱动对象

    @pytest.mark.parametrize('name,pwd,expect', [('18132519715', '999999', '8189')])
    def test_login(self, name, pwd, expect):
        """登录测试方法"""
        self.page_factory.home_page.click_mine()  # 点击我的
        self.page_factory.mine_page.click_login()  # 点击登录注册
        self.page_factory.login_page.input_username(name)  # 输入用户名
        self.page_factory.login_page.input_password(pwd)  # 输入密码
        self.page_factory.login_page.click_login_btn()  # 点击登录按钮
        self.page_factory.login_page.click_con_btn()  # 点击签到确认按钮
        nick_name = self.page_factory.login_page.get_nick_name()  # 获取昵称
        print('昵称是：', nick_name)
        assert expect in nick_name  # 断言判断结果
