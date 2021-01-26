#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#coding=utf-8
# # https://blog.csdn.net/oJiuJieZhong/article/details/113060387?utm_medium=distribute.pc_category.none-task-blog-hot-11.nonecase&depth_1-utm_source=distribute.pc_category.none-task-blog-hot-11.nonecase&request_id=
# Python实现京东抢秒杀
from selenium import webdriver  # 导入火狐浏览器的驱动
import time
import datetime
from os import path

d = path.dirname(__file__)
abspath = path.abspath(d)

webdriver = webdriver.Chrome() #Firefox()     # 打开一个火狐浏览器
webdriver.maximize_window()


def login():
    webdriver.get("https://cart.jd.com/cart_index")  # 此为购物车网站
    time.sleep(3)
    webdriver.find_element_by_id("cartEmptyGologinBtn").click()   # 一般需要登录，此处点击的是去登录按钮
    time.sleep(15)  # 为了避免输入校验码绕过了输入登录账户密码的步骤，此处打开的是二维码页面
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))

def buy(buytime):
  while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
  # 对比时间，时间到的话就点击结算
    if now >= buytime:
     try:
        # 点击结算按钮
        if webdriver.find_element_by_name("select-all"):
            webdriver.find_element_by_name("select-all").click()
        if webdriver.find_element_by_class_name("common-submit-btn"):
            webdriver.find_element_by_class_name("common-submit-btn").click()
        webdriver.find_element_by_link_text("知道了").click()
     except:
      # time.sleep(0.2)
      # print(now)
      # time.sleep(0.1)
      pass
      try:
        webdriver.find_element_by_id('order-submit').click()
        time.sleep(0.05)
      except:
        pass
if __name__ == "__main__":
  # times = input("请输入抢购时间：")
  # 时间格式："2018-09-06 11:20:00.000000"
  login()
  buy("2021-01-23 00:00:00.000000")
