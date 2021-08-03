# _*_ coding: UTF-8 _*_
# @Time : 2021/4/30 11:26
# @Author : caoyujie
# @Site : 
# @File : read_excel.py
# @Software : PyCharm


import xlrd
import xlwt
from datetime import date,datetime
import pprint
import xlsxwriter
from xlutils.copy import copy

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
# 要读取的文件和里面总共有多少行
def meiyihang(filename,zonggong):
    content=xlrd.open_workbook(filename)
    first=content.sheet_by_index(0)
    # 从第5行到最后一行的遍历
    i=5
    while i<zonggong:
        a_line.append(first.row_values(i))
        # 从第33列到最后一列的遍历
        total=33
    # pprint.pprint(a_line)
        while total<=62:
            finallyy.append(first.row_values(i)[total])
            total=total+1
        i+=1
    # pprint.pprint(finallyy)
    last=[]
    for fen in range(0,int(len(finallyy)),30):
        c=finallyy[fen:fen+30]
        last.append(c)
    return last
    # print(last)
    # pprint.pprint(last)

# 计算有多少行
def pushin(arr,kaishi,jieshu):
    while kaishi<=jieshu:
        # print(kaishi)

        kaishi+=1

def putnumber():
    i=0
    yigongarr=[]
    nianjiaarr=[]
    peichanjiaarr=[]
    nianjia=0
    peichanjia=0
    linshi=meiyihang('six.xls',143)
    # 每一行
    # for i in linshi:
    #     for j in i:
    #         if "年假" in j:
    #             lianjia+=1
    #
    #         elif "陪产假" in j:
    #             peichanjia+=1
    #     lianjiaarr.append(lianjia)
    #     peichanjiaarr.append(peichanjia)
    #     lianjia=0
    #     peichanjia=0
    # print(lianjiaarr)

    while i<=143:
        # if '年产假' in linshi[i]:
        #     lianjia+=1
        # lianjiaarr.append(lianjia)
        # if '陪产假' in linshi[i]:
        #     peichanjia+=1
        # peichanjiaarr.append(peichanjia)
        nianjia=0
        peichanjia=0
        for neirong in linshi[i]:
            if "年假" in str(neirong):
                nianjia+=1
            if "陪产假" in str(neirong):
                peichanjia+=1

        nianjiaarr.append(nianjia)
        peichanjiaarr.append(peichanjia)
        i+=1
        yigongarr=[nianjiaarr,peichanjiaarr]

    print(yigongarr)







def writein(adss,adse):
    liangge=putnumber()
    oldWb = xlrd.open_workbook(adss)
    #先打开已存在的表
    newWb = copy(oldWb)
    #复制
    newWs = newWb.get_sheet(1)
    #取sheet表
    # 年假
    y=2
    x=6
    c=2
    j=7
    for i in liangge[0]:
        newWs.write(y,x, label = i)
        y+=1
        print(y)
    for j in liangge[1]:
        newWs.write(c,j, label = j)
        c+=1
        print(c)

    newWb.save(adse)
    #保存至result路径



if __name__ == '__main__':
    # cao()
    # read_excel()
    # 一共有多少行数
    meiyihang('six.xls',143)
    # pushin(meiyihang('six.xls'),3,140)
    putnumber()
    # writein()


