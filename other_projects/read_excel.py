# _*_ coding: UTF-8 _*_
# @Time : 2021/4/30 11:26
# @Author : caoyujie
# @Site : 
# @File : read_excel.py
# @Software : PyCharm


import xlrd
import xlwt
from datetime import date,datetime

file1 = '12'
arr=[]
arr1=[]

def read_excel():
    wb = xlrd.open_workbook('123.xls')#打开文件
    # print(wb.sheet_names())#获取所有表格名字
    sheet1 = wb.sheet_by_index(0)#通过索引获取第几个表格
    # sheet2 = wb.sheet_by_name('年级')#通过名字获取表格
    # print(sheet1)
    # print(sheet1.ncols)
    rows = sheet1.row_values(2)#获取行内容
    cols = sheet1.col_values(3)#获取列内容
    for i in range(0,sheet1.nrows):
        # 把每一列的内容加入数组
        arr.append(sheet1.row_values(i))
        # print(sheet1.col_values(i))
        # print(cols)
        # print(sheet1.cell(1,0).value)
    print(arr)
    # for a in arr:
        # result=','.join(a)
        # print(a)
        # for j in a:
        #     arr1.append(j)
    # print(arr1)
    # result=','.join(arr1)
    # print(result)

yujie=[]
def cao():
    # 首先打开这个文件
    excell=xlrd.open_workbook('six.xls')
    # 选取这个文件的第一张表
    one=excell.sheet_by_index(0)
    # print(one.nrows)
    # print(one.ncols)
    # print(one.row_values(1))
    # 从0到总共的行数循环
    for j in range(34,one.ncols):
        for k in one.col_values(j):
            yujie.append(k)
    print(yujie)

a_line=[]
finallyy=[]
def meiyihang(filename):
    content=xlrd.open_workbook(filename)
    first=content.sheet_by_index(0)
    for i in range(5,first.nrows):
        for k in first.row_values(i):
            pass


if __name__ == '__main__':
    # cao()
    read_excel()
    # meiyihang('six.xls')
