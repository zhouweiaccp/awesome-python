#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo - 当前Project名称;
# manDebug - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2019/12/1122:07 - 当前系统日期;
# 554961776@qq.com  pip install pypiwin32
# from scrapy.cmdline import execute
# import sys
# import os
#
# # 添加当前项目的绝对地址
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# # 执行 scrapy 内置的函数方法execute，  使用 crawl 爬取并调试，最后一个参数jobbole 是我的爬虫文件名
# execute(['scrapy', 'crawl', '80txt'])


#
# from scrapy import cmdline
#
#
# name = 'douban_movie_top250'
# cmd = 'scrapy crawl {0}'.format('80txt')
# cmdline.execute(cmd.split())

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())
    process.crawl('balingtxtSpider')    #  你需要将此处的spider_name替换为你自己的爬虫名称
    process.start()