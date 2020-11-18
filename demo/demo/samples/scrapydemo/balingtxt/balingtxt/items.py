# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BalingtxtItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
    newDate = scrapy.Field()
    remark = scrapy.Field()
    downnum = scrapy.Field()
    sizenum = scrapy.Field()
    author = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass
