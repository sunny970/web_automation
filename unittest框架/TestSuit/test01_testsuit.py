# -*-coding:utf8-*-
# 导入包
import unittest
# 导入用例--类
from TestCase.test01_iwebshop01 import TestCase01

if __name__ == '__main__':
    # 创建用例打包对象
    suite = unittest.TestSuite()
    # 添加用例  一条一条添加 -----方法1
    # suite.addTest(TestCase01("test001"))
    # 添加用例  直接添加用例类  -----方法2
    # suite.addTest (unittest.makeSuite(TestCase01))
    # 添加用例  直接添加用例类  -----方法3
    suite.addTest (unittest.makeSuite(TestCase01))
    # 执行
    unittest.TextTestRunner().run(suite)