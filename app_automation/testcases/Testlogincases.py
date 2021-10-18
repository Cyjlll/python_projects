# _*_ coding: UTF-8 _*_
# @Time : 2021/10/11 19:44
# @Author : caoyujie
# @Site : 
# @File : test_cases.py
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
from app_automation.pageobjects.login_page import LoginPage
import pytest

class Test_class(object):

    # 先导入这个页面的类，然后再实例化
    def test_oen(self):
        device_info={
            "platformName":"Android",    #系统名称
            "platformVersion":"5.1.1",     #系统版本号
            "appPackage" : "com.icarvisions.iCarView",    #app包名
            "appActivity":"net.babelstar.cmsv6.view.LoginActivity",#app入口的activity
            "automationName": "UIAutomator1",
            "deviceName":"Android Emulator"#设备名称
        }
        driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',device_info)
        login_page=LoginPage(driver=driver)
        login_page.login("YJ","aaa123@@","47.119.170.216:8080")

if __name__ == '__main__':
    pytest.main()