#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install xlrd
#pip install xlwt

import xlrd#读取excel   https://www.cnblogs.com/ljy1227476113/p/11951430.html
import xlwt#写入excel
# import MySQLdb
import requests
import linecache
import random
from bs4 import BeautifulSoup

if __name__=="__main__":
    f = xlwt.Workbook(encoding='utf-8') #创建工作簿
    sheet1 = f.add_sheet(u'sheet1') #创建sheet
    row0 = [u'ID',u'name',u'tref',u'comment_num']
    #生成第一行
    for i in range(0,len(row0)):
        sheet1.write(0,i,row0[i])

    n=0#ID编号
    target='https://www.cnblogs.com/'#博客园首页
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    headers = {'User-Agent':user_agent}

    req=requests.get(url=target)
    html=req.text
    html=html.replace('<br>',' ').replace('<br/>',' ').replace('/>','>')
    bf=BeautifulSoup(html,"html.parser")
    texts=bf.find_all('div',class_='post_item_body')
    #texts_div=texts.find_all('div',class_='wz_content')
    for item in texts:
        n=n+1
        item_name=item.find('a').text#标题
        item_href=item.find('a')['href']#链接
        item_refer2=item.find('span',class_='article_comment').text#评论数
        print('{} {} {}\n'.format(item_name,item_href,item_refer2))
        mid=[n,item_name,item_href,item_refer2]
        for i in range(4):#写入excel
            sheet1.write(n,i,mid[i])
    print("Done!")
    f.save('demo1.xls') #保存文件

    book = xlrd.open_workbook("demo1.xls")#打开excel
    sheet = book.sheet_by_name("sheet1")
# #建立一个MySQL连接
#     database = MySQLdb.connect (host="localhost", user = "root", passwd = "111111", db = "mysql")
# # 获得游标对象, 用于逐行遍历数据库数据
#     cursor = database.cursor()
# # 创建插入SQL语句
#     query = """INSERT INTO mypython VALUES (%s, %s, %s, %s)"""
# # 创建一个for循环迭代读取xls文件每行数据的, 从第二行开始是要跳过标题
#     for r in range(1, sheet.nrows):
#         product      = sheet.cell(r,0).value
#         customer = sheet.cell(r,1).value.encode()#python3中string格式要encode()
#         rep          = sheet.cell(r,2).value.encode()
#         date     = sheet.cell(r,3).value.encode()
#
#         values = (0, customer, rep, date)
#       # 执行sql语句
#         cursor.execute(query, values)
# # 关闭游标
#     cursor.close()
# # 提交
#     database.commit()
# # 关闭数据库连接
#     database.close()
# 打印结果
    print("All Done! ")