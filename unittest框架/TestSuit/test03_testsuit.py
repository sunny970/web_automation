# -*- coding:utf-8 -*-
# 导入包
import unittest

import time

from tools.HTMLTestRunner import HTMLTestRunner
if __name__ == '__main__':
    # 创建用例打包对象并添加指定目录下的xx开头的文件
    suite = unittest.defaultTestLoader.discover("../TestCase/",pattern="test*.py")
    # 生成的报告存放位置
    dir_path = "../result/"
    # 时间
    now_time = time.strftime ( "%Y_%m_%d %H_%M_%S" )
    # 报告
    file = dir_path+now_time+"report.html"
    # 打开 写入数据
    with open(file,"wb") as R:
        runner = HTMLTestRunner(stream=R,title="web自动化测试",description="操作系统：win10")
        # 执行
        runner.run(suite)



