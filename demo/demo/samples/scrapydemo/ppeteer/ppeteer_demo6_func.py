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

# 获取验证码
async def main2(self, username, pwd, url):  # 定义main协程函数，

    login_count = 0

    # 打开浏览器
    browser = await launch(
        {'headless': False, "userDataDir": r"./temp_data", 'args': ['--no-sandbox'], })

    # 登录检测
    while login_count < 10:
        # 登录
        await self.login(browser, username, pwd, url)

        # 检测是否登录成功
        if await self.check_login(browser):
            break
        else:
            login_count += 1

    # 尝试登录次数大于10就退出
    if login_count > 10:
        print("login failed!")
        await browser.close()
        return

        do_something()

    # async def login(self, browser, username, pwd, url):
    #     page = await browser.newPage()  # 启动个新的浏览器页面
    #     await page.setUserAgent(
    #         'Mozilla/5.0 (Windows NT 6.1; WOW64) '
    #         'AppleWebKit/537.36 (KHTML, like Gecko) '
    #         'Chrome/68.0.3440.106 Safari/537.36')
    #
    #     await page.goto(url)  # 访问登录页面
    #
    #     # 就是在浏览器运行的时候，始终让window.navigator.webdriver=false
    #     # navigator是windiw对象的一个属性，同时修改plugins，languages，navigator 且让
    #     await page.evaluate(
    #         '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    #
    #     # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
    #     await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    #     await page.evaluate('''() =>{ Object.defineProperty(navigator,
    #      'languages', { get: () => ['en-US', 'en'] }); }''')
    #     await page.evaluate('''() =>{ Object.defineProperty(navigator,
    #      'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
    #
    #     time.sleep(2)
    #
    #     # 使用type选定页面元素，并修改其数值，用于输入账号密码，修改的速度仿人类操作，因为有个输入速度的检测机制
    #     # 因为 pyppeteer 框架需要转换为js操作，而js和python的类型定义不同，所以写法与参数要用字典，类型导入
    #     await page.type('#username', username, {'delay': self.input_time_random() - 50})
    #     await page.type('#password', pwd, {'delay': self.input_time_random()})
    #
    #     # await page.screenshot({'path': './picture/headless-test-result.png'})    # 截图测试
    #
    #     time.sleep(1)
    #
    #     # 验证码操作
    #     verification_code(page);
    #
    # # 点击提交
    # submit = await page.xpath("//button[@class='auth_login_btn primary full_width']")
    # await submit[0].click()
    #
    # time.sleep(1)


asyncio.get_event_loop().run_until_complete(main())  # 创建异步池并执行main函数。