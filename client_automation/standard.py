# _*_ coding: UTF-8 _*_
# @Time : 2021/3/29 9:16
# @Author : caoyujie
# @Site : 
# @File : slag_test.py
# @Software : PyCharm

import time
import pywinauto.application
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto import mouse
from pywinauto import application
import pyautogui
# 启动方式一
one=Application(backend='uia').start(r"C:\IVMS\NewClientWpf\NewClientWpf.exe")

# 启动方式二
# one=Application().connect(process=21904)
# 捕捉登陆窗口
main=one.window(title="智能车辆监控系统")
# 然后打印这个窗口下的所有节点
# main.print_control_identifiers()
# 登陆
def login():
    # 用户名的框
    user_frame=main.edit
    # 在框里输入用户名
    user_frame.type_keys("111")
    # 密码的框
    pwd_frame=main.Edit2
    # 输入密码
    # pwd_frame.type_keys('{END}')
    # pwd_frame.type_keys('{BACKSPACE}' * 6)
    # pwd_frame.type_keys("000000")
    # set_text 设置文本，已有清除
    pwd_frame.set_text("000000")
    # 获取服务器的框
    svr_frame=main.Edit3
    # 输入ip地址
    svr_frame.type_keys("192.168.168.90")
    # 回车登陆
    main.Button3.type_keys("{VK_RETURN}")
# 等待登陆窗口消失后
    time.sleep(5)
# dlg = one.top_window()
# 获取客户端的窗口
mainn=one.window(title="智能车辆监控系统")
mainn.wait("exists",timeout=3,retry_interval=2)
mainn.draw_outline(colour ='green',thickness = 2,rect = None)

# 首页里面热力图的展示
def click_homepage():
    # mainn.print_control_identifiers()
    mainn.RadioButton1.click_input()
    # shouye= mainn.top_window()
    # 等到窗户真的开着
    # actionable_dlg = mainn.wait('visible')
    # mainn.print_control_identifiers()
    # mainn.Static1.click_input()
    mainn.Static2.click_input()
    mainn.Static3.click_input()
    mainn.Static4.click_input()

    pywinauto.mouse.click(button='left', coords=(1736, 22))

#拉框搜索
def add_rectangle():
    # 点击这个拉框搜索的图片并点击
    mainn.Image50.click_input()
    # 按下鼠标按钮
    pywinauto.mouse.press(button='left', coords=(514, 275))
    # 释放鼠标按钮
    pywinauto.mouse.release(button='left', coords=(676, 431))

# 勾选车辆
def check_vehicle():
    # mainn.CheckBox4.CheckByClick()
    mainn.CheckBox4.click_input()
    # mainn.CheckBox4.wait('enabled').click()
    # CheckByClick(*args, **kwargs)


# mainn.RadioButton3.click_input()
# mainn.RadioButton1.click_input()
# mainn.RadioButton4.click_input()
# mainn.RadioButton5.click_input()
# mainn.RadioButton6.click_input()
# mainn.RadioButton7.click_input()
# mainn.RadioButton8.click_input()

def search_vehicle():
    pywinauto.mouse.click(coords=(45, 134))
    mainn.type_keys("123")
    mainn.type_keys("{ENTER}")




def exercise():
    # mainn.findbestmatch.find_best_control_matches('首页','RadioButton')
    # mainn.findbestmatch.find_best_match('热力图',1,limit_ratio = 0.5)
    one.findwindows.enum_windows()

if __name__ == '__main__':
    login()
    search_vehicle()
    # exercise()
    # check_vehicle()
    # click_homepage()
    # add_rectangle()































































































# one['记事本'].print_control_identifiers()
# # 取到编辑窗口
# edit = one['无标题 - 记事本']['Edit']
# # 对编辑窗口进行输入内容
# edit.type_keys("柠檬班")
# # 快捷键操作
# send_keys("^a")
# send_keys("^c")
# send_keys("^v")
# send_keys("{VK_RETURN}")
# send_keys("^v")