#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# awesome-python - 当前Project名称;
# ppeteer_demo1 - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名; "executablePath": r"F:\360Downloads\chrome-win\chrome.exe",
# 2020/11/20 21:35  https://mohen.blog.csdn.net/article/details/107312709
# pip install pyppeteer -i https://pypi.douban.com/simple
# https://npm.taobao.org/mirrors/chromium-browser-snapshots/Win_x64/818858/chrome-win.zip
# C:\Users\chive\AppData\Local\pyppeteer\pyppeteer\local-chromium\588429

# 头条

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height


async def main():
    width, height = screen_size()
    print(f'screen : [ width:{width} , height:{height} ]')

    browser = await launch(headless=False, args=[f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})

    # 是否启用JS，enabled设为False，则无渲染效果
    await page.setJavaScriptEnabled(enabled=True)

    await page.goto('https://www.toutiao.com')
    await asyncio.sleep(5)

    print(await page.cookies())  # 打印页面cookies
    print(await page.content())  # 打印页面文本
    print(await page.title())  # 打印当前页标题

    # 抓取新闻标题
    title_elements = await page.xpath('//div[@class="title-box"]/a')
    for item in title_elements:
        # 获取文本
        title_str = await (await item.getProperty('textContent')).jsonValue()
        print(await item.getProperty('textContent'))
        # 获取链接
        title_link = await (await item.getProperty('href')).jsonValue()
        print(title_str)
        print(title_link)

    # 在搜索框中输入python
    await page.type('input.tt-input__inner', 'python')

    # 点击搜索按钮
    await page.click('button.tt-button')
    await asyncio.sleep(5)

    # print(page.url)
    # 今日头条点击后新开一个页面, 通过打印url可以看出page还停留在原页面
    # 以下用于切换至新页面
    pages = await browser.pages()
    page = pages[-1]
    # print(page.url)

    page_source = await page.content()
    text = pq(page_source)
    await page.goto(
        url="https://www.toutiao.com/api/search/content/?"
            "aid=24&app_name=web_search&offset=60&format=json"
            "&keyword=python&autoload=true&count=20&en_qc=1"
            "&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1555589585193"
    )
    for i in range(1, 10):
        print(text("#J_section_{} > div > div > div.normal.rbox > div > div.title-box > a > span".format(i)).text())

    # 关闭浏览器
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

