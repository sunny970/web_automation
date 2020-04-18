# -*- coding:utf-8 -*-
# 导入包
import unittest
from time import sleep
import time , sys
from selenium import webdriver


class TestCase01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://192.168.43.73/iwebshop/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    # 必须test开头（测试异常登录--密码错误）
    def test001(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_css_selector('[alt="填写用户名或邮箱"]').send_keys("晴天")

        self.driver.find_element_by_css_selector ('[type="password"]').send_keys ( "11111111" )

        self.driver.find_element_by_css_selector('[value="登录"]').click ()
        # 断言assert
        text = self.driver.find_element_by_css_selector('.prompt').text
        try:
            self.assertIn("密码错误",text)
        except AssertionError:
            now_time = time.strftime("%Y_%m_%d %H_%M_%S")
            self.driver.get_screenshot_as_file("./image/%s--%s.jpg" % (now_time,sys.exc_info()[1]))
            raise


    def tearDown(self):
        # 回到首页
        self.driver.find_element_by_partial_link_text ( "首页" ).click ()

        # 退出
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()