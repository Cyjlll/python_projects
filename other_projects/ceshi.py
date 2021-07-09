# _*_ coding: UTF-8 _*_
# @Time : 2021/6/11 14:08
# @Author : caoyujie
# @Site : 
# @File : ceshi.py
# @Software : PyCharm


import time
import pywinauto.application
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import mouse
from pywinauto import application
import pyautogui

def cao():
    one=Application(backend='win32').start(r"C:\IVMS\Client\IVMSClient.exe")
    main=one.window(title="登录")
# main.print_control_identifiers()
    main.Button.click_input()
    time.sleep(10)
    # contentMain=one.window(title="登录")
    # time.sleep(3)
    pywinauto.mouse.click(coords=(34, 146))
    time.sleep(2)
    pywinauto.mouse.click(coords=(1867, 28))
    pywinauto.mouse.click(coords=(1867, 28))
    pywinauto.mouse.click(coords=(908, 582))
    time.sleep(2)


i=1

while i<100:
    cao()
    i+=1
# if __name__ == '__main__':
#     def restart():
#         try:
#             cao()
#         except:
#             print('!!!')
#         finally:
#             restart()