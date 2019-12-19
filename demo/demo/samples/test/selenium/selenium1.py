#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
# date:2019/12/18
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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import os

# os.environ["webdriver.chrome.driver"] = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("https://www.baidu.com")
try:
    element = driver.find_element_by_id('kw')
    element.send_keys("Selenium automation")  # 发送内容
    time.sleep(1)
    element.send_keys(Keys.CONTROL + 'a')
    element.send_keys(Keys.BACKSPACE)

    # ActionChains下相关方法在当前的firefox不工作，这个是一个已知的bug。
    element = driver.find_element_by_xpath("//*[@id='lg']/img")
    actionChains = ActionChains(driver)
    actionChains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    driver.find_element_by_link_text("新闻").click()
    print('test pass: element found by link text')
    print(driver.get_window_size())

    driver.set_window_size(1280, 800)  # 分辨率 1280*800
    time.sleep(1)
    print(driver.get_window_size())

    driver.set_window_size(1024, 768)  # 分辨率 1024*768
    time.sleep(1)

    # 方法二
    if u"百度一下，你就知道" == driver.title:
        print('Assertion test pass.')
    else:
        print('Assertion test fail.')
except Exception as e:
    print("Exception found", format(e))

for link in driver.find_elements_by_xpath("//*[@href]"):
    print(link.get_attribute('href'))
# 断言方法二，本文重点介绍方法 https://www.cnblogs.com/du-hong/p/11956076.html
# error_mes = driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_10__error']").text
# try:
#     assert error_mes == u'请您输入手机/邮箱/用户名'
#     print('Test pass.')
# except Exception as e:
#     print("Test fail.", format(e))


# 登录腾讯课堂页面
driver.get('https://ke.qq.com/course/list')

# 点击首页登录
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//a[@id="js_login"]')))
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


def get_size(driver):
    """
    获取窗口尺寸并打印

    """
    size = driver.get_window_size()  # 获取窗口尺寸
    print(size)  # 打印窗口尺寸
    time.sleep(3)  # 暂停3秒


driver.get("https://www.baidu.com")  # 打开网页
get_size(driver)
driver.set_window_size(800, 600)  # 设置窗口尺寸为800*600
get_size(driver)
driver.minimize_window()  # 窗口最小化，窗口尺寸未发生变化
get_size(driver)
driver.maximize_window()  # 窗口最大化
get_size(driver)

driver.get_screenshot_as_file("D:\\screenshot.png")  # 截图

# 进行后退、前进操作
driver.back()  # 后退
time.sleep(3)
driver.forward()  # 前进
time.sleep(3)

# 对网页进行刷新
driver.refresh()

driver.quit()  # 停止进程
