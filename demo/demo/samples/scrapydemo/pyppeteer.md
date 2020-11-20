
pyppeteer github 地址：https://github.com/miyakogi/pyppeteer

pyppeteer  英文文档地址：https://miyakogi.github.io/pyppeteer/
pyppeteer 官方文档 API Reference ：https://miyakogi.github.io/pyppeteer/reference.html

puppeteer（ Nodejs 版 selenium ）快速入门：https://blog.csdn.net/freeking101/article/details/91542887

爬虫界又出神器|一款比selenium更高效的利器：https://blog.csdn.net/chen801090/article/details/93216278

python爬虫利器 pyppeteer(模拟浏览器) 实战：https://blog.csdn.net/xiaoming0018/article/details/89841728

重点：pyppeteer使用遇到的 bug 及解决方法：http://www.sanfenzui.com/pyppeteer-bug-collection.html

pyppeteer 进阶技巧 （ Xvfb 配合实现 headless 效果 ）：https://www.cnblogs.com/dyfblog/p/10887940.html

Python爬虫之pyppeteer的使用（爬虫、获取cookie、截屏插件、防爬绕过）：https://mohen.blog.csdn.net/article/details/107312709

 

 

Pyppeteer 简介
 

提起 selenium 想必大家都不陌生，作为一款知名的 Web 自动化测试框架，selenium 支持多款主流浏览器，提供了功能丰富的API 接口，经常被我们用作爬虫工具来使用。但是 selenium 的缺点也很明显，比如速度太慢、对版本配置要求严苛，最麻烦是经常要更新对应的驱动。还有些网页是可以检测到是否是使用了selenium 。并且selenium 所谓的保护机制不允许跨域 cookies 保存以及登录的时候必须先打开网页然后后加载 cookies 再刷新的方式很不友好。

今天就给大家介绍另一款 web 自动化测试工具 Pyppeteer，虽然支持的浏览器比较单一，但在安装配置的便利性和运行效率方面都要远胜 selenium。

介绍 Pyppeteer 之前先说一下 Puppeteer，Puppeteer 是 Google 基于 Node.js 开发的一个工具，主要是用来操纵 Chrome  浏览器的 API，通过 Javascript 代码来操纵 Chrome 浏览器的一些操作，用作网络爬虫完成数据爬取、Web 程序自动测试等任务。其 API 极其完善，功能非常强大。 而 Pyppeteer 又是什么呢？它实际上是 Puppeteer 的 Python 版本的实现，但他不是 Google 开发的，是一位来自于日本的工程师依据 Puppeteer 的一些功能开发出来的非官方版本。

Pyppeteer 其实是 Puppeteer 的 Python 版本。pyppeteer 模块看不懂就去看puppeteer文档，pyppeteer 只是在 puppeteer之上稍微包装了下而已 。

注意：本来 chrome 就问题多多，puppeteer 也是各种坑，加上 pyppeteer 是基于前者的改编 python 版本，也就是产生了只要前两个有一个有 bug，那么 pyppeteer 就会原封不动的继承下来，本来这没什么，但是现在遇到的问题就是 pyppeteer 这个项目从2018年9月份之后几乎没更新过，前两者都在不断的更新迭代，而 pyppeteer 一直不更新，导致很多 bug 根本没人修复。

 

下面简单介绍下 Pyppeteer 的两大特点：chromium 浏览器 和 asyncio框架：

 

1).chromium
Chromium 是一款独立的浏览器，是 Google 为发展自家的浏览器 Google Chrome 而开启的计划，相当于 Chrome的实验版，且 Chromium 是完全开源的。二者基于相同的源代码构建，Chrome 所有的新功能都会先在 Chromium 上实现，待验证稳定后才会移植，因此 Chromium 的版本更新频率更高，也会包含很多新的功能，但作为一款独立的浏览器，Chromium 的用户群体要小众得多。两款浏览器“同根同源”，它们有着同样的 Logo，但配色不同，Chrome 由蓝红绿黄四种颜色组成，而 Chromium 由不同深度的蓝色构成。



Pyppeteer 的 web 自动化是基于 chromium 来实现的，由于 chromium 中某些特性的关系，Pyppeteer 的安装配置非常简单，关于这一点稍后我们会详细介绍。

 

2).asyncio
asyncio 是 Python 的一个异步协程库，自3.4版本引入的标准库，直接内置了对异步IO的支持，号称是Python最有野心的库，官网上有非常详细的介绍：https://docs.python.org/3/library/asyncio.html

 

 

安装与使用
 

由于 Pyppeteer 采用了 Python 的 async 机制，所以其运行要求的 Python 版本为 3.5 及以上。

 

1).极简安装
使用 pip3 install pyppeteer 命令就能完成 pyppeteer 库的安装，至于 chromium 浏览器，只需要一条 pyppeteer-install 命令就会自动下载对应的最新版本 chromium 浏览器到 pyppeteer 的默认位置。

window 下 安装完 pyppeteer ，会在 python 安装目录下的 Scripts 目录下 有 pyppeteer-install.exe 和 pyppeteer-install-script.py 两个文件，执行 任意一个都可以安装 chromium 浏览器到 pyppeteer 的默认位置。



运行 pyppeteer-install.exe ：



如果不运行 pyppeteer-install 命令，在第一次使用 pyppeteer 的时候也会自动下载并安装 chromium 浏览器，效果是一样的。总的来说，pyppeteer 比起 selenium 省去了 driver 配置的环节。

当然，出于某种原因（需要梯子，或者科学上网），也可能会出现chromium自动安装无法顺利完成的情况，这时可以考虑手动安装：首先，从下列网址中找到自己系统的对应版本，下载chromium压缩包；

'linux': 'https://storage.googleapis.com/chromium-browser-snapshots/Linux_x64/575458/chrome-linux.zip'
'mac': 'https://storage.googleapis.com/chromium-browser-snapshots/Mac/575458/chrome-mac.zip'
'win32': 'https://storage.googleapis.com/chromium-browser-snapshots/Win/575458/chrome-win32.zip'
'win64': 'https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/575458/chrome-win32.zip'

然后，将压缩包放到pyppeteer的指定目录下解压缩，windows系统的默认目录。

其他系统下的默认目录可以参照下面：

Windows: C:\Users\<username>\AppData\Local\pyppeteer
OS X: /Users/<username>/Library/Application Support/pyppeteer
Linux: /home/<username>/.local/share/pyppeteer
or in $XDG_DATA_HOME/pyppeteer if $XDG_DATA_HOME is defined.
Details see appdirs’s user_data_dir.

好了，安装完成之后我们命令行下测试下：
>>> import pyppeteer
如果没有报错，那么就证明安装成功了。

 

2).使用
Pyppeteer 是一款非常高效的 web 自动化测试工具，由于 Pyppeteer 是基于 asyncio 构建的，它的所有 属性 和方法 几乎都是 coroutine (协程) 对象，因此在构建异步程序的时候非常方便，天生就支持异步运行。

程序构建的基本思路是新建 一个 browser 浏览器 和 一个 页面 page。

看下面这段代码，在 main 函数中，先是建立一个浏览器对象，然后打开新的标签页，访问百度主页，对当前页面截图并保存为“example.png”，最后关闭浏览器。前文也提到过，pyppeteer 是基于 asyncio 构建的，所以在使用的时候需要用到 async/await 结构。

import asyncio
from pyppeteer import launch
 
 
async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://baidu.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()
 
 
asyncio.get_event_loop().run_until_complete(main())
运行上面这段代码会发现并没有浏览器弹出运行，这是因为 Pyppeteer 默认使用的是无头浏览器，如果想要浏览器显示，需要在launch 函数中设置参数 “headless =False”，程序运行结束后在同一目录下会出现截取到的网页图片：



 

遇到的错误
 

1）pyppeteer.errors.NetworkError: Protocol error Network.getCookies: Target close
控制访问指定 url 之后 await page.goto(url)，会遇到上面的错误，如果这时候使用了 sleep 之类的延时也会出现这个错误或者类似的 time out。 
这个问题是 puppeteer 的 bug，但是对方已经修复了，而 pyppeteer 迟迟没更新，就只能靠自己了，搜了很多人的文章，例如：https://github.com/miyakogi/pyppeteer/issues/171 ，但是我按照这个并没有成功。也有人增加一个函数，但调用这个参数依然没解决问题。

async def scroll_page(page):
    cur_dist = 0
    height = await page.evaluate("() => document.body.scrollHeight")
    while True:
        if cur_dist < height:
            await page.evaluate("window.scrollBy(0, 500);")
            await asyncio.sleep(0.1)
            cur_dist += 500
        else:
            break
可以把 python 第三方库 websockets 版本 7.0 改为 6.0 就可以了，亲测可用。

pip uninstall websockets #卸载websockets
 
pip install websockets==6.0 
或者
pip install websockets==6.0 --force-reinstall #指定安装6.0版本
 

2）chromium浏览器多开页面卡死问题。
解决这个问题的方法就是浏览器初始化的时候添加'dumpio':True。

# 启动 pyppeteer 属于内存中实现交互的模拟器
browser = await launch({'headless': False, 'args': ['--no-sandbox'], 'dumpio': True})
3）浏览器窗口很大，内容显示很小。
需要设置浏览器显示大小，默认就是无法正常显示。可以看到页面左侧右侧都是空白，网站内容并没有完整铺满chrome.

# Pyppeteer 支持字典 和 关键字传参，Puppeteer 只支持字典传参。
# 这里使用字典传参
browser = await launch(
    {
        'headless': False, 
        'dumpio': True, 
        'autoClose': False, 
        'args': [
            '--no-sandbox', 
            '--window-size=1366,850'
        ]
    }
)
await page.setViewport({'width': 1366, 'height': 768})
通过上面设置Windows-size和Viewport大小来实现网页完整显示。

但是对于那种向下无限加载的长网页这种情况如果浏览器是可见状态会显示不全，针对这种情况的解决方法就是复制当前网页新开一个标签页粘贴进去就正常了

 

Pyppeteer 和 Puppeteer 的 不同点

Pyppeteer支持字典和关键字传参，Puppeteer只支持字典传参
# Puppeteer只支持字典传参
browser = await launch({'headless': True})
# Pyppeteer支持字典和关键字传参
browser = await launch({'headless': True})
browser = await launch(headless=True)
元素选择器方法名 $变为querySelector
# Puppeteer使用$符
Page.$()/Page.$$()/Page.$x()
# Pyppeteer使用Python风格的函数名
Page.querySelector()/Page.querySelectorAll()/Page.xpath()
# 简写方式为：
Page.J(), Page.JJ(), and Page.Jx()
Page.evaluate() 和 Page.querySelectorEval()的参数
Puppeteer的evaluate()方法使用JavaScript原生函数或JavaScript表达式字符串。Pyppeteer的evaluate()方法只使用JavaScript字符串，该字符串可以是函数也可以是表达式，Pyppeteer会进行自动判断。但有时会判断错误，如果字符串被判断成了函数，并且报错，可以添加选项force_expr=True，强制Pyppeteer作为表达式处理。

获取页面内容：

content = await page.evaluate('document.body.textContent', force_expr=True)
获取元素的内部文字：

element = await page.querySelector('h1')
title = await page.evaluate('(element) => element.textContent', element)
 

基础用法
 

抓取内容  可以使用 xpath 表达式
"""
# Pyppeteer 三种解析方式
    Page.querySelector()      # 选择器
    Page.querySelectorAll()
    Page.xpath()                   # xpath  表达式
# 简写方式为：
    Page.J(), Page.JJ(), and Page.Jx()
"""

示例 1 ：

import asyncio
from pyppeteer import launch
 
 
async def main():
    # headless参数设为False，则变成有头模式
    # Pyppeteer支持字典和关键字传参，Puppeteer只支持字典传参
    
    # 指定引擎路径
    # exepath = r'C:\Users\Administrator\AppData\Local\pyppeteer\pyppeteer\local-chromium\575458\chrome-win32/chrome.exe'
    # browser = await launch({'executablePath': exepath, 'headless': False, 'slowMo': 30})
    
    browser = await launch(
        # headless=False,
        {'headless': False}
    )
 
    page = await browser.newPage()
 
    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})
 
    # 是否启用JS，enabled设为False，则无渲染效果
    await page.setJavaScriptEnabled(enabled=True)
    # 超时间见 1000 毫秒
    res = await page.goto('https://www.toutiao.com/', options={'timeout': 1000})
    resp_headers = res.headers  # 响应头
    resp_status = res.status  # 响应状态
    
    # 等待
    await asyncio.sleep(2)
    # 第二种方法，在while循环里强行查询某元素进行等待
    while not await page.querySelector('.t'):
        pass
    # 滚动到页面底部
    await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
 
    await asyncio.sleep(2)
    # 截图 保存图片
    await page.screenshot({'path': 'toutiao.png'})
 
    # 打印页面cookies
    print(await page.cookies())
 
    """  打印页面文本 """
    # 获取所有 html 内容
    print(await page.content())
 
    # 在网页上执行js 脚本
    dimensions = await page.evaluate(pageFunction='''() => {
            return {
                width: document.documentElement.clientWidth,  // 页面宽度
                height: document.documentElement.clientHeight,  // 页面高度
                deviceScaleFactor: window.devicePixelRatio,  // 像素比 1.0000000149011612
            }
        }''', force_expr=False)  # force_expr=False  执行的是函数
    print(dimensions)
 
    #  只获取文本  执行 js 脚本  force_expr  为 True 则执行的是表达式
    content = await page.evaluate(pageFunction='document.body.textContent', force_expr=True)
    print(content)
 
    # 打印当前页标题
    print(await page.title())
 
    # 抓取新闻内容  可以使用 xpath 表达式
    """
    # Pyppeteer 三种解析方式
    Page.querySelector()  # 选择器
    Page.querySelectorAll()
    Page.xpath()  # xpath  表达式
    # 简写方式为：
    Page.J(), Page.JJ(), and Page.Jx()
    """
    element = await page.querySelector(".feed-infinite-wrapper > ul>li")  # 纸抓取一个
    print(element)
    # 获取所有文本内容  执行 js
    content = await page.evaluate('(element) => element.textContent', element)
    print(content)
 
    # elements = await page.xpath('//div[@class="title-box"]/a')
    elements = await page.querySelectorAll(".title-box a")
    for item in elements:
        print(await item.getProperty('textContent'))
        # <pyppeteer.execution_context.JSHandle object at 0x000002220E7FE518>
 
        # 获取文本
        title_str = await (await item.getProperty('textContent')).jsonValue()
 
        # 获取链接
        title_link = await (await item.getProperty('href')).jsonValue()
        print(title_str)
        print(title_link)
 
    # 关闭浏览器
    await browser.close()
 
 
asyncio.get_event_loop().run_until_complete(main())
示例 2 ：

import asyncio
import pyppeteer
from collections import namedtuple
 
headers = {
    'date': 'Sun, 28 Apr 2019 06:50:20 GMT',
    'server': 'Cmcc',
    'x-frame-options': 'SAMEORIGIN\nSAMEORIGIN',
    'last-modified': 'Fri, 26 Apr 2019 09:58:09 GMT',
    'accept-ranges': 'bytes',
    'cache-control': 'max-age=43200',
    'expires': 'Sun, 28 Apr 2019 18:50:20 GMT',
    'vary': 'Accept-Encoding,User-Agent',
    'content-encoding': 'gzip',
    'content-length': '19823',
    'content-type': 'text/html',
    'connection': 'Keep-alive',
    'via': '1.1 ID-0314217270751344 uproxy-17'
}
 
Response = namedtuple("rs", "title url html cookies headers history status")
 
 
async def get_html(url):
    browser = await pyppeteer.launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    res = await page.goto(url, options={'timeout': 10000})
    data = await page.content()
    title = await page.title()
    resp_cookies = await page.cookies()  # cookie
    resp_headers = res.headers  # 响应头
    resp_status = res.status  # 响应状态
    print(data)
    print(title)
    print(resp_headers)
    print(resp_status)
    return title
 
 
if __name__ == '__main__':
    url_list = [
        "https://www.toutiao.com",
        "http://jandan.net/ooxx/page-8#comments",
        "https://www.12306.cn/index"
    ]
    task = [get_html(url) for url in url_list]
 
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*task))
    for res in results:
        print(res)
 

模拟输入
模拟输入文本：

# 模拟输入 账号密码  {'delay': rand_int()} 为输入时间
await page.type('#TPL_username_1', "sadfasdfasdf")
await page.type('#TPL_password_1', "123456789", )
 
await page.waitFor(1000)
await page.click("#J_SubmitStatic")
使用 tkinter 获取页面高度 宽度

def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height
 

爬取京东商城
示例代码：

import requests
from bs4 import BeautifulSoup
from pyppeteer import launch
import asyncio
 
 
def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height
 
 
async def main(url):
    # browser = await launch({'headless': False, 'args': ['--no-sandbox'], })
    browser = await launch({'args': ['--no-sandbox'], })
    page = await browser.newPage()
    width, height = screen_size()
    await page.setViewport(viewport={"width": width, "height": height})
    await page.setJavaScriptEnabled(enabled=True)
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    )
    await page.goto(url)
 
    # await asyncio.sleep(2)
 
    await page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
 
    await asyncio.sleep(1)
 
    # content = await page.content()
    li_list = await page.xpath('//*[@id="J_goodsList"]/ul/li')
 
    # print(li_list)
    item_list = []
    for li in li_list:
        a = await li.xpath('.//div[@class="p-img"]/a')
        detail_url = await (await a[0].getProperty("href")).jsonValue()
        promo_words = await (await a[0].getProperty("title")).jsonValue()
        a_ = await li.xpath('.//div[@class="p-commit"]/strong/a')
        p_commit = await (await a_[0].getProperty("textContent")).jsonValue()
        i = await li.xpath('./div/div[3]/strong/i')
        price = await (await i[0].getProperty("textContent")).jsonValue()
        em = await li.xpath('./div/div[4]/a/em')
        title = await (await em[0].getProperty("textContent")).jsonValue()
        item = {
            "title": title,
            "detail_url": detail_url,
            "promo_words": promo_words,
            'p_commit': p_commit,
            'price': price
        }
        item_list.append(item)
        # print(item)
        # break
    # print(content)
 
    await page_close(browser)
    return item_list
 
 
async def page_close(browser):
    for _page in await browser.pages():
        await _page.close()
    await browser.close()
 
 
msg = "手机"
url = "https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq={}&cid2=653&cid3=655&page={}"
 
task_list = []
for i in range(1, 6):
    page = i * 2 - 1
    url = url.format(msg, msg, page)
    task_list.append(main(url))
 
loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*task_list))
# print(results, len(results))
for i in results:
    print(i, len(i))
 
print('*' * 100)
# soup = BeautifulSoup(content, 'lxml')
# div = soup.find('div', id='J_goodsList')
# for i, li in enumerate(div.find_all('li', class_='gl-item')):
#     if li.select('.p-img a'):
#         print(li.select('.p-img a')[0]['href'], i)
#         print(li.select('.p-price i')[0].get_text(), i)
#         print(li.select('.p-name em')[0].text, i)
#     else:
#         print("#" * 200)
#         print(li)
 

抓取淘宝
示例代码：

# -*- coding: utf-8 -*-
 
import time
import random
import asyncio
from retrying import retry  # 错误自动重试
from pyppeteer.launcher import launch
 
 
js1 = '''() =>{Object.defineProperties(navigator,{ webdriver:{ get: () => false}})}'''
js2 = '''() => {alert(window.navigator.webdriver)}'''
js3 = '''() => {window.navigator.chrome = {runtime: {}, }; }'''
js4 = '''() =>{Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});}'''
js5 = '''() =>{Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5,6],});}'''
 
 
def retry_if_result_none(result):
    return result is None
 
 
@retry(retry_on_result=retry_if_result_none, )
async def mouse_slide(page=None):
    await asyncio.sleep(3)
    try:
        await page.hover('#nc_1_n1z')
        await page.mouse.down()
        await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
        await page.mouse.up()
 
    except Exception as e:
        print(e, '     :slide login False')
        return None
    else:
        await asyncio.sleep(3)
        slider_again = await page.Jeval('.nc-lang-cnt', 'node => node.textContent')
        if slider_again != '验证通过':
            return None
        else:
            await page.screenshot({'path': './headless-slide-result.png'})
            print('验证通过')
            return 1
 
 
def input_time_random():
    return random.randint(100, 151)
 
 
def screen_size():
    """使用tkinter获取屏幕大小"""
    import tkinter
    tk = tkinter.Tk()
    width = tk.winfo_screenwidth()
    height = tk.winfo_screenheight()
    tk.quit()
    return width, height
 
 
async def main(username, pwd, url):
    browser = await launch(
        {'headless': False, 'args': ['--no-sandbox'], },
        userDataDir='./userdata',
        args=['--window-size=1366,768']
    )
    page = await browser.newPage()
    width, height = screen_size()
    await page.setViewport(viewport={"width": width, "height": height})
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
    )
 
    await page.goto(url)
    await page.evaluate(js1)
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)
 
    pwd_login = await page.querySelector('.J_Quick2Static')
    # print(await (await pwd_login.getProperty('textContent')).jsonValue())
    await pwd_login.click()
 
    await page.type('#TPL_username_1', username, {'delay': input_time_random() - 50})
    await page.type('#TPL_password_1', pwd, {'delay': input_time_random()})
 
    await page.screenshot({'path': './headless-test-result.png'})
    time.sleep(2)
 
    slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块
 
    if slider:
        print('出现滑块情况判定')
        await page.screenshot({'path': './headless-login-slide.png'})
        flag = await mouse_slide(page=page)
        if flag:
            print(page.url)
            await page.keyboard.press('Enter')
            await get_cookie(page)
    else:
        await page.keyboard.press('Enter')
        await page.waitFor(20)
        await page.waitForNavigation()
        try:
            global error
            error = await page.Jeval('.error', 'node => node.textContent')
        except Exception as e:
            error = None
            print(e, "错啦")
        finally:
            if error:
                print('确保账户安全重新入输入')
            else:
                print(page.url)
                # 可继续网页跳转 已经携带 cookie
                # await get_search(page)
                await get_cookie(page)
    await page_close(browser)
 
 
async def page_close(browser):
    for _page in await browser.pages():
        await _page.close()
    await browser.close()
 
 
async def get_search(page):
    # https://s.taobao.com/search?q={查询的条件}&p4ppushleft=1%2C48&s={每页 44 条 第一页 0 第二页 44}&sort=sale-desc
    await page.goto("https://s.taobao.com/search?q=气球")
 
    await asyncio.sleep(5)
    # print(await page.content())
 
 
# 获取登录后cookie
async def get_cookie(page):
    res = await page.content()
    cookies_list = await page.cookies()
    cookies = ''
    for cookie in cookies_list:
        str_cookie = '{0}={1};'
        str_cookie = str_cookie.format(cookie.get('name'), cookie.get('value'))
        cookies += str_cookie
    print(cookies)
    # 将cookie 放入 cookie 池 以便多次请求 封账号 利用cookie 对搜索内容进行爬取
    return cookies
 
 
if __name__ == '__main__':
    tb_username = '淘宝用户名'
    tb_pwd = '淘宝密码'
    tb_url = "https://login.taobao.com/member/login.jhtml"
 
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(tb_username, tb_pwd, tb_url))
 

利用 上面 获取到的 cookie 爬取搜索内容
示例代码：

import json
import requests
import re
 
# 设置 cookie 池 随机发送请求 通过 pyppeteer 获取 cookie
cookie = '_tb_token_=edd7e354dee53;t=fed8f4ca1946ca1e73223cfae04bc589;sg=20f;cna=2uJSFdQGmDMCAbfFWXWAC4Jv;cookie2=1db6cd63ad358170ea13319f7a862c33;_l_g_=Ug%3D%3D;v=0;unb=3150916610;skt=49cbfd5e01d1b550;cookie1=BxVRmD3sh19TaAU6lH88bHw5oq%2BgcAGcRe229Hj5DTA%3D;csg=cf45a9e2;uc3=vt3=F8dByEazRMnQZDe%2F9qI%3D&id2=UNGTqfZ61Z3rsA%3D%3D&nk2=oicxO%2BHX4Pg%3D&lg2=U%2BGCWk%2F75gdr5Q%3D%3D;existShop=MTU1Njg3MDM3MA%3D%3D;tracknick=%5Cu7433150322;lgc=%5Cu7433150322;_cc_=V32FPkk%2Fhw%3D%3D;mt=ci=86_1;dnk=%5Cu7433150322;_nk_=%5Cu7433150322;cookie17=UNGTqfZ61Z3rsA%3D%3D;tg=0;enc=tThHs6Sn3BAl8v1fu3J4tMpgzA1n%2BLzxjib0vDAtGsXJCb4hqQZ7Z9fHIzsN0WghdcKEsoeKz6mBwPUpyzLOZw%3D%3D;JSESSIONID=B3F383B3467EC60F8CA425935232D395;l=bBMspAhrveV5732DBOCanurza77OSIRYYuPzaNbMi_5pm6T_G4QOlC03xF96VjfRswYBqh6Mygv9-etuZ;hng=CN%7Czh-CN%7CCNY%7C156;isg=BLi41Q8PENDal3xUVsA-aPbfiWaKiRzB6vcTu_IpBPOmDVj3mjHsO86vxUQYW9SD;uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=UIHiLt3xD8xYTw%3D%3D&existShop=false&pas=0&cookie14=UoTZ4ttqLhxJww%3D%3D&tag=8&lng=zh_CN;thw=cn;x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0;swfstore=34617;'
 
headers = {
    'cookie': cookie,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
}
 
rep = requests.get('https://s.taobao.com/search?q=手机&p4ppushleft=1%2C48&s=0&sort=sale-desc ', headers=headers)
rep.encoding = 'utf-8'
res = rep.text
print(res)
 
r = re.compile(r'g_page_config = (.*?)g_srp_loadCss', re.S)
res = r.findall(res)
 
data = res[0].strip().rstrip(';')
dic_data = json.loads(data)
auctions = dic_data.get('mods')['itemlist']['data']['auctions']
 
# print(auctions,len(auctions))
for item in auctions[1:]:
    print(item)
    break
 

针对iframe 的操作
page.frames 获取所有的 iframe 列表 需要判断操作的是哪一个 iframe 跟操作 page 一样操作
from pyppeteer import launch
import asyncio
 
 
async def main(url):
    w = await launch({'headless': False, 'args': ['--no-sandbox'], })
 
    page = await w.newPage()
    await page.setViewport({"width": 1366, 'height': 800})
    await page.goto(url)
    try:
        await asyncio.sleep(1)
 
        frame = page.frames
        print(frame)  # 需要找到是哪一个 frame
        title = await frame[1].title()
        print(title)
        await asyncio.sleep(1)
        login = await frame[1].querySelector('#switcher_plogin')
        print(login)
        await login.click()
 
        await asyncio.sleep(20)
    except Exception as e:
        print(e, "EEEEEEEEE")
 
    for _page in await w.pages():
        await _page.close()
    await w.close()
 
 
asyncio.get_event_loop().run_until_complete(main("https://i.qq.com/?rd=1"))
# asyncio.get_event_loop().run_until_complete(main("https://www.gushici.com/"))
 

与 scrapy 的整合
加入downloadmiddleware

from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
import pyppeteer
import asyncio
import os
from scrapy.http import HtmlResponse
 
pyppeteer.DEBUG = False 
 
class FundscrapyDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self) :
        print("Init downloaderMiddleware use pypputeer.")
        os.environ['PYPPETEER_CHROMIUM_REVISION'] ='588429'
        # pyppeteer.DEBUG = False
        print(os.environ.get('PYPPETEER_CHROMIUM_REVISION'))
        loop = asyncio.get_event_loop()
        task = asyncio.ensure_future(self.getbrowser())
        loop.run_until_complete(task)
 
        #self.browser = task.result()
        print(self.browser)
        print(self.page)
        # self.page = await browser.newPage()
    async def getbrowser(self):
        self.browser = await pyppeteer.launch()
        self.page = await self.browser.newPage()
        # return await pyppeteer.launch()
    async def getnewpage(self): 
        return  await self.browser.newPage()
 
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s
 
    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
 
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        loop = asyncio.get_event_loop()
        task = asyncio.ensure_future(self.usePypuppeteer(request))
        loop.run_until_complete(task)
        # return task.result()
        return HtmlResponse(url=request.url, body=task.result(), encoding="utf-8",request=request)
 
    async def usePypuppeteer(self, request):
        print(request.url)
        # page = await self.browser.newPage()
        await self.page.goto(request.url)
        content = await self.page.content()
        return content 
 
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
 
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response
 
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.
 
        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass
 
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
 

 

实战 异步爬取
 

示例 1 ：快速上手
接下来我们测试下基本的页面渲染操作，这里我们选用的网址为：http://quotes.toscrape.com/js/，这个页面是 JavaScript 渲染而成的，用基本的 requests 库请求得到的 HTML 结果里面是不包含页面中所见的条目内容的。

为了证明 requests 无法完成正常的抓取，我们可以先用如下代码来测试一下：

import requests
from pyquery import PyQuery as pq
 
url = 'http://quotes.toscrape.com/js/'
response = requests.get(url=url)
doc = pq(response.text)
print('Quotes : {0}'.format(doc('.quote').length))
 
# 结果
# Quotes : 0
这里首先使用 requests 来请求网页内容，然后使用 pyquery 来解析页面中的每一个条目。观察源码之后我们发现每个条目的 class 名为 quote，所以这里选用了 .quote 这个 CSS 选择器来选择，最后输出条目数量。

运行结果：Quotes: 0

结果是 0，这就证明使用 requests 是无法正常抓取到相关数据的。

为什么？

因为这个页面是 JavaScript 渲染而成的，我们所看到的内容都是网页加载后又执行了 JavaScript 之后才呈现出来的，因此这些条目数据并不存在于原始 HTML 代码中，而 requests 仅仅抓取的是原始 HTML 代码。

好的，所以遇到这种类型的网站我们应该怎么办呢？

其实答案有很多：

分析网页源代码数据，如果数据是隐藏在 HTML 中的其他地方，以 JavaScript 变量的形式存在，直接提取就好了。
分析 Ajax，很多数据可能是经过 Ajax 请求时候获取的，所以可以分析其接口。
模拟 JavaScript 渲染过程，直接抓取渲染后的结果。
而 Pyppeteer 和 Selenium 就是用的第三种方法，下面我们再用 Pyppeteer 来试试，如果用 Pyppeteer 实现如上页面的抓取的话，代码就可以写为如下形式：

import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
 
 
async def main():
    browser = await launch()
    page = await browser.newPage()
    url = 'http://quotes.toscrape.com/js/'
    await page.goto(url=url)
    doc = pq(await page.content())
    print('Quotes : {0}'.format(doc('.quote').length))
    await browser.close()
 
asyncio.get_event_loop().run_until_complete(main())
运行结果：Quotes: 10
看运行结果，这说明我们就成功匹配出来了 class 为 quote 的条目，总数为 10 条，具体的内容可以进一步使用 pyquery 解析查看。

那么这里面的过程发生了什么？

实际上，Pyppeteer 整个流程就完成了浏览器的开启、新建页面、页面加载等操作。另外 Pyppeteer 里面进行了异步操作，所以需要配合 async/await 关键词来实现。首先， launch 方法会新建一个 Browser 对象，然后赋值给 browser，然后调用 newPage 方法相当于浏览器中新建了一个选项卡，同时新建了一个 Page 对象。然后 Page 对象调用了 goto 方法就相当于在浏览器中输入了这个 URL，浏览器跳转到了对应的页面进行加载，加载完成之后再调用 content 方法，返回当前浏览器页面的源代码。然后进一步地，我们用 pyquery 进行同样地解析，就可以得到 JavaScript 渲染的结果了。另外其他的一些方法如调用 asyncio 的 get_event_loop 等方法的相关操作则属于 Python 异步 async 相关的内容了，大家如果不熟悉可以了解下 Python 的 async/await 的相关知识。好，通过上面的代码，我们就可以完成 JavaScript 渲染页面的爬取了。

 

模拟网页截图，保存 PDF，执行自定义的 JavaScript 获得特定的内容
接下来我们再看看另外一个例子，这个例子可以模拟网页截图，保存 PDF，另外还可以执行自定义的 JavaScript 获得特定的内容，代码如下：

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
这里我们又用到了几个新的 API，完成了网页截图保存、网页导出 PDF 保存、执行 JavaScript 并返回对应数据。

 evaluate 方法执行了一些 JavaScript，JavaScript 传入的是一个函数，使用 return 方法返回了网页的宽高、像素大小比率三个值，最后得到的是一个 JSON 格式的对象。

总之利用 Pyppeteer 我们可以控制浏览器执行几乎所有动作，想要的操作和功能基本都可以实现，用它来自由地控制爬虫当然就不在话下了。

了解了基本的实例之后，我们再来梳理一下 Pyppeteer 的一些基本和常用操作。Pyppeteer 的几乎所有功能都能在其官方文档的 API Reference 里面找到，链接为：https://miyakogi.github.io/pyppeteer/reference.html，用到哪个方法就来这里查询就好了，参数不必死记硬背，即用即查就好。

 

登录淘宝 （打开网页后，手动输入用户名和密码，可以看到正常跳转到登录后的页面）：

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
 
    await asyncio.sleep(100)
    # await browser.close()
 
asyncio.get_event_loop().run_until_complete(main())
如果把上面 js 去掉，发现淘宝可以检测出来， 跳转不到登录后的页面。

window.navigator 对象包含有关访问者浏览器的信息：https://www.runoob.com/js/js-window-navigator.html

js 主要需要修改浏览器的 window.navigator.webdriver、window.navigator.languages等值。

打开正常的浏览器可以看到：



window.navigator.webdriver的值为undefined，而通过pyppeteer控制打开的浏览器该值为True，当被检测到该值为True的时候，则滑动会一直失败，所以我们需要修改该属性。需要注意，在测试的过程中发现登陆成功后页面的该属性又会变成True，所以在每次重新加载页面后要重新设置该属性的值。

async def page_evaluate(page):
    # 替换淘宝在检测浏览时采集的一些参数
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
 

另一种方法可以进一步免去淘宝登录的烦恼，那就是设置用户目录。

平时我们已经注意到，当我们登录淘宝之后，如果下次再次打开浏览器发现还是登录的状态。这是因为淘宝的一些关键 Cookies 已经保存到本地了，下次登录的时候可以直接读取并保持登录状态。

那么这些信息保存在哪里了呢？其实就是保存在用户目录下了，里面不仅包含了浏览器的基本配置信息，还有一些 Cache、Cookies 等各种信息都在里面，如果我们能在浏览器启动的时候读取这些信息，那么启动的时候就可以恢复一些历史记录甚至一些登录状态信息了。

这也就解决了一个问题：很多朋友在每次启动 Selenium 或 Pyppeteer 的时候总是是一个全新的浏览器，那就是没有设置用户目录，如果设置了它，每次打开就不再是一个全新的浏览器了，它可以恢复之前的历史记录，也可以恢复很多网站的登录信息。

当然可能时间太久了，Cookies 都过期了，那还是需要登录的。

那么这个怎么来做呢？很简单，在启动的时候设置 userDataDir 就好了，示例如下：

 browser = await launch(
        headless=False,
        userDataDir='./userdata',
        args=['--disable-infobars', f'--window-size={width},{height}']
    )
好，这里就是加了一个 userDataDir 的属性，值为 userdata，即当前目录的 userdata 文件夹。我们可以首先运行一下，然后登录一次淘宝，这时候我们同时可以观察到在当前运行目录下又多了一个 userdata 的文件夹：



用户文件夹

具体的介绍可以看官方的一些说明，如：https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md 这里面介绍了 userdatadir 的相关内容。

 

命令行启动 chrome 并进入指定的 URL：chrome.exe --disable-infobars --user-data-dir="./userdatadir" --new-window https://login.taobao.com/member/login.jhtml

执行完后会打开 淘宝的登录页面，登录淘宝，然后保存用户名密码，这样登录信息就保存在 userdatadir 目录下了

在执行 chrome.exe --disable-infobars --user-data-dir="./userdatadir" --new-window https://www.taobao.com

可以看到已经时登录状态了。

 

 

 

示例 2 ：爬取今日头条
# -*- coding: utf-8 -*-
# @Author  : 
# @File    : toutiao.py
# @Software: PyCharm
# @description : XXX
 
 
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
    print(await page.title())    # 打印当前页标题
 
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
 
示例代码2：

import asyncio
from pyppeteer import launch
 
 
async def main():
    # headless参数设为False，则变成有头模式
    browser = await launch(
        # headless=False
    )
 
    page = await browser.newPage()
 
    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})
 
    # 是否启用JS，enabled设为False，则无渲染效果
    await page.setJavaScriptEnabled(enabled=True)
 
    await page.goto('https://www.toutiao.com/')
 
    # 打印页面cookies
    print(await page.cookies())
 
    # 打印页面文本
    print(await page.content())
 
    # 打印当前页标题
    print(await page.title())
 
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
 
    # 关闭浏览器
    await browser.close()
 
 
asyncio.get_event_loop().run_until_complete(main())
 

 百度首页交互
示例代码：

import time
import asyncio
from pyppeteer import launch
 
async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.setViewport({'width': 1200, 'height': 800})
    await page.goto('https://www.baidu.com')
    # 在搜索框中输入python
    await page.type('input#kw.s_ipt','python')
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
 

示例：

import asyncio
import pyppeteer
from collections import namedtuple
 
Response = namedtuple("rs", "title url html cookies headers history status")
 
 
async def get_html(url, timeout=30):
    # 默认30s
    browser = await pyppeteer.launch(headless=True, args=['--no-sandbox'])
    page = await browser.newPage()
    res = await page.goto(url, options={'timeout': int(timeout * 1000)})
    data = await page.content()
    title = await page.title()
    resp_cookies = await page.cookies()
    resp_headers = res.headers
    resp_history = None
    resp_status = res.status
    response = Response(
        title=title,
        url=url,
        html=data,
        cookies=resp_cookies,
        headers=resp_headers,
        history=resp_history,
        status=resp_status
    )
    return response
 
 
if __name__ == '__main__':
    url_list = [
        "http://www.10086.cn/index/tj/index_220_220.html",
        "http://www.10010.com/net5/011/",
        # "http://python.jobbole.com/87541/"
    ]
    task = (get_html(url) for url in url_list)
 
    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(asyncio.gather(*task))
    for res in results:
        print(res.title)


https://blog.csdn.net/freeking101/article/details/93331204