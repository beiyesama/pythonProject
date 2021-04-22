# coding:utf-8
from selenium import webdriver


class BasePage:
    def __init__(self,driver):
        self.driver = driver
    #封装定位方式
    def find_element(self,*args):
        element = self.driver.find_element(*args)
        return element
    def find_elements(self,*loc):
        elements = self.driver.find_elements(*loc)
        return elements

