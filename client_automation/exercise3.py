# _*_ coding: UTF-8 _*_
# @Time : 2021/5/18 20:08
# @Author : caoyujie
# @Site : 
# @File : standard.py
# @Software : PyCharm

import time
import pywinauto
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import application


# new = Application(backend='uia').connect(handle=0x001D1752)
# content=new.window(title="智能车辆监控系统")
# content.print_control_identifiers()
for i in range(1,8):
    j="RadioButton"+str(i)
    print(j)
# content.HelpTopics.ListBox.select(2)
# content.RadioButton1.click_input()
# content.RadioButton2.click_input()
# content.RadioButton3.click_input()
# content.RadioButton4.click_input()
# content.RadioButton5.click_input()
# content.RadioButton6.click_input()
# content.RadioButton7.click_input()
# content.RadioButton8.click_input()


weixin=Application.connect()