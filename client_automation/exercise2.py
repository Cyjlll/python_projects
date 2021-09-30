from pywinauto.application import Application
from pywinauto import application
import autoit
import time
import pywinauto
from pywinauto.keyboard import send_keys
import requests
import unittest
import requests
# url="http://192.168.168.9:8080/"
# req=requests.get(url)
# print(req.text)



# class Test(unittest.TestCase):
#     try:
#         def test01(self):
#             '''判断 a == b '''
#             a = 1
#             b = 2
#             self.assertEqual(a,b)
#
#         def test02(self):
#             '''判断 a in b '''
#             a = "a"
#             b = "ab"
#             self.assertIn(a,b)
#
#         def test04(self):
#             '''失败案例'''
#             a = "上海-悠悠"
#             b = "yoyo"
#             self.assertEqual(a,b)
#
#         def test03(self):
#             '''判断 a is True '''
#             a = False
#             self.assertTrue(a)
#
#     except Exception as e:
#         print(e)
#
#
# if __name__ == "__main__":
#     unittest.main()

respones=requests.post('http://192.168.168.9:8080/LoginAction_loginMobile.action?update=gViewerAndroid&server=login&userAccount=1322&password=1000000&languages=cn')
print(respones.text)


{"result":2}
