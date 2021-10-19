# _*_ coding: UTF-8 _*_
# @Time : 2021/9/28 17:45
# @Author : caoyujie
# @Site : 
# @File : login.py
# @Software : PyCharm


from appium import webdriver
import time
import unittest
from appium.webdriver.common.touch_action import TouchAction
import requests


class login(unittest.TestCase):
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
        respones=requests.post('http://192.168.168.9:8080/LoginAction_loginMobile.action?update=gViewerAndroid&server=login&userAccount=1322&password=000000&languages=cn')
        # self.assertNotEqual(respones.text,'{"result":2}')
        print(respones.text)
        print(respones.status_code)
        # time.sleep(6)

    def test2(self):
        pass
    def tearDown(self) -> None:
        print('测试完成')
        self.driver.quit()
    @classmethod
    def tearDownClass(cls) -> None:
        print('所有测试完成')

if __name__=="__main__":
    unittest.main()