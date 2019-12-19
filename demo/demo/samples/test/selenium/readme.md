目录
* [Pywin32]()
* [Pywinauto](https://pywinauto.readthedocs.io/en/latest/contents.html) Pywin32升级
* [Pyautogui]() Pyautogui侧重于鼠标、键盘、截图等功能，且是基于图像匹配进行定位的，而Pywinauto侧重与对系统的操作，虽然也有键盘和鼠标的模拟操作，但核心上还是软件上的操作更多。两者各有所长，需根据实际情况选择合适的
* [appium](https://github.com/appium/appium) 手机端

## selenium安装

### chrome
1 https://cdn.npm.taobao.org/dist/chromedriver/2.43/chromedriver_win32.zip  解压到 C:\Program Files (x86)\Google\Chrome\Application
2.python -m pip install selenium

### 其他地址参考
http://selenium-release.storage.googleapis.com/3.13/IEDriverServer_x64_3.13.0.zip
https://github.com/mozilla/geckodriver/releases
https://www.cnblogs.com/du-hong/p/10143393.html

## 目录说明
* [selenium1.py]()  安装和基本测试 截图 遍历元素
* [selenium2_find.py]() find 发现元素用法

## xpath
firepath  https://addons.mozilla.org/zh-CN/firefox/addon/chropath-for-firefox/
ChroPath

find_element_by_xpath("//form[@id='form']/span/input") 2.3 层级与属性结合：
find_element_by_xpath("//input[@id='kw' and @class='su']/span/input")  #2.4 使用逻辑运算符

## 任务
1.总体测试过了一遍，没有全部练习完
2.测试总结，分类目录后续要整理

# Pywin32
Pywin32是一个Python库，为python提供访问Windows API的扩展，提供了齐全的Windows常量、接口、线程以及COM机制等等。这个库里面最重要的三个模块win32api、win32gui和win32con。
查找句柄：窗体是指窗口到文本框的所有控件，每个窗体都有独立的句柄。要操作任意一个窗体，都需要找到这个窗体的句柄。我们可以用win32gui模块中的FindWindow函数和FindWindowEx函数（子窗体函数）来得到指定窗体的句柄。（使用Spy++或Inspect可以很方便地查看目标窗口的窗口名、类名和句柄）

## url
https://selenium-python.readthedocs.io/navigating.html#popup-dialogs
https://github.com/defnngj/book-code/blob/master/appium_project/app_config.py    Selenium3自动化测试实战 基于Python语言书籍 
https://github.com/defnngj/pyrequest  本项目为《Web接口开发与自动化测试--基于Python语言》一书中接口自动化测试项目代码。主要针对发布会签到系统的接口进行测试。 发布会签到系统：http://github.com/defnngj/guest