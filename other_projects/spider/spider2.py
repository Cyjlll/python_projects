# _*_ coding: UTF-8 _*_
# @Time : 2021/5/7 15:39
# @Author : caoyujie
# @Site : 
# @File : spider2.py
# @Software : PyCharm



from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配`
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作


response=urllib.request('http://www.zhihu.com')
html=response.read()
print(html)