# 主页
from selenium.webdriver.common.by import By

# 主页页面
mine = By.XPATH, '//*[contains(@text,"我的")]'  # 我的

# 我的页面
login = By.XPATH, '//*[contains(@text,"登录")]'  # 登录

# 登录页面
username = By.ID, 'com.bjcsxq.chat.carfriend:id/login_phone_et'  # 账号
passsword = By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et'  # 密码
login_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn'  # 登录按钮
con_btn = By.XPATH, '//*[contains(@text,"确定")]'  # 签到提示框确定按钮
nick_name = By.ID, 'com.bjcsxq.chat.carfriend:id/mine_username_tv'  # 昵称
toast = By.XPATH,'//*[contains(@text,"账户未注册")]'