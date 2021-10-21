# _*_ coding: UTF-8 _*_
# @Time : 2021/10/21 19:25
# @Author : caoyujie
# @Site : 
# @File : excel_openpyxl.py
# @Software : PyCharm


import openpyxl

excel=openpyxl.load_workbook('../other_projects/openpyxll.xlsx')

for i in excel.sheetnames:
    # excel[i]只是一个对象
    for j in excel[i].values:
        # 每一行的内容
        if type(j[0]) is int:
            print(j)


