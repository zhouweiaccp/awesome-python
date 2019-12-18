#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
#date:2019/12/18
__author__ = 'xxx'
# 0 安装chrome浏览器 77.0.3865.120 (正式版本) （32 位） (cohort: Stable)
# 1 https://cdn.npm.taobao.org/dist/chromedriver/2.43/chromedriver_win32.zip  解压到 C:\Program Files (x86)\Google\Chrome\Application  E:\programdata\python\Scripts
# 2.python -m pip install selenium

# 3.导入模块
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# os.environ["webdriver.chrome.driver"] = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome()
driver.maximize_window()

# 登录腾讯课堂页面
driver.get('https://ke.qq.com/course/list')

# 点击首页登录
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@id="js_login"]')))
driver.find_element_by_id("js_login").click()

# 登录弹窗点击QQ登录
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(@class,"btns-enter-qq")]')))
driver.find_element_by_xpath('//a[contains(@class,"btns-enter-qq")]').click()

# iframe切换
# driver.switch_to.frame('login_frame_qq') #通过name
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="login_frame_qq"]')) #通过webelement

# 弹窗点击账户密码登录switcher_plogin
#WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@id="switcher_plogin"]')))
time.sleep(10)
driver.find_element_by_xpath('//a[@id="switcher_plogin"]').click()