#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# awesome-python - 当前Project名称;
# ppeteer_demo1 - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# "executablePath": r"F:\360Downloads\chrome-win\chrome.exe",
# 2020/11/20 21:35  https://mohen.blog.csdn.net/article/details/107312709  https://blog.csdn.net/freeking101/article/details/93331204
# pip install pyppeteer -i https://pypi.douban.com/simple
# https://npm.taobao.org/mirrors/chromium-browser-snapshots/Win_x64/818858/chrome-win.zip
# C:\Users\chive\AppData\Local\pyppeteer\pyppeteer\local-chromium\588429


#
# 拦截请求
# 可以对出现的请求，进行拦截 类似mitmproxy。

import asyncio
import json

from jsonpath import jsonpath
from pyppeteer import launcher

# launcher.AUTOMATION_ARGS.remove("--enable-automation")

from pyppeteer import launch

from pyppeteer.network_manager import Request, Response


async def intercept_request(req: Request):
    await req.continue_()  # 请求，看源码可以重新编写请求


async def intercept_response(res: Response):
    if 'ext2020/apub/json/prevent.new' in res.url:
        print('拦截到请求')
        json_text = await res.text()
        title_li = jsonpath(json.loads(json_text), '$..title')
        for title in title_li:
            print(title)
    pass


async def main():
    # 浏览器 启动参数
    start_parm = {
        # 启动chrome的路径
        "executablePath": r"F:\360Downloads\chrome-win\chrome.exe",
        # 关闭无头浏览器 默认是无头启动的
        "headless": False,
        "args": [
            '--disable-infobars',  # 关闭自动化提示框
            # '--no-sandbox',  # 关闭沙盒模式
            '--start-maximized',  # 窗口最大化模式
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            # UA

        ],

    }
    # 创建浏览器对象，可以传入 字典形式参数
    browser = await launch(**start_parm)

    # 创建一个页面对象， 页面操作在该对象上执行
    page = await browser.newPage()
    await page.setJavaScriptEnabled(enabled=True)

    # 启用拦截器
    await page.setRequestInterception(True)
    page.on('request', intercept_request)
    page.on('response', intercept_response)

    js_text = """
    () =>{ 
        Object.defineProperties(navigator,{ webdriver:{ get: () => false } });
        window.navigator.chrome = { runtime: {},  };
        Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] });
        Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], });
     }
        """
    await page.evaluateOnNewDocument(js_text)  # 本页刷新后值不变，自动执行js
    await page.goto('https://news.qq.com/')  # 页面跳转
    await asyncio.sleep(100)  # 不关闭
    # await browser.close()


asyncio.get_event_loop().run_until_complete(main())  # 创建异步池并执行main函数。