# _*_ coding: UTF-8 _*_
# @Time : 2021/9/28 20:25
# @Author : caoyujie
# @Site : 
# @File : app_login_page.py
# @Software : PyCharm


import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class Login():
    # 设置固定参数
    def __init__(self,driver):
        self.driver=driver
        self.url=('http://192.168.168.9:8080/LoginAction_loginMobile.action?update=gViewerAndroid&server=login&userAccount=1322&password=000000&languages=cn')
        self.username=(By.ID,'com.icarvisions.iCarView:id/login_editview_account')
        self.passwd=(By.ID,'com.icarvisions.iCarView:id/login_edittext_pwd')
        self.server=(By.ID,'com.icarvisions.iCarView:id/login_edittext_server')
        self.btn=(By.ID,'com.icarvisions.iCarView:id/lyLogin_tvSave')
        self.wait=WebDriverWait(self.driver,30,0.5)

        self.device_info={}
        self.device_info['platformName']='Android'#系统名称
        self.device_info['platformVersion']='5.1.1'#系统版本号
        self.device_info['appPackage']='com.icarvisions.iCarView'#app包名
        self.device_info['appActivity']='net.babelstar.cmsv6.view.LoginActivity'#app入口的activity
        self.device_info['deviceName']='Android Emulator'#设备名称

    def open(self):
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.device_info)
    # 输入用户名
    def putin_username(self,uname):
         try:
             # 设置等待时间，直到用户名框出现
             self.wait.until(expected_conditions.visibility_of_element_located(self.username))
             # 输入用户名，解元组
             self.driver.find_element(*self.username).send_keys(uname)
         except:
             raise Exception('用户名异常')
    # 输入密码
    def putin_passwd(self,pwd):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.passwd))
            self.driver.find_element(*self.passwd).send.keys(pwd)
        except:
            raise Exception('密码异常')
    # 输入服务器
    def putin_server(self,server_port):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.server))
            self.driver.find_element(*self.server).send.keys(server_port)
        except:
            raise Exception('服务器异常')

    # 点击登陆
    def login_btn(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located(self.btn))
            self.driver.find_element(*self.btn).click()
        except:
            raise Exception('登陆按钮异常')



if __name__=='__main__':
    testCase=Login(webdriver.Chrome())
    testCase.open()
    testCase.putin_username('1322')
    testCase.putin_passwd('000000')
    testCase.putin_server('192.168.168.9:8080')
    testCase.login_btn()




