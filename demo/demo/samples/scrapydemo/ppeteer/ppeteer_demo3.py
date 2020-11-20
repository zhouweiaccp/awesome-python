#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# awesome-python - 当前Project名称;
# ppeteer_demo1 - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名; "executablePath": r"F:\360Downloads\chrome-win\chrome.exe",
# 2020/11/20 21:35  https://mohen.blog.csdn.net/article/details/107312709
# pip install pyppeteer -i https://pypi.douban.com/simple
# https://npm.taobao.org/mirrors/chromium-browser-snapshots/Win_x64/818858/chrome-win.zip
# C:\Users\chive\AppData\Local\pyppeteer\pyppeteer\local-chromium\588429

# taobbao    没关闭页面
import asyncio
from pyppeteer import launch

width, height = 1366, 768

js1 = '''() =>{Object.defineProperties(navigator,{ webdriver:{ get: () => false}})}'''
js2 = '''() => {alert(window.navigator.webdriver)}'''
js3 = '''() => {window.navigator.chrome = {runtime: {}, }; }'''
js4 = '''() =>{Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});}'''
js5 = '''() =>{Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5,6],});}'''


async def page_evaluate(page):
    # 替换淘宝在检测浏览时采集的一些参数
    # 需要注意，在测试的过程中发现登陆成功后页面的该属性又会变成True
    # 所以在每次重新加载页面后要重新设置该属性的值。
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')


async def main():
    browser = await launch(
        headless=False,
        # userDataDir='./userdata',
        args=['--disable-infobars', f'--window-size={width},{height}', '--no-sandbox']
    )
    page = await browser.newPage()

    await page.setViewport(
        {
            "width": width,
            "height": height
        }
    )
    url = 'https://www.taobao.com'
    await page.goto(url=url)

    # await page.evaluate(js1)
    # await page.evaluate(js3)
    # await page.evaluate(js4)
    # await page.evaluate(js5)

    await page_evaluate(page)

    await asyncio.sleep(100)  #不关闭
    # await browser.close()


asyncio.get_event_loop().run_until_complete(main())
