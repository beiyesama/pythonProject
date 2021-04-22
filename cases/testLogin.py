# coding:utf-8
import unittest
import ddt
import time
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from selenium import webdriver

@ddt.ddt
class TestLogin(unittest.TestCase):

    testData = [{'mobile': '15658678027', 'password': '123456dbb'},
                {'mobile': '19965412404', 'password': '654321dbb'}]
    @ddt.data(*testData)
    def test01(self,data):
        driver = webdriver.Chrome()
        driver.get("http://aliyun.32.cn")
        driver.maximize_window()
        HomePage(driver).home_login_click()
        LoginPage(driver).login(data["mobile"],data["password"])
        time.sleep(5)
        result = HomePage(driver).is_login_success()
        self.assertTrue(result)
        driver.quit()


if __name__=="__main__":
    unittest.main()
