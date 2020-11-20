



## 防检测的一些方法 待验证
1、常用小功能
async def init_pyppeteer(self):
        self.browser = await pyppeteer.launch({'headless': False,
                                               # 'userDataDir': './userdata',# 用户临时目录，保存cookie可以开启
                                               'args': [
                                                   # '--window-size={1300},{800}',
                                                   '--start-maximized',  # 最大化窗口
                                                   '--proxy-server=http://118.24.51.247:1443',#浏览器代理 配合某些中间人代理使用
                                                   # '--load-extension={}'.format(chrome_extension),  # 加载插件
                                                   # '--disable-extensions-except={}'.format(chrome_extension),
                                                   # '--disable-extensions',
                                                   '--hide-scrollbars',
                                                   '--disable-bundled-ppapi-flash',
                                                   '--mute-audio',
                                                   '--no-sandbox',  # 取消沙盒模式 沙盒模式下权限太小
                                                   '--no-sandbox',  # 不显示信息栏  比如 chrome正在受到自动测试软件的控制
                                                   '--disable-setuid-sandbox',
                                                   '--disable-gpu',
                                                   '--disable-infobars'
                                                   # log等级设置 在某些不是那么完整的系统里 如果使用默认的日志等级 可能会出现一大堆的warning信息
                                               ],
                                               'dumpio': True,  # 减少内存消耗
                                               # "slowMo": 25  # 让执行慢下来
                                               })
        self.page = await self.browser.newPage()
        width, height = self.screen_size()
        await self.page.setViewport({
            "width": width,
            "height": height
        })
        # 设置浏览器头部
        await self.page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                                     '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')
        await self.page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                         '{ webdriver:{ get: () => false } }) }')  # 本页刷新后值不变
1.1、绕过对方网站监测
import pyppeteer
async def page_evaluate(self, page):
    '''window.navigator.webdriver=false'''
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => undefined } }) }''')  # 以下为插入中间js，将淘宝会为了检测浏览器而调用的js修改其结果。
    await page.evaluate('''() =>{ window.navigator.chrome = { runtime: {},  }; }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'languages', { get: () => ['en-US', 'en'] }); }''')
    await page.evaluate('''() =>{ Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5,6], }); }''')
 
async def main(self):
    browser = await pyppeteer.launch()
    page = await browser.newPage()
    await self.page_evaluate(page)
1.2、网络通信异常处理
 await page.goto(h5_detail_url,waitUntil=["networkidle0", "load", "domcontentloaded"],options={'timeout': 30000})
1.3、禁止渲染
# # 是否启用JS，enabled设为False，则无渲染效果
await self.page.setJavaScriptEnabled(enabled=False)
1.4、等待元素加载
 #waitForSelector 默认为30000（30秒）,为0禁用超时
await self.page.waitForSelector('.shop_list .clearfix span.tit_shop',{'timeout': 9000}) #等待元素加载
await asyncio.sleep(2)
1.5、滚动浏览器
使用js滚动到某个元素

 # 使用js滚动到某个元素
await self.page.evaluate('document.querySelector(".page_al").scrollIntoView();')
滚动到浏览器底部

#滚动到浏览器底部
await self.page.evaluate('window.scrollBy(0, document.body.scrollHeight)')
滚动多少像素

#浏览器向上滚动400个像素
