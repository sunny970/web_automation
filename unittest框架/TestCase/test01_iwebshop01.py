# -*- coding:utf-8 -*-
# 导入包
import unittest
from time import sleep
import time , sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class TestCase01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://192.168.43.73/iwebshop/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    # 必须test开头（测试正常登录）
    def test001(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_css_selector('[alt="填写用户名或邮箱"]').send_keys("晴天")

        self.driver.find_element_by_css_selector ('[type="password"]').send_keys ( "111111" )

        self.driver.find_element_by_css_selector('[value="登录"]').click ()
        # 断言assert
        text = self.driver.find_element_by_css_selector('div[class^="body_tool"]>a').text
        try:
            self.assertIn("晴天",text)
        except AssertionError:
            now_time = time.strftime("%Y_%m_%d %H_%M_%S")
            self.driver.get_screenshot_as_file("./image/%s--%s.jpg" % (now_time,sys.exc_info()[1]))
            raise
        # 退出登录
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector('div[class^="body_tool"]>a')).perform()
        self.driver.find_element_by_css_selector('div[class*="out"]>a').click()
        # 回到首页

        self.driver.find_element_by_partial_link_text("首页").click()

    def tearDown(self):

        self.driver.quit()


if __name__ == '__main__':
    unittest.main()