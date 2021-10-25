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

import time

current_time=time.strftime("%y-%m-%d-%H-%M-%S",time.localtime(time.time()))
print(current_time)
