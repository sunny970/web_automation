# -*- coding:utf-8 -*-
# 导入包
import unittest , time

from tools.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':

    suite = unittest.defaultTestLoader.discover("../TestCase/",pattern="test*.py")

    # dir_path = "../result/"
    # now_time = time.strftime ( "%Y_%m_%d %H_%M_%S" )
    # file = dir_path + now_time + "report.html"

    file =  "../result/"+time.strftime ( "%Y_%m_%d %H_%M_%S" )+"report.html"

    with open(file,"wb") as R:
        # runner = HTMLTestRunner(stream=R,title="web自动化测试",description="操作系统：win10")
        # runner.run ( suite )
        HTMLTestRunner ( stream=R , title="web自动化测试" , description="操作系统：win10" ).run ( suite )



