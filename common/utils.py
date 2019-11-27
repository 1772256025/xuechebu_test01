"""
获取驱动对象
"""
from appium import webdriver


def init_driver():
    capabilities = {  # 声明启动参数
        "platformName": "Android",  # 平台类型（iOS 或 Android)
        "platformVersion": "5.1",  # 手机系统版本
        "deviceName": "模拟器",  # 设备名称
        "appPackage": "com.bjcsxq.chat.carfriend",  # 待测应用的包名
        "appActivity": ".MainActivity"  # 待测应用的启动名
    }
    # com.bjcsxq.chat.carfriend/.MainActivity
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                              desired_capabilities=capabilities)  # 实例化驱动对象
    return driver


if __name__ == '__main__':
    init_driver()
