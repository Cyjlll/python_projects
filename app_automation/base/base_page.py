# _*_ coding: UTF-8 _*_
# @Time : 2021/10/6 19:16
# @Author : caoyujie
# @Site :
# @File : base_page.py
# @Software : PyCharm
import unittest
import pprint
from selenium import webdriver
from appium import webdriver
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
from appium.webdriver.common.mobileby import MobileBy



class BasePage:
    pass
    device_info={}
    device_info['platformName']='Android'#系统名称
    device_info['platformVersion']='5.1.1'#系统版本号
    device_info['appPackage']='com.icarvisions.iCarView'#app包名
    device_info['appActivity']='net.babelstar.cmsv6.view.LoginActivity'#app入口的activity
    device_info['deviceName']='Android Emulator'#设备名称
    driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',device_info)


# 每次使用这个类时都会使用到这个构造函数
    def __init__(self,driver):
        self.driver=driver

# 封装定位方法
    def locator(self,loc):
        # 解元组
        return self.driver.find_element(*loc)
    # 输入方法
    def input(self,loc,value):
        self.locator(loc).send_keys(value)
#     点击方法
    def click(self,loc):
        self.locator(loc).click()

