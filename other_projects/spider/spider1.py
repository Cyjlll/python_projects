# _*_ coding: UTF-8 _*_
# @Time : 2021/4/19 20:20
# @Author : caoyujie
# @Site : 
# @File : spider1.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import urllib
import requests
import json
import xlwt
import xlrd
import re

# url='http://top.baidu.com/'
# param='fr=mhd_card'
# r=requests.get(url,params=param)
# print(r)
# print(r.text)



html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""




# soup = BeautifulSoup(html_doc, 'html.parser')
# a = soup.find('p',class_="tittle")
# print(a)

header="""
<div data-v-f499b276="" 
class="tab"><!----> <div data-v-f499b276="" class="tab-item"><div data-v-f499b276="" class="ivu-tooltip"><div class="ivu-tooltip-rel"><div data-v-f499b276="" 
class="tab-link"><div data-v-f499b276="" class="tab-img tab-17"></div> <span data-v-f499b276="" title="大数据分析" class="tab-title">大数据分析</span></div> </div> 
<div class="ivu-tooltip-popper ivu-tooltip-dark" style="display: none; position: absolute; will-change: top, left; top: 56px; left: 1182px;" x-placement="bottom">
<div class="ivu-tooltip-content"><div class="ivu-tooltip-arrow"></div> <div class="ivu-tooltip-inner ivu-tooltip-inner-with-width" style="max-width: 400px;">
<div data-v-f499b276=""><p data-v-f499b276="">首页</p> <p data-v-f499b276="">主动安全分析</p> <p data-v-f499b276="">固件首页</p> <p data-v-f499b276="">上下客分析</p>
</div></div></div></div></div></div> <!----> <!----> <!----> <!----> <div data-v-f499b276="" class="tab-item" style=""><div data-v-f499b276="" class="tab-link">
<div data-v-f499b276="" class="tab-img tab-5"></div> <span data-v-f499b276="" title="平台功能" class="tab-title">平台功能</span></div></div> <div data-v-f499b276="" 
class="tab-item"><div data-v-f499b276="" class="tab-link"><div data-v-f499b276="" class="tab-img tab-11"></div> <span data-v-f499b276="" title="主动安全" 
class="tab-title">主动安全</span></div></div> <div data-v-f499b276="" class="tab-item"><div data-v-f499b276="" class="tab-link"><div data-v-f499b276="" 
class="tab-img tab-6"></div> <span data-v-f499b276="" title="报表统计" class="tab-title">报表统计</span></div></div> <div data-v-f499b276="" class="tab-item">
<div data-v-f499b276="" class="tab-link"><div data-v-f499b276="" class="tab-img tab-12"></div> <span data-v-f499b276="" title="报警分析" class="tab-title">报警分析</span>
</div></div> <!----> <div data-v-f499b276="" class="tab-item router-link-exact-active router-link-active"><div data-v-f499b276="" class="tab-link">
<div data-v-f499b276="" class="tab-img tab-7"></div> <span data-v-f499b276="" title="系统管理" class="tab-title">系统管理</span></div></div> <!----> 
<div data-v-f499b276="" class="tab-item"><div data-v-f499b276="" class="tab-link"><div data-v-f499b276="" class="tab-img tab-8"></div> <span data-v-f499b276=""
 title="服务器管理" class="tab-title">服务器管理</span></div></div> <div data-v-f499b276="" class="tab-item" style="display: none;"><div data-v-f499b276="" 
 class="tab-link"><div data-v-f499b276="" class="tab-img tab-10"></div> <span data-v-f499b276="" title="系统配置" class="tab-title">系统配置</span></div></div> 
 <!----> <!----></div>"""
lalala = BeautifulSoup(header, 'html.parser')
# .findAll('span',attrs={'class':'tab-title'})
span=lalala.findAll('div',attrs={'class':'tab-link'})

for item in span:
    print(item)


