# _*_ coding: UTF-8 _*_
# @Time : 2021/6/15 20:09
# @Author : caoyujie
# @Site : 
# @File : lianxiqq.py
# @Software : PyCharm


from pywinauto.application import Application
from pywinauto import application
import autoit
import time
import pywinauto
from pywinauto.keyboard import send_keys



# app=application.Application(backend="uia").connect(handle=135168)
# print(app)


# app=application.Application(backend="uia").connect(handle=986922)

app=application.Application(backend="uia").start(r"D:\Bin\QQScLauncher.exe")
pywinauto.tests.allcontrols.AllControlsTest(windows)
