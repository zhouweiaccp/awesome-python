


### link
- [](https://github.com/microsoft/playwright-python)它支持主流的浏览器，包含：Chrome、Firefox、Safari、Microsoft Edge 等，同时支持以无头模式、有头模式运行，并提供了同步、异步的 API，可以结合 Pytest 测试框架使用，并且支持浏览器端的自动化脚本录制
- [](https://www.cnblogs.com/jinjiangongzuoshi/p/14154605.html)



pip3 install playwright
python3 -m playwright codegen --target python -o 'mikezhou.py' -b chromium https://www.baidu.com  录制脚本
python -m playwright help   帮助


















## code1 
```python
from time import sleep
from playwright import sync_playwright

# 注意：默认是无头模式
with sync_playwright() as p:
    # 分别对应三个浏览器驱动
    for browser_type in [p.chromium, p.firefox, p.webkit]:

        # 指定为有头模式，方便查看
        browser = browser_type.launch(headless=False)
        page = browser.newPage()
        page.goto('http://baidu.com')

        # 执行一次搜索操作
        page.fill("input[name=\"wd\"]", "自动化测试实战宝典")
        with page.expect_navigation():
            page.press("input[name=\"wd\"]", "Enter")

        # 等待页面加载完全
        page.waitForSelector("text=搜索工具")
        
        # 截图
        page.screenshot(path=f'test-{browser_type.name}.png')

        # 休眠3s
        sleep(3)

        # 关闭浏览器
        browser.close()
```


```python
import asyncio
from playwright import async_playwright

# 异步执行
async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            # 指定为有头模式，方便查看
            browser = await browser_type.launch(headless=False)
            page = await browser.newPage()

            await page.goto('http://baidu.com')

            # 执行一次搜索操作
            await page.fill("input[name=\"wd\"]", "自动化测试实战宝典")
            await page.press("input[name=\"wd\"]", "Enter")

            # 等待页面加载完全
            await page.waitForSelector("text=搜索工具")

            # 截图
            await page.screenshot(path=f'test-{browser_type.name}.png')
            await browser.close()

asyncio.get_event_loop().run_until_complete(main())
```