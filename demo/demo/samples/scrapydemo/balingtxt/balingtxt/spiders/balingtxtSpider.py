# -*- coding: utf-8 -*-
import scrapy
from balingtxt.items import BalingtxtItem


# https://www.bilibili.com/video/BV1jx411b7E3?p=7
# https://github.com/AndyofJuly/scrapyDemo/blob/master/New/Teacher/Teacher/spiders/test.py
class BalingtxtspiderSpider(scrapy.Spider):
    name = 'balingtxtSpider'
    allowed_domains = ['balingtxt.com']
    offset=1
    start_urls = ['http://www.balingtxt.com/sort1/{}.html'.format(offset)]

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
            item['author'] = site.xpath("./div[3]/span[1]/a[1]/text()").extract()[0]
            item["sizenum"] = self.finddownloadNum(site.xpath('./div[3]/span[1]').extract_first(),
                                                   site.xpath('./div[3]/span[1]/small[2]').extract_first())
            # 总下载数
            item["downnum"] = self.finddownloadNum(site.xpath('./div[3]/span[1]').extract_first(), site.xpath('./div[3]/span[1]/small[5]').extract_first())
            #lastpage '123'
            #strmaxpage= response.xpath('//div[@id="pages"]/div[1]/div[1]/div[1]/a[@class="last"]/text()').extract_first()
            # more specific
            # item['category'] = urllib.unquote('/'.join(response.url.split('/')[-3:])).decode('utf-8')
            items.append(item)
        return items

    # 字符串查找， strsize=sites[0].xpath('./div[3]/span[1]/small[2]').extract_first()
    #strpan=sites[0].xpath('./div[3]/span[1]').extract_first()
    def finddownloadNum(self,sourcestr,str2):
        index=sourcestr.index(str2)
        span=sourcestr[index+len(str2):]
        return  span[0:span.index('\n')]
