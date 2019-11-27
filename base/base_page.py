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

    def get_text_func(self, location):
        """获取特定文本信息方法"""
        return self.find_element_func(location).text

    def get_toast_message(self, location):
        """获取toast信息"""
        # xpath = '//*[contains(@text."{}")]'.format(text)
        # element = WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(By.XPATH,xpath))
        # print('获取的toast信息为：',element.text)
        return self.find_element_func(location).text
    def get_attribute_func(self,location,attr_name):
        """元素获取属性方法"""
        element =self.find_element_func(location)
        return element.get_attribute(attr_name)
