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

# oldWb = xlrd.open_workbook(r"D:\python项目\other_projects\first.xls",'w+b')
# #先打开已存在的表
# newWb = copy(oldWb)
# #复制
# newWs = newWb.get_sheet(1)
# #取sheet表
# newWs.write(2,6, label = 'diyige')
# #下标从零开始，写入第六列第二行写入内容
# newWb.save("D:\python项目\other_projects\end.xls")
#保存至result路径

# # 创建一个workbook 设置编码
# workbook = xlwt.Workbook(encoding = 'utf-8')
# # 创建一个worksheet
# worksheet = workbook.add_sheet('My Worksheet')
#
# # 写入excel
# # 参数对应 行, 列, 值
# worksheet.write(1,1, label = 'this is test')
#
# # 保存
# workbook.save('Excel_test2.xls')

#import xlutils;

from xlutils.copy import copy

styleBoldRed = xlwt.easyxf('font: color-index red, bold on')

headerStyle = styleBoldRed

wb = xlwt.Workbook()

ws = wb.add_sheet(gConst['xls']['sheetName'])

ws.write(0, 0, "Header", headerStyle)

ws.write(0, 1, "CatalogNumber", headerStyle)

ws.write(0, 2, "PartNumber", headerStyle)

wb.save(gConst['xls']['fileName'])

#open existed xls file

#newWb = xlutils.copy(gConst['xls']['fileName']);

#newWb = copy(gConst['xls']['fileName']);

oldWb = xlrd.open_workbook(gConst['xls']['fileName'], formatting_info=True)

# print oldWb; #

newWb = copy(oldWb)

# print newWb; #

newWs = newWb.get_sheet(0)

newWs.write(1, 0, "value1")
newWs.write(1, 1, "value2")

newWs.write(1, 2, "value3")

print("write new values ok")

newWb.save(gConst['xls']['fileName'])

print("save with same name ok")