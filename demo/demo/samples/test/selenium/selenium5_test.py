#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo - 当前Project名称;
# selenium4_test - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2019/12/1822:12 - 当前系统日期;
# 554961776@qq.com


# 3.导入模块

import unittest
from selenium import webdriver
from time import sleep

'''
cnblog的登录测试，分下面几种情况：
(1)用户名、密码正确
(2)用户名正确、密码不正确
(3)用户名正确、密码为空
(4)用户名错误、密码正确
(5)用户名为空、密码正确（还有用户名和密码均为空时与此情况是一样的，这里就不单独测试了）
'''


class LoginCase(unittest.TestCase):

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()

    # 定义登录方法
    def login(self, username, password):
        self.dr.get('https://passport.cnblogs.com/user/signin')  # cnblog登录页面
        self.dr.find_element_by_id('LoginName').send_keys(username)
        self.dr.find_element_by_id('Password').send_keys(password)
        self.dr.find_element_by_id('submitBtn').click()

    def test_login_success(self):
        '''用户名、密码正确'''
        self.login('北京-宏哥', '!qaz2wsx')  # 正确用户名和密码
        sleep(3)
        link = self.dr.find_element_by_id('lnk_current_user')
        self.assertTrue('北京-宏哥' in link.text)  # 用assertTrue(x)方法来断言  bool(x) is True 登录成功后用户昵称在lnk_current_user里
        self.dr.get_screenshot_as_file("D:\\cnblogtest\\login_success.jpg")  # 截图  可自定义截图后的保存位置和图片命名

    def test_login_pwd_error(self):
        '''用户名正确、密码不正确'''
        self.login('北京-宏哥', 'kemi')  # 正确用户名，错误密码
        sleep(2)
        error_message = self.dr.find_element_by_class_name('ajax-error-box').text
        self.assertIn('用户名或密码错误', error_message)  # 用assertIn(a,b)方法来断言 a in b  '用户名或密码错误'在error_message里
        self.dr.get_screenshot_as_file("D:\\cnblogtest\\login_pwd_error.jpg")

    def test_login_pwd_null(self):
        '''用户名正确、密码为空'''
        self.login('北京-宏哥', '')  # 密码为空
        error_message = self.dr.find_element_by_id('Password-error').text
        self.assertEqual(error_message, '请输入密码')  # 用assertEqual(a,b)方法来断言  a == b  请输入密码等于error_message
        self.dr.get_screenshot_as_file("D:\\cnblogtest\\login_pwd_null.jpg")

    def test_login_user_error(self):
        '''用户名错误、密码正确'''
        self.login('北京-宏哥1', '!qaz2wsx')  # 密码正确，用户名错误
        sleep(2)
        error_message = self.dr.find_element_by_id('ajax-error-box').text
        self.assertIn('用户名或密码错误', error_message)  # 用assertIn(a,b)方法来断言 a in b
        self.dr.get_screenshot_as_file("D:\\cnblogtest\\login_user_error.jpg")

    def test_login_user_null(self):
        '''用户名为空、密码正确'''
        self.login('', '!qaz2wsx')  # 用户名为空，密码正确
        error_message = self.dr.find_element_by_id('LoginName-error').text
        self.assertEqual(error_message, '请输入登录用户名')  # 用assertEqual(a,b)方法来断言  a == b
        self.dr.get_screenshot_as_file("D:\\cnblogtest\\login_user_null.jpg")

    def tearDown(self):
        sleep(2)
        print('自动测试完毕！')
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()

#  　　上一篇介绍了自动化框架的架构，今天宏哥就带领小伙伴或者童鞋们开始开工往这个框架里开始添砖加瓦。主要是介绍一个框架unittest单元测试框架和一种设计思想POM。
#
# 2. unittest单元测试框架
# 前面文章已经简单介绍了一些关于自动化测试框架的介绍，知道了什么是自动化测试框架，主要有哪些特点，基本组成部分等。在继续介绍框架设计之前，我们先来学习一个工具，叫unittest。
#
#        unittest是一个单元测试框架，是Python编程的单元测试框架。有时候，也做叫做“PyUnit”,是Junit的Python语言版本。这里了解下,Junit是Java语言的单元测试框架，Java还有一个很好用的单元测试框架叫TestNG,本系列只学习Python，所以只需要unittest是
#
# Python里的一个单元测试框架就可以了。
#
#       unittest支持测试自动化，共享测试用例中的初始化和关闭退出代码，在unittest中最小单元是test，也就是一个测试用例。要了解unittest单元测试框架，先来了解以下几个重要的概念。
#
# 2.1 测试固件（test fixture）
#       一个测试固件包括两部分，执行测试代码之前的准备部分和测试结束之后的清扫代码。这两部分一般用函数setUp()和tearDown()表示。这里举例以下，例如要测试百度搜索selenium这个场景，我们的测试固件可以这样写，setUp()里写打开浏览器，浏览器最大
#
# 化，和打开百度首页等脚本代码；在tearDown（）里写结束搜索后，退出并关闭浏览器的代码。
#
# 2.2 测试用例（test case）
#        unittest中管理的最小单元是测试用例，一个测试用例，包括测试固件，和具体测试业务的函数或者方法。一个测试用例中，测试固件可以不写，但是至少有一个已test开头的函数。unittest会自动化识别test开头的函数是测试代码，如果你写的函数不是test开头，
#
# unittest是不会执行这个函数里面的脚本的，这个千万要记住，所有的测试函数都要test开头，记住是小写的哦。
#
# 2.3 测试套件 （test suite）
#        很简单，就是很多测试用例的集合，叫测试套件，一个测试套件可以随意管理多个测试用例。如果测试用例比作单个学生，测试套件就是好像是班级的概念。
#
# 2.4 测试执行器 （test runner）
#        test runner是一个用来执行加载测试用例，并执行用例，且提供测试输出的一个组建。test runner可以加载test case或者test suite进行执行测试任务。
#
# 我们举例来，练习一下test fixture和test case的使用，学习unittest的简单用法：
#
# 2.5 设计思路
# 1. 新建一个testbaidu.py的文件
#
# 2. 导入unittest模块
#
# 3. 当前测试类继承unittest.TestCase，相当于当前利用unittest创建了一个test case，这个test case是能够被unittest直接识别。
#
# 4. 写setUP(),主要是打开浏览器和打开站点
#
# 5. 写一个test_search（）用例写搜索的代码
#
# 6. 写tearDown(),主要是浏览器退出操作
#selenium6_test.py