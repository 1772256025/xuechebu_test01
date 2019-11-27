"""
基类
"""
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element_func(self, location, timeout=10, poll=1):
        """元素定位方法"""
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*location))
        return element

    def click_func(self, location):
        # 元素点击方法
        self.find_element_func(location).click()

    def input_func(self, location, text):
        # 元素输入方法
        element = self.find_element_func(location)
        element.clear()
        element.send_keys(text)
