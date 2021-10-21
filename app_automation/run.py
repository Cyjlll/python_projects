# _*_ coding: UTF-8 _*_
# @Time : 2021/10/19 20:29
# @Author : caoyujie
# @Site : 
# @File : run.py.py
# @Software : PyCharm


import unittest
#放在python的安装目录下
import HTMLTestRunner
import time
import os



#指定扫描的用例文件，将匹配的文件批量执行
#discover(参数1，参数2)
###参数1：被执行的文件路径   参数2：被执行的文件名字
suite=unittest.defaultTestLoader.discover('./testcases',pattern='*cases.py')
#生成测试报告  wb二进制的形式写入
file=open(f'./log/result{time.strftime("%Y%m%d")}.html','wb')
#执行
runner=HTMLTestRunner.HTMLTestRunner(stream=file,title='iCarview测试报告')
runner.run(suite)
file.close()

