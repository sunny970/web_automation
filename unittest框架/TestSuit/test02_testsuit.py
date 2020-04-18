# -*- coding:utf-8 -*-
# 导入包
import unittest


if __name__ == '__main__':
    # 创建用例打包对象并添加指定目录下的xx开头的文件
    suite = unittest.defaultTestLoader.discover("../TestCase",pattern="test*.py")
    # 执行
    unittest.TextTestRunner().run ( suite )
