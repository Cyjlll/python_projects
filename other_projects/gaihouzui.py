# _*_ coding: UTF-8 _*_
# @Time : 2021/5/20 20:25
# @Author : caoyujie
# @Site : 
# @File : exercise.py
# @Software : PyCharm

import time
import pywinauto.application
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import mouse
from pywinauto import application
import pyautogui
import os

# app = pywinauto.application.Application(backend='uia').connect(path="WeChat")
# app = pywinauto.application.Application(backend='uia').start('notepad.exe')
# content=app[r'无标题 - 记事本']
# systray_icons = app.ShellTrayWnd.NotificationAreaToolbar
# connect to outlook
# app.wait_cpu_usage_lower(threshold=5)
# app.window(title='无标题 - 记事本').wait('ready', timeout=5000)
# app.Open.wait_not('visible')
# content.print_control_identifiers()
# content.minimize()
# screenWidth, screenHeight = pyautogui.size()
# print(screenWidth)

# pyautogui.typewrite(message='123',interval=0.5)
# content.Button5.click()
# app['记事本']['不保存'].click()
# pyautogui.keyDown('enter')
# app['取消'].click()

# pywinauto.mouse.double_click  1849,195
# weixin = Application.connect(path='WeChat.exe')
# print(app.HelpTopics.Edit.texts())
# print(systray_icons)
# print(app)

# print(os.name)
# print(os.path.exists('C:/Users/Administrator/Desktop/更新/ivmsdatasvr.exe'))

def modify_suffix(lujing):

    if os.path.exists(lujing):
        # 所有exe后缀的文件
        allfile=[filename for filename in os.listdir(lujing) if filename.endswith('exe')]
        # 去掉后缀名的exe文件
        fileone=[os.path.splitext(one)[0] for one in allfile]
        # print(fileone)

        # oldfile=os.path.join(lujing,str(fileone+diyige))
        # print(oldfile)



        for i in fileone:
            # print(i)
            oldfile=os.path.join(lujing,str(i)+'.exe')
            print(oldfile)
            newfile=os.path.join(lujing,str(i)+'.123')
            print(newfile)
            os.rename(oldfile,newfile)
            print(i+"chenggongl")
    else:
        print('路径不存在')



modify_suffix('C:/Users/Administrator/Desktop/更新/')


