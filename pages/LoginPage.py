from selenium.webdriver.common.by import By
from common.BasePage import BasePage
import time
class LoginPage(BasePage):
    #元素定位
    switch_button_ele = (By.CSS_SELECTOR,".iconfont")
    switch_mobile_ele = (By.XPATH,"//div[@class='v-tab']")
    login_mobile_ele =(By.XPATH,"//input[@placeholder='请输入常用手机号码']")
    login_password_ele = (By.CSS_SELECTOR,"[placeholder='请输入密码']")
    login_button_ele = (By.CSS_SELECTOR,".primary.v-btn > .v-btn__content")
    #获取元素对象
    def switch_button(self):
        element = self.find_element(*LoginPage.switch_button_ele)
        return element
    def switch_mobile(self):
        element = self.find_element(*LoginPage.switch_mobile_ele)
        return element
    def login_mobile(self):
        element = self.find_elements(*LoginPage.login_mobile_ele)
        return element[1]
    def login_password(self):
        element = self.find_element(*LoginPage.login_password_ele)
        return element
    def login_button(self):
        element = self.find_element(*LoginPage.login_button_ele)
        return element

    #页面操作
    def login(self,mobile,password):
        self.switch_button().click()
        time.sleep(1)
        self.switch_mobile().click()
        time.sleep(3)
        self.login_mobile().send_keys(mobile)
        self.login_password().send_keys(password)
        self.login_button().click()