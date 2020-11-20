#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# awesome-python - 当前Project名称;
# ppeteer_demo1 - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名; "executablePath": r"F:\360Downloads\chrome-win\chrome.exe",
# 2020/11/20 21:35  https://mohen.blog.csdn.net/article/details/107312709
# pip install pyppeteer -i https://pypi.douban.com/simple
# https://npm.taobao.org/mirrors/chromium-browser-snapshots/Win_x64/818858/chrome-win.zip
# C:\Users\chive\AppData\Local\pyppeteer\pyppeteer\local-chromium\588429

import time
import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({'width': 1200, 'height': 800})
    await page.goto('https://www.baidu.com')
    # 在搜索框中输入python
    await page.type('input#kw.s_ipt', 'python')
    # 点击搜索按钮
    await page.click('input#su')

    # 等待元素加载，第一种方法，强行等待5秒
    # await asyncio.sleep(5)

    # 第二种方法，在while循环里强行查询某元素进行等待
    while not await page.querySelector('.t'):
        pass

    # 滚动到页面底部
    await page.evaluate('window.scrollBy(0, window.innerHeight)')

    # 这些等待方法都不好用
    # await page.waitForXPath('h3', timeout=300)
    # await page.waitForNavigation(waitUntil="networkidle0")
    # await page.waitForFunction('document.getElementByTag("h3")')
    # await page.waitForSelector('.t')
    # await page.waitFor('document.querySelector("#t")')
    # await page.waitForNavigation(waitUntil='networkidle0')
    # await page.waitForFunction('document.querySelector("").inner‌​Text.length == 7')

    title_elements = await page.xpath('//h3[contains(@class,"t")]/a')
    for item in title_elements:
        title_str = await (await item.getProperty('textContent')).jsonValue()
        print(title_str)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
