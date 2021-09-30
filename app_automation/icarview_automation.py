# _*_ coding: UTF-8 _*_
# @Time : 2021/8/24 19:21
# @Author : caoyujie
# @Site : 
# @File : icarview_automation.py
# @Software : PyCharm

from appium import webdriver
import time
import unittest
from appium.webdriver.common.touch_action import TouchAction

class ShouYe(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        pass
    def setUp(self) -> None:
        device_info={}
        device_info['platformName']='Android'#系统名称
        device_info['platformVersion']='5.1.1'#系统版本号
        device_info['appPackage']='com.icarvisions.iCarView'#app包名
        device_info['appActivity']='net.babelstar.cmsv6.view.LoginActivity'#app入口的activity
        device_info['deviceName']='Android Emulator'#设备名称


        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',device_info)
    def test1(self):
        time.sleep(3)
        self.driver.find_element_by_id('com.icarvisions.iCarView:id/login_editview_account').send_keys('1322')
        self.driver.find_element_by_id('com.icarvisions.iCarView:id/login_edittext_pwd').send_keys('000000')
        self.driver.find_element_by_id('com.icarvisions.iCarView:id/login_edittext_server').send_keys('192.168.168.9:8080')
        self.driver.find_element_by_id('com.icarvisions.iCarView:id/lyLogin_tvSave').click()
        time.sleep(6)
    def TearDown(self):
        self.driver.quit()
    @classmethod
    def tearDownClass(cls) -> None:
        pass
