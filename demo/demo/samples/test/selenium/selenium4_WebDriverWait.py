#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo - 当前Project名称;
# selenium4_WebDriverWait - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2019/12/1822:05 - 当前系统日期;
# 554961776@qq.com


# 3.导入模块

# A. 使用前，先引用相关库
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()  # 打开Chrome浏览器
driver.get('https://www.baidu.com/')  # 打开百度
driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()  # 点击【登录】；click() 方法，可模拟在按钮上的一次鼠标单击。
# B. 确定元素的定位表达式
ele_locator = "TANGRAM__PSP_10__footerULoginBtn"  # 通过id,确定‘用户名登录’元素

# C.  使用expected_conditions对应的方法来生成判断条件
# EC.方法名(定位方式,定位表达式)
# EC.visibility_of_element_located(By.ID,ele_locator)#元素可见

# D.  调用WebDriverWait类设置等待总时长、轮询周期
# WebDriverWait(driver, 超时时长, 调用频率（默认0.5s）).until(可执行方法, 超时时返回的信息)
# 等待10秒钟，每隔1秒去查看对应的元素是否可见；如果可见，继续下一步操作；如果不可见，则继续等待，直到10s结束，如果元素还是不可见，则抛出超时异常
WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((By.ID, ele_locator)))

driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()  # 点击【用户名登录】

time.sleep(2)
driver.get('https://www.baidu.com/')
time.sleep(3)
# 折腾半天才发现定位出来的不是下拉框……
driver.find_element(By.LINK_TEXT, '设置').click()
driver.find_element(By.LINK_TEXT, '搜索设置').click()
time.sleep(2)

sel = driver.find_element(By.XPATH, '//*[@id="nr"]')  # 定位下拉框
Select(sel).select_by_value('50')  # 通过value的值进行选定条目
driver.find_element(By.CLASS_NAME, 'prefpanelgo').click()
time.sleep(2)
driver.switch_to.alert.accept()  # 此处同意警告框提示内容
# time.sleep(2)
driver.close()  # 关闭当前窗口


# https://www.cnblogs.com/du-hong/p/12010213.html
# driver.implicitly_wait(30)#隐性等待,最长30s  不到，则它将以轮询的方式不断地判断元素是否被定位到。假设在第6秒定位到了元素则继续执行，若直到超出设置时长（10秒）还没有定位到元素，则抛出异常
# 2.3.显性等待 WebDriverWait
# WebDriverWait配合该类的until()和until_not()方法，根据条件灵活的等待
#
# 程序每隔xx秒看一眼，如果条件成立了，则执行下一步，否则继续等待，直到超过设置的最长时间，然后抛出TimeoutException。
#
# 显式等待是你在代码中定义等待一定条件发生后再进一步执行你的代码。
# A. 使用前，先引用相关库
# B. 确定元素的定位表达式
# C.  使用expected_conditions对应的方法来生成判断条件
# WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.ID,ele_locator)))
# WebDriverWait(driver,10,1).until(EC.visibility_of_element_located((By.XPATH,ele_locator))
# """
# title_is：判断当前页面的title是否等于预期
# title_contains：判断当前页面的title是否包含预期字符串
# presence_of_element_located：判断某个元素是否被加到了dom树里，并不代表该元素一定可见
# visibility_of_element_located：判断某个元素是否可见. 可见代表元素非隐藏，并且元素的宽和高都不等于0
# visibility_of：跟上面的方法做一样的事情，只是上面的方法要传入locator，这个方法直接传定位到的element就好了
# presence_of_all_elements_located：判断是否至少有1个元素存在于dom树中。举个例子，如果页面上有n个元素的class都是'column-md-3'，那么只要有1个元素存在，这个方法就返回True
# text_to_be_present_in_element：判断某个元素中的text是否 包含 了预期的字符串
# text_to_be_present_in_element_value：判断某个元素中的value属性是否包含了预期的字符串
# frame_to_be_available_and_switch_to_it：判断该frame是否可以switch进去，如果可以的话，返回True并且switch进去，否则返回False
# invisibility_of_element_located：判断某个元素中是否不存在于dom树或不可见
# element_to_be_clickable - it is Displayed and Enabled：判断某个元素中是否可见并且是enable的，这样的话才叫clickable
# staleness_of：等某个元素从dom树中移除，注意，这个方法也是返回True或False
# element_to_be_selected：判断某个元素是否被选中了,一般用在下拉列表
# element_located_to_be_selected
# element_selection_state_to_be：判断某个元素的选中状态是否符合预期
# element_located_selection_state_to_be：跟上面的方法作用一样，只是上面的方法传入定位到的element，而这个方法传入locator
# alert_is_present：判断页面上是否存在alert
# """