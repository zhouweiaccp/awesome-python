#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo - 当前Project名称;
# manDebug - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2019/12/1122:07 - 当前系统日期;
# 554961776@qq.com


from scrapy.cmdline import execute
import os
import sys

# 添加当前项目的绝对地址
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# 执行 scrapy 内置的函数方法execute，  使用 crawl 爬取并调试，最后一个参数jobbole 是我的爬虫文件名
execute(['scrapy', 'crawl', '80txt'])
