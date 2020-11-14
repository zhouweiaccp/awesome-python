# -*- coding: utf-8 -*-
import scrapy
from balingtxt.items import BalingtxtItem


# https://www.bilibili.com/video/BV1jx411b7E3?p=7
# https://github.com/AndyofJuly/scrapyDemo/blob/master/New/Teacher/Teacher/spiders/test.py
class BalingtxtspiderSpider(scrapy.Spider):
    name = 'balingtxtSpider'
    allowed_domains = ['balingtxt.com']
    start_urls = ['http://www.balingtxt.com/sort1/15.html']

    def parse(self, response):
        self.log("A response from %s just arrived!" % response.url)
        items = []
        sites = response.xpath("//div[@class='list_box']")
        for site in sites:
            item = BalingtxtItem()
            item['url'] = site.xpath("./div[@class='title_box']/div[@class='book_bg']/a/@href").extract()[0]
            item['name'] = site.xpath("./div[@class='title_box']/div[@class='book_bg']/a/@title").extract()[0]
            item['status'] = site.xpath("./div[@class='title_box']/div[@class='book_rg']/span[1]/text()").extract()[0]
            item['newDate'] = site.xpath("./div[@class='title_box']/div[@class='book_rg']/span[2]/em/text()").extract()[
                0]
            item['remark'] = site.xpath("./div[@class='book_jj']/text()").extract()[0]
            # more specific
            # item['category'] = urllib.unquote('/'.join(response.url.split('/')[-3:])).decode('utf-8')
            items.append(item)
        return items
