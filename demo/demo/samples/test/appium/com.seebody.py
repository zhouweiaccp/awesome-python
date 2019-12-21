#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo - 当前Project名称;
# com.seebody.py - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2019/12/2021:47 - 当前系统日期;
# 554961776@qq.com

# 3.导入模块 https://www.cnblogs.com/du-hong/p/10997307.html
# nox_adb.exe connect 127.0.0.1:62001
# adb devices
# aapt dump badging D:\1\Download\zhangtongjiayuan_381.apk
# C:\Users\chive\AppData\Local\Android\Sdk\tools\bin
# 测试没有成功，报错如下，怀疑设备名
# > info: [debug] Getting connected devices...
# > info: [debug] executing cmd: C:\Users\chive\AppData\Local\Android\Sdk\platform-tools\adb.exe devices
# > info: [debug] 1 device(s) connected
# > info: Found device 127.0.0.1:62001
# > info: [debug] Setting device id to 127.0.0.1:62001
# > info: [debug] Waiting for device to be ready and to respond to shell commands (timeout = 5)
# > info: [debug] executing cmd: C:\Users\chive\AppData\Local\Android\Sdk\platform-tools\adb.exe -s 127.0.0.1:62001 wait-for-device
# > info: [debug] executing cmd: C:\Users\chive\AppData\Local\Android\Sdk\platform-tools\adb.exe -s 127.0.0.1:62001 shell "echo 'ready'"
# > info: [debug] Starting logcat capture
# > info: [debug] Getting device API level
# > info: [debug] executing cmd: C:\Users\chive\AppData\Local\Android\Sdk\platform-tools\adb.exe -s 127.0.0.1:62001 shell "getprop

from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'  # android的apk还是IOS的ipa
desired_caps['platformVersion'] = '6.0'  # android系统的版本号
desired_caps['deviceName'] = '127.0.0.1:62001'  # 手机设备名称，通过adb devices  查看
desired_caps['appPackage'] = 'com.seebady'  # apk的包名
desired_caps['appActivity'] = 'com.seebaby.login.ui.activity.LauncherActivity'  # apk的launcherActivity
# desired_caps['unicodeKeyboard'] = True   #使用unicodeKeyboard的编码方式来发送字符串
# desired_caps['resetKeyboard'] = True   #将键盘给隐藏起来
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)  # 启动服务器地址，后面跟的是手机信息
# 休眠五秒等待页面加载完成
time.sleep(60*2)

driver.find_element_by_id("com.seebaby:id/et_account").click()
driver.find_element_by_id("com.seebaby:id/et_account").clear()
driver.find_element_by_id("com.seebaby:id/et_account").send_keys('18251167280')
time.sleep(4)

# driver.quit()
#
# aapt
# dump
# badging
# D:\XXX.apk
# 获取安装包的所有信息
#
# adb
# devices（查看手机是否连接到电脑）
#
# adb
# shell
# pm
# list
# packages：列出所有的包名，找到所查看包的包名。
#
# adb
# shell
# dumpsys
# package
# com.android.XXX：查看某个包的具体信息
#
# 其它：
#
# adb
# devices：查看Android设备是否连接到电脑。
#
# adb
# shell
# dumpsys
# activity：查看当前运行的是哪个activity, 运行的一些进程等
#
# adb
# shell
# dumpsys
# activity
# activities
#
# adb
# shell
# pm
# list
# packages：列出所有的包名。
#
# adb
# shell
# dumpsys
# package：列出所有的安装应用的信息
#
# adb
# shell
# dumpsys
# package
# com.android.XXX：查看某个包的具体信息
#
# adb
# shell
# dumpsys
# activity | grep
# mFocusedActivity：查看当前resume的是哪个activity
#
# adb
# logcat | grep
# ActivityManager：查看当前正在运行的Activity
#
# adb
# logcat | grep
# Displayed：查看当前正在运行的Activity