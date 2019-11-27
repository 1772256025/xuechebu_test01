"""
登录测试用例
"""
import allure
import pytest
from common.utils import init_driver
from page.page_factory import PageFactory
from tools.read_yaml import build_login_data


class TestLogin(object):
    """登录测试类"""

    def setup(self):
        self.driver = init_driver()  # 获取驱动对象
        self.page_factory = PageFactory(self.driver)  # 工厂实例化

    def teardown(self):
        self.driver.quit()  # 退出驱动对象

    @pytest.mark.parametrize('name,pwd,expect,is_success', build_login_data())
    def test_login(self, name, pwd, expect,is_success):
        """登录测试方法"""
        if is_success:
            self.page_factory.home_page.click_mine()  # 点击我的
            self.page_factory.mine_page.click_login()  # 点击登录注册
            self.page_factory.login_page.input_username(name)  # 输入用户名
            self.page_factory.login_page.input_password(pwd)  # 输入密码
            self.page_factory.login_page.click_login_btn()  # 点击登录按钮
            self.page_factory.login_page.click_con_btn()  # 点击签到确认按钮
            nick_name = self.page_factory.login_page.get_nick_name()  # 获取昵称
            print('昵称是：', nick_name)
            try:
                assert expect in nick_name  # 断言判断结果
            except Exception as e:
                # 断言出错截图
                self.driver.get_screenshot_as_file('./screenshot/bug.png')
                # 1.with open 打开截图生成的截图文件，注意：由于打开的是图片文件，因此读取方式应该指定为‘rb'(二进制读取)
                with open('./screenshot/bug.png','rb')as f:
                    # 2.天假图片文件到Allure测试报告中，注意：1）步骤标题  2）读取的文件内容  3）指定添加的文件后缀
                    allure.MASTER_HELPER.attach('断言失败截图',f.read(),allure.MASTER_HELPER.attach_type.PNG)
                raise e   # 主动抛出异常，恢复用例执行状态
        else:
            self.page_factory.home_page.click_mine()  # 点击我的
            self.page_factory.mine_page.click_login()  # 点击登录注册
            self.page_factory.login_page.input_username(name)  # 输入用户名
            self.page_factory.login_page.input_password(pwd)  # 输入密码
            self.page_factory.login_page.click_login_btn()  # 点击登录按钮
            message = self.page_factory.login_page.get_toast()
            assert expect in message
