#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo - 当前Project名称;
# selenium2_framealert - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2019/12/1821:53 - 当前系统日期;
# 554961776@qq.com

# 3.导入模块
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
# 步骤：https://www.cnblogs.com/du-hong/p/11982646.html
#
# 1.先确认你要操作的元素，是否存在与iframe中，如果元素在iframe中就需要切换
#
# 2.找到该iframe
#
# 3.切换到该iframe （两种方式）
#
#    第一种方式：有三种方法，只是单纯的切换
#    driver.switch_to.frame(1) #通过index（下标）
#    driver.switch_to.frame('login_frame_qq') #通过name
#    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="login_frame_qq"]')) #通过webelement
#
#    第两种方式：既等待元素可见又进行了iframe切换
#
#    WebDriverWait(driver,20).until(EC.frame_to_be_available_and_switch_to_it('login_frame_qq'))
#
# 4.切换完后，就以这个iframe中的html为主html
#
# 5.返回默认的html页面，无论现在在那一层的iframe，执行一次即可。
#    driver.switch_to.default_content()
# 登录腾讯课堂页面
driver.get('https://ke.qq.com/course/list')

cookies=driver.get_cookies()
print(type(cookies))
print(cookies)

# 点击首页登录
WebDriverWait(20, driver).until(EC.visibility_of_element_located((By.XPATH, '//a[@id="js_login"]')))
driver.find_element_by_id("js_login").click()

# 登录弹窗点击QQ登录
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(@class,"btns-enter-qq")]')))
driver.find_element_by_xpath('//a[contains(@class,"btns-enter-qq")]').click()

# iframe切换
# driver.switch_to.frame('login_frame_qq') #通过name
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name="login_frame_qq"]'))  # 通过webelement

# 弹窗点击账户密码登录switcher_plogin
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@id="switcher_plogin"]')))
time.sleep(10)
driver.find_element_by_xpath('//a[@id="switcher_plogin"]').click()


# ##
# 7.1 多个iframe的切换问题
# # 如：有两个iframe：f1、f2
# # 1.定位到f1
# driver.switch_to_frame("f1")
# # 2.操作元素
# # ······
# # 3.退出iframe
# driver.switch_to_default_content()
# # 4.定位到f2
# driver.switch_to_frame("f2")
# # ······
# 7.2 嵌套：f1中嵌套着f2
# driver.switch_to_frame("f1")
# driver.switch_to_frame("f2")
# # 操作元素
# 7.3 退出iframe：
# # 第一种方式：跳出所有iframe，回到主界面
# driver.switch_to_default_content()
#
# # 第二种方式：回到f1（返回上一级）
# driver.switch_to.parent_frame()