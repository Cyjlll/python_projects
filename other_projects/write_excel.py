# _*_ coding: UTF-8 _*_
# @Time : 2021/7/15 20:16
# @Author : caoyujie
# @Site : 
# @File : write_excel.py
# @Software : PyCharm

import xlsxwriter

# encoding=gbk
import xlsxwriter
import xlwt
import xlrd
from xlutils.copy import copy

oldWb = xlrd.open_workbook(r"D:\python项目\other_projects\five.xls",'w+b')
#先打开已存在的表
newWb = copy(oldWb)
#复制
newWs = newWb.get_sheet(1)
#取sheet表
newWs.write(3, 5, "pass")
#写入 2行4列写入pass
newWb.save(r"D:\python项目\other_projects\five.xls")
#保存至result路径