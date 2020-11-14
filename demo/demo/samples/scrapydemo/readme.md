



# 2.scrapy 选择器
（1） 正则表达式 ——re()

（2）xpath——xpath()

（3）CSS——css()

response.css("xxx").extract() ——提取所有节点（然后可以通过循环遍历所有的子节点）
response.css("xxx").extract_first() ——提取第一个节点
response.css("xxx::text").extract_first()——获取节点的内部文本
response.css("xxx::attr()").extract_first()——获取节点的属性值（不用加引号）
（4）序列化该节点为unicode字符串并返回list——extract()



## crawl
scrapy crawl  balingtxtSpider -o itm.json -s FEED_EXPORT_ENCODING=utf-8

## css
类选择器：元素的class属性，比如class="box"表示选取class为box的元素；
ID选择器：元素的id属性，比如id="box"表示选取id为box的元素；
元素选择器：直接选择文档元素，比如p表示选择所有的p元素，div表示选择所有的div元素；
属性选择器：选择具有某个属性的元素，如*[title]表示选择所有包含title属性的元素、a[href]表示选择所有带有href属性的a元素等；
后代选择器：选择包含元素后代的元素，如li a表示选取所有li 下所有a元素；
子元素选择器：选择作为某元素子元素的元素，如h1 > strong表示选择父元素为h1 的所有 strong 元素；
相邻兄弟选择器：选择紧接在另一元素后的元素，且二者有相同父元素，如h1 + p表示选择紧接在 h1 元素之后的所有p元素；
scrapy 中的css使用方法
以a元素来举例说明

response.css('a')：返回的是selector对象；
response.css('a').extract()：返回的是a标签对象；
response.css('a::text').extract_first()：返回的是第一个a标签中文本的值；
response.css('a::attr(href)').extract_first()：返回的是第一个a标签中href属性的值；
response.css('a[href*=image]::attr(href)').extract()：返回所有a标签中href属性包含image的值；
response.css('a[href*=image] img::attr(src)').extract()：返回所有a标签下image标签的src属性；

![](./css.png)

##  xpath
xpath('//a')    # 所有a标签(子孙后代)
xpath('//a[2]')        # 所有a标签，按索引找第二个

xpath('//a[@id]')    # 所有a标签，并且含有id属性
xpath('//a[@id="i1"]')        # 所有a标签，并且属性id='i1'
xpath('//a[@href="link.html"][@id="i1"]')    # 所有a标签，属性href="link.html" 而且 id="i1"

xpath('//a[contains(@href, "link")]')    # 所有a标签，属性href的值包含"link"
xpath('//a[starts-with(@href, "link")]')    # 所有a标签，属性href的值以"link"开头
xpath('//a[re:test(@id, "i\d+")]')        # 所有a标签 属性id的值 符合正则表达式"i\d+"的规则

xpath('//a[re:test(@id, "i\d+")]/text()').extract()        # 所有a标签，取text的值
xpath('//a[re:test(@id, "i\d+")]/@href').extract()        # 所有a标签，取href的属性值

xpath('/html/body/ul/li/a/@href').extract()        # 取所有的值
xpath('//body/ul/li/a/@href').extract_first()    # 取第一个值



## link
*[Python_Master_Courses](https://github.com/makelove/Python_Master_Courses/)Python大师课程 
*[itcast.cn教程](https://github.com/AndyofJuly?tab=repositories)
*[smart_login](https://github.com/SpiderClub/smart_login) 各大网站登陆方式，有的是通过selenium登录，有的是通过抓包直接模拟登录
*[SpiderClub](https://github.com/SpiderClub) 分布式爬虫
*[spiders](https://github.com/asen477/scrapy/blob/master/goods/goods/spiders/jd_spider.py) mysql jd
*[wechat-spider)](https://github.com/pythonchannel/wechat-spider) 微信手机客户端爬虫，爬取公众号所有 文章、阅读量、点赞量和评论内容 ---思路比较细
*[wechat-spider)](https://github.com/striver-ing/wechat-spider) 开源微信爬虫：爬取公众号所有 文章、阅读量、点赞量和评论内容。易部署。持续维护！！！
*[](https://github.com/54xingzhe/weixin_crawler) weixin_crawler是一款使用Scrapy、Flask、Echarts、Elasticsearch等实现的微信公众号文章爬虫，自带分析报告和全文检索功能，几百万的文档都能瞬间搜索。
*[](https://github.com/pythonchannel/download-no-copyright-image) 好文章链接
*[](https://mp.weixin.qq.com/s?__biz=MjM5MTQ4NjA3Nw==&mid=2459678096&idx=1&sn=2cc8436f8ab35b03ba81e4e65758ecac&chksm=b1dbcc8286ac4594116c20aa6c9ff36e3428cd19903225bc8e27f20d8e3c27930f4f79d06550&scene=21#wechat_redirect)
*[]()
*[]()
*[]()
*[]()
*[]()
