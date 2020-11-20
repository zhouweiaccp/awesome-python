#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# awesome-python - 当前Project名称;
# ppeteer_demo1 - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名; "executablePath": r"F:\360Downloads\chrome-win\chrome.exe",
# 2020/11/20 21:35  https://mohen.blog.csdn.net/article/details/107312709  https://blog.csdn.net/freeking101/article/details/93331204
# pip install pyppeteer -i https://pypi.douban.com/simple
# https://npm.taobao.org/mirrors/chromium-browser-snapshots/Win_x64/818858/chrome-win.zip
# C:\Users\chive\AppData\Local\pyppeteer\pyppeteer\local-chromium\588429



# 这里我们又用到了几个新的 API，完成了网页截图保存、网页导出 PDF 保存、执行 JavaScript 并返回对应数据。
#
#  evaluate 方法执行了一些 JavaScript，JavaScript 传入的是一个函数，使用 return 方法返回了网页的宽高、像素大小比率三个值，最后得到的是一个 JSON 格式的对象。
#
# 总之利用 Pyppeteer 我们可以控制浏览器执行几乎所有动作，想要的操作和功能基本都可以实现，用它来自由地控制爬虫当然就不在话下了。
# 了解了基本的实例之后，我们再来梳理一下 Pyppeteer 的一些基本和常用操作。Pyppeteer 的几乎所有功能都能在其官方文档的 API Reference
# 里面找到，链接为：https://miyakogi.github.io/pyppeteer/reference.html，用到哪个方法就来这里查询就好了，
# 参数不必死记硬背，即用即查就好
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    url = 'http://quotes.toscrape.com/js/'
    await page.goto(url=url)
    await page.screenshot(path='test_screenshot.png')
    await page.pdf(path='test_pdf.pdf')

    # 在网页上执行js 脚本
    dimensions = await page.evaluate(pageFunction='''() => {
                return {
                    width: document.documentElement.clientWidth,    // 页面宽度
                    height: document.documentElement.clientHeight,  // 页面高度
                    deviceScaleFactor: window.devicePixelRatio,     // 像素比 1.0000000149011612
                }
            }''', force_expr=False)  # force_expr=False  执行的是函数

    print(dimensions)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

# 结果
# {'width': 800, 'height': 600, 'deviceScaleFactor': 1}
