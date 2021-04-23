# coding:utf-8
import unittest
import ddt
import time
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from selenium import webdriver
from common.xlrd_read_xlsx import ExcelRead

@ddt.ddt
class TestLogin(unittest.TestCase):
    path = r"A:\pythonProject\data\test.xlsx"
    sheetname = "Sheet1"
    testData = ExcelRead(path,sheetname).get_data()
    print(testData)
    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.quit()
    @ddt.data(*testData)
    def test01(self,data):
        self.driver.get("http://aliyun.32.cn")
        self.driver.maximize_window()
        HomePage(self.driver).home_login_click()
        LoginPage(self.driver).login(data["mobile"],data["password"])
        time.sleep(5)
        result = HomePage(self.driver).is_login_success()
        self.assertTrue(result)

if __name__=="__main__":
    unittest.main()
