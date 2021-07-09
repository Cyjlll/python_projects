# _*_ coding: UTF-8 _*_
# @Time : 2021/5/14 17:42
# @Author : caoyujie
# @Site : 
# @File : jiekou.py
# @Software : PyCharm


import requests
import time
import unittest
# from data import test


def addstudent(self):
        data={
            'pageIndex':1,
            'pageSize':10
        }
        r=requests.post('http://192.168.168.9:8080/device/online.do',data=data)
        result=r.json()

