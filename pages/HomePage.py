import time

from selenium.webdriver.common.by import By
from common.BasePage import BasePage

class HomePage(BasePage):
    #元素定位
    home_login_ele =(By.XPATH,"//ul[@class='topbar-right pull-right']//a[contains(.,'登录')]")
    home_name_ele = (By.XPATH,"//p[@class='fs16 textover']")
    #获得元素对象
    def home_login(self):
        element = self.find_element(*HomePage.home_login_ele)
        return element
    def home_name(self):
        element = self.find_element(*HomePage.home_name_ele)
        return element
    #页面操作
    def home_login_click(self):
        self.home_login().click()
        time.sleep(3)
    def home_name_get_text(self):
        text = self.home_name().text
        return text
    def is_login_success(self):
        if self.home_name_get_text() != "Hi，你好":
            return True
        else:
            return False

