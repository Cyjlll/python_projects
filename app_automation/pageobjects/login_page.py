# _*_ coding: UTF-8 _*_
# @Time : 2021/10/10 14:50
# @Author : caoyujie
# @Site : 
# @File : login_page.py
# @Software : PyCharm
import unittest
import pprint
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver
import pprint
from selenium import webdriver
from selenium.webdriver.support.select import Select
from app_automation.base.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy



# 登陆页面
# 继承base页面里的方法
class LoginPage(BasePage):
    # 特有的一些元素定位
    user_name=(MobileBy.ID,'com.icarvisions.iCarView:id/login_editview_account')
    passwd=(MobileBy.ID,'com.icarvisions.iCarView:id/login_edittext_pwd')
    serverport=(MobileBy.ID,'com.icarvisions.iCarView:id/login_edittext_server')
    loginbutton=(MobileBy.ID,'com.icarvisions.iCarView:id/lyLogin_tvSave')

    def login(self,zhanghao,mima,fuwuqi):
        self.input(*self.user_name,zhanghao)
        self.input(*self.passwd,mima)
        self.input(*self.serverport,fuwuqi)
        self.click(*self.loginbutton)
        
