# -*- coding:utf-8 -*-
# 导入包
import unittest
from time import sleep
from selenium import webdriver
class TestCase01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://192.168.43.73/iwebshop/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    # 必须test开头
    def test001(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_css_selector('[alt="填写用户名或邮箱"]').send_keys("晴天")

        self.driver.find_element_by_css_selector ('[type="password"]').send_keys ( "111111" )

        self.driver.find_element_by_css_selector('[value="登录"]').click ()
    def tearDown(self):

        self.driver.quit()


if __name__ == '__main__':
    unittest.main()