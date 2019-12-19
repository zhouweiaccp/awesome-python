#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo - 当前Project名称;
# selenium6_test - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2019/12/1822:21 - 当前系统日期;
# 554961776@qq.com

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 主要是介绍一个框架unittest单元测试框架和一种设计思想POM。
# 解释：
# 最后结尾处的unittest.main(), 添加这个是支持在cmd，里面，cd到这个脚本文件所在的目录，然后python
# 脚本名.py执行，如果不添加这一段，是无法执行cmd里面运行脚本的，在PyCharm中，不添加最后一段，也可以通过，右键
# Run
# "unittest xxx"，来达到执行效果。
#
# 3.
# 什么是POM（Page
# Object
# Model）
# 　　前面我们介绍了Python中的单元测试框架unittest，以后我们所有的测试类文件，都采用unittest来辅助我们进行debug和脚本开发。搞定了debug机制和确定了unittest来进行创建和管理我们的自动化测试脚本，接下来我们来考虑下，框架设计中一种很普遍的设计
#
# 思想 - POM（Page
# Object
# Model）。
#
# 3.1
# POM是什么
# Page
# Object
# Model(POM)
# 直译为“页面对象模型”，这种设计模式旨在为每个待测试的页面创建一个页面对象(
#
#
# class )，将那些繁琐的定位操作封装到这个页面对象中，只对外提供必要的操作接口。
#
# 3.2 POM 有什么好处
# POM 将页面定位和业务操作分开，分离了测试对象和测试脚本，如果UI更改页面，测试脚本不需要更改，只需要更改页面对象中的某些代码就可以，提高了可维护性。
#
# POM，中文字母意思是，页面对象模型，POM是一种最近几年非常流行的自动化测试模型，或者思想，POM不是一个框架，就是一个解决问题的思想。采用POM的目的，是为了解决前端中UI变化频繁，从而造成测试自动化脚本维护的成本越来越大。下图，形
#
# 象描述了POM的好处。
#
#
#
# 从上图看出，采取了POM设计思路和不采取的区别，左侧把测试代码和页面元素都写在一个类文件，如果需要更改页面，那么就要修改页面元素定位，从而要修改这个类中测试代码，这个看起来和混乱。右侧，采取POM后，主要的区别就是，把页面元素和业务
#
# 逻辑和测试脚本分离出来到两个不同类文件。ClassA只写页面元素定位，和业务逻辑代码操作的封装，ClassB只写测试脚本，不关心如何元素定位，只写调用ClassA的代码去覆盖不同的测试场景。如果前端页面发生变化，只需要修改ClassA的元素定位，而不需要去
#
# 修改ClassB中的测试脚本代码。
#
# POM主要有以下优点：
#
# 1. 把web ui对象仓库从测试脚本分离，业务代码和测试脚本分离。
#
# 2. 每一个页面对应一个页面类，页面的元素写到这个页面类中。
#
# 3. 页面类主要包括该页面的元素定位，和和这些元素相关的业务操作代码封装的方法。
#
# 4. 代码复用，从而减少测试脚本代码量。
#
# 5. 层次清晰，同时支持多个编写自动化脚本开发，例如每个人写哪几个页面，不影响他人。
#
# 6. 建议页面类和业务逻辑方法都给一个有意义的名称，方便他人快速编写脚本和维护脚本。
#
# 3.3 牛刀小试
# 比如测试一个登陆页面：新浪微博 ，执行测试的人员传递不同的数据到帐号、密码框就可以了，而不应该去顾虑：页面是否已经加载完成？怎样定位到帐号输入框？怎样定位到登陆按钮等等问题。
#
# 这些问题全部交由登陆页面的“页面对象”去解决并封装起来，只提供给测试人员三个接口方法：1.帐号输入接口、2.密码输入接口、3.提交接口。
#
# 首先定义一个基本页面 BasePage类 ，定义基本的页面操作，提供给其他页面去继承，basePage.py 内容如下：
# https://www.cnblogs.com/du-hong/p/12058673.html
class BaiduSearch(unittest.TestCase):

    def setUp(self):
        """
        测试固件的setUp()的代码，主要是测试的前提准备工作
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://www.baidu.com")

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭浏览器
        :return:
        """
        self.driver.implicitly_wait(8)
        self.driver.quit()

    def test_baidu_search(self):
        """
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
        :return:
        """
        self.driver.find_element_by_id('kw').send_keys('selenium')
        time.sleep(1)
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        try:
            assert 'selenium' in self.driver.title
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))


#
# if __name__ == '__main__':
#     unittest.main()


class BasePage(object):
    """
     基础页面，提供给其他页面继承
     """

    def __init__(self, driver, base_url, title):
        """
       初始化
       """
        self.driver = driver
        self.base_url = base_url
        self.title = title

    def _open(self, url):
        """
        私有方法，打开url参数指定的页面,
        并检查打开是否正确
        """
        self.driver.get(url)
        # 显式等待10秒，如果打开页title与预期不符或者超时，抛出异常
        WebDriverWait(self.driver, 10).until(EC.title_is(self.title))

    def open(self):
        """
        公共方法，调用私有方法_open()打开链接
        """
        self._open(self.base_url)

    def find_element(self, *loc):
        """
        定位指定元素
        """
        # 显式等待元素，超过10秒未找到则抛出超时异常(TimeoutException)
        # presence_of_element_located： 不关心元素是否可见，只关心元素是否存在在页面中
        # visibility_of_element_located： 不仅找到元素，并且该元素必须可见
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(loc))
        return self.driver.find_element(*loc)


class LoginPage(BasePage):
    """
    新浪微薄登陆页面
    继承自基础页面BasePage
   """
    # 定位帐号输入框
    username_loc = (By.ID, 'loginname')
    # 定位密码输入框
    password_loc = (By.NAME, 'password')
    # 定位登陆按钮
    submit_loc = (By.XPATH, './/*[@id="pl_login_form"]/div/div[3]/div[6]/a')
    # 定位提示信息，如：请输入验证码
    # 不要迷信开发者工具提供的Xpath，
    # 比如这里提供的Xpath：//*[@id="layer_15582553868501"]/div/p/span[2]，
    # id是动态的，无法使用，需自行推到Xpath
    message_loc = (By.XPATH, '//div[@class="content layer_mini_info"]/p/span[2]')

    # 输入用户名操作
    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    # 输入密码操作
    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    # 点击登陆按钮操作
    def submit(self):
        self.find_element(*self.submit_loc).click()

    # 获取提示信息
    def get_message(self):
        return self.find_element(*self.message_loc).text


if __name__ == '__main__':  # 测试登陆
    # 预打开页面
    base_url = 'https://weibo.com/'
    # 页面title
    title = '微博-随时随地发现新鲜事'
    # 准备好待输入的用户名和密码
    username = 'haha'
    password = 'hehe'

    # 打开Chrome浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 登陆页面初始化
    login = LoginPage(driver, base_url, title)
    # 打开新浪微博页
    login.open()
    # 输入用户名
    login.type_username(username)
    # 输入密码
    login.type_password(password)
    # 点击登陆
    login.submit()
    # 打印提示信息
    print(login.get_message())

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     page = BasePage(driver, 'https://www.baidu.com/', '百度一下，你就知道')
#     page.open()
#     driver.quit()
