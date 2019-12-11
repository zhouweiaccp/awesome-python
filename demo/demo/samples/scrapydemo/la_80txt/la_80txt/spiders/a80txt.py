# -*- coding: utf-8 -*-
import scrapy


class A80txtSpider(scrapy.Spider):
    name = '80txt'
    allowed_domains = ['80txt.la']
    start_urls = ['http://80txt.la/']

    def parse(self, response):
        pass
