# -*- coding:utf-8 -*-
# 导入包
import unittest , time , sys
from selenium import webdriver

url = ""

class TestCase01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    # 必须test开头（测试正常登录）
    def test001(self):
        # 测试内容
        pass
        # 断言
        try:
            self.assertIn("xx",yy)
        except AssertionError:
            now_time = time.strftime("%Y_%m_%d %H_%M_%S")
            self.driver.get_screenshot_as_file("../image/%s--%s.jpg" % (now_time,sys.exc_info()[1]))
            raise

    def tearDown(self):
        # 退出游览器
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()