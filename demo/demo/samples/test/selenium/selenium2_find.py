#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo - 当前Project名称;
# selenium2_find - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2019/12/1820:45 - 当前系统日期;
# 554961776@qq.com
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 打开一个网页
driver.get("https://www.zhihu.com/")


time.sleep(2)
ele = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/div/form/div[2]/div[2]/label/input')
#'//*[@id="root"]/div/main/div/div/div[1]/div/form/div[2]/div[2]/label/input')
print(ele)

ele.click()
driver.back()

# 查找多个元素的方法
eles = driver.find_elements_by_class_name("Feed")

print(eles)
print(len(eles))

time.sleep(5)
eles = driver.find_elements(By.CLASS_NAME, 'Feed')
# XPATH = "xpath"
# LINK_TEXT = "link text"
# PARTIAL_LINK_TEXT = "partial link text"
# NAME = "name"
# TAG_NAME = "tag name"
# CLASS_NAME = "class name"
# CSS_SELECTOR = "css selector"

print(eles)
print(len(eles))

driver.quit()
# 5.定位大法 https://www.cnblogs.com/du-hong/p/11933299.html
# webdriver 提供了八种元素定位方法：
#
# id
# name
# class name
# tag name
# link text
# partial link text
# xpath
# css selector
# 在 Python 语言中对应的定位方法如下：
# find_element_by_id()
# find_element_by_name()
# find_element_by_class_name()
# find_element_by_tag_name()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_xpath()
# find_element_by_css_selector()
# 下面我们就逐一的来看这些定位方法的使用。在此之前，我们拷取百度首页的前端代码，以定位页面上的元素为例进行讲解。
#
# <html>
# <head>
# <body>
# <script>
# <div id="wrapper" style="display: block;">
# <div id="debug" style="display:block;position:..">
# <script>
# <div id="head" class="s_down">
# <div class="head_wrapper">
# <div class="s_form">
# <div class="s_form_wrapper">
# <div id="lg">
# <a id="result_logo" onmousedown="return .." href="/">
# <form id="form" class="fm" action="/s" name="f">
# <input type="hidden" value="utf-8" name="ie">
# <input type="hidden" value="8" name="f">
# <input type="hidden" value="1" name="rsv_bp">
# <input type="hidden" value="1" name="rsv_idx">
# <input type="hidden" value="" name="ch">
# <input type="hidden" value="02.." name="tn">
# <input type="hidden" value="" name="bar">
# <span class="bg s_ipt_wr">
# <input id="kw" class="s_ipt" autocomplete="off"
# maxlength="100" value="" name="wd">
# </span>
# <span class="bg s_btn_wr">
# <input id="su" class="bg s_btn" type="submit"
# value="百度一下">
# </span>
# ....
# </body>
# </html>hello
# 注意这段代码并非百度首页的页面源代码，而是通过前端工具查看所得到页面代码与结构。那么这样的 HTML 结构有如下特征。
#
# （1）它们由标签对组成：
#
# <html></html>
# <body></body>
# <div></div>
# <form></form>
# 那么 html、div 就是标签的标签名。
#
# （2）标签各种属性属性：
#
# <div id="head" class="s_down">
# <from class="well">
# <input id="kw" name="wd" class="s_ipt">
# 就像人一样也会有各种属性，身份证号（id）、姓名（name）、职业（class）等。
#
# （3）标签对之间可以有文本数据。
#
# <a>新闻</a>
# <a>hao123</a>
# <a>地图</a>
# （4）标签有由层级关系
#
# <html>
#     <body>
#     </body>
# </html>
# <div>
#     <from>
#         <input />
#     </from>
# <div>
# 对于上面结构，如果把 input 看作是子标签，那么 form 就是它的父标签。
#
# 理解了上面这些特性是学习定位方法的基础。我们以百度输入框和百度搜索按钮为例来学习不同的定位方法，两个元素的代码如下。
#
# ……
# <input id="kw" class="s_ipt" autocomplete="off" maxlength="100" value=""name="wd">
# ……
# <input id="su" class="bg s_btn" type="submit" value="百度一下">
# 5.1 id 定位
# name 如果把页面上看元素看作一个人的话，如果我们想找一个人如何去找，那么这个人一定有其别于其它人的“属性”，比如他的身份证号一定和别人不一样，他的名字和别人不一样。那么我们就可以通过身证号和名字来找到一个人。那么 id 就可以看做是一个人的身
#
# 份号，当然这个 id 并不像我们现实中的身份证号有那么强的唯一性，如果在一个页面上发现有两个元素的 id="kw"也是不足为奇的，这个取决前端代码的规范程度。
#
# 对百度首页上的输入框与百度搜索按钮来说，定位方法如下：
#
# find_element_by_id("kw")
# find_element_by_id("su")
# find_element_by_id()方法用于元素中 id 属性的定位。
# 5.2 name 定位
# name 的定位与 id 类似，每一个人都会有名字，那么 name 就可作是一个元素的名字。通过 name 定位输入框：
#
# find_element_by_name("wd")
# find_element_by_name()方法用于元素中 name 属性的定位，百度搜索按钮并没有提供 name 属性，那么我们就不能通过 name 去定位百度搜索按钮。
#
# 5.3 class 定位
# class 也是不少元素会有的一个属性，它的定位和 name 以及 id 类似，下面通过 class 去定位百度输入框和百度搜索按钮：
#
# find_element_by_class_name("s_ipt")
# find_element_by_class_name("bg s_btn")
# find_element_by_class_name()方法用于元素中 class 属性的定位。
# 5.4 tag 定位
# tag 定位取的是一个元素的标签名，通过标签名去定位单个元素的唯一性最底，因为在一个页面中有太多的元素标签为<div>和<input>了，所以很难通过标签名去区分不同的元素。
#
# 通过标签名定位百度首页上的输入框与百度搜索按钮：
#
# find_element_by_tag_name("input")
# find_element_by_tag_name("input")
# find_element_by_tag_name()方法通过元素的 tag name 来定位元素。通过上面的例子，我们并不能区别不同的元素，因为在一个页面上标签名相同很难以避免。
#
# 5.5 link 定位
# link 定位与前面介绍的几种定位方法有所不同，它专门用来定位本链接。百度输入框上面的几个文本链接的代码如下：
#
# <a class="mnav" name="tj_trnews" href="http://news.baidu.com">新闻</a>
# <a class="mnav" name="tj_trhao123" href="http://www.hao123.com">hao123</a>
# <a class="mnav" name="tj_trmap" href="http://map.baidu.com">地图</a>
# <a class="mnav" name="tj_trvideo" href="http://v.baidu.com">视频</a>
# <a class="mnav" name="tj_trtieba" href="http://tieba.baidu.com">贴吧>
# 通过查看上面的代码，我们发现通过 name 属性定位是个不错的选择。不过我们这里为了要学习 link定位，通过 link 定位实现如下：
#
# find_element_by_link_text("新闻")
# find_element_by_link_text("hao123")
# find_element_by_link_text("地图")
# find_element_by_link_text("视频")
# find_element_by_link_text("贴吧")
# find_element_by_link_text()方法通过元素标签对之间的文本信息来定位元素。不过，需要强调的是Python 对于中文的支持并不好，如查 Python 在执行中文的地方出现在乱码，可以在中文件字符串的前面加个小“u”可以有效的避免乱码的问题，加 u 的作用是把中文字
#
# 符串转换中 unicode 编码，如：
#
# find_element_by_link_text(u"新闻")
# 5.6 partial link 定位
# parial link 定位是对 link 定们的一个种补充，有些文本连接会比较长，这个时候我们可以取文本链接的有一部分定位，只要这一部分信息可以唯一的标识这个链接。
#
# <a class="mnav" name="tj_lang" href="#">一个很长很长的文本链接</a>
# 通过 partial link 定位如下：
#
# find_element_by_partial_link_text("一个很长的")
# find_element_by_partial_link_text("文本连接")
# find_element_by_link_text()方法通过元素标签对之间的部分文本信息来定位元素。
#
# 6. 定位元素
# selenium提供了多种方式进行定位元素： find_element_by_*
#
# 1 find_element_by_id
# 2 find_element_by_name
# 3 find_element_by_xpath
# 4 find_element_by_link_text
# 5 find_element_by_partial_link_text
# 6 find_element_by_tag_name
# 7 find_element_by_class_name
# 8 find_element_by_css_selector
# 当然也可以一次定位多个元素： find_elements_by_*
#
# 1 find_elements_by_name
# 2 find_elements_by_xpath
# 3 find_elements_by_link_text
# 4 find_elements_by_partial_link_text
# 5 find_elements_by_tag_name
# 6 find_elements_by_class_name
# 7 find_elements_by_css_selector
