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

## Selenium2 Python自动化测试实战
[](F:\Program Files\Tencent\584936909\FileRecv\Selenium2 Python自动化测试实战（第二版）.pdf)

### Selenium2 find_element
1. find_element_by_id()   <div id="123">aa</div>
2. find_element_by_name()   <input type="text" name="aa123"/>
3. find_element_by_class_name() <input type="text" class="aa123"/>
4. find_element_by_tag_name("inpute")  <input type="text" name="aa123"/>
5. find_element_by_link_text("wwxxx")   <a href="ww">wwxxx</a>
6. find_element_by_partial_link_text("ww") <a href="ww">wwxxx</a>
7. find_element_by_xpath()
8. find_element_by_css_selector(".bg s_btn")

find_element(By.ID,"kw")
find_element(By.NAME,"wd")
find_element(By.CLASS_NAME,"s_ipt")
find_element(By.TAG_NAME,"input")
find_element(By.LINK_TEXT,u"新闻")
find_element(By.PARTIAL_LINK_TEXT,u"新")
find_element(By.XPATH,"//*[@class='bg s_btn']")
find_element(By.CSS_SELECTOR,"span.bg s_btn_wr>input#su")

### 鼠标事件
 ActionChains 中存储的行为
 context_click() 右击
 double_click() 双击
 drag_and_drop() 拖动
 move_to_element() 鼠标悬停

from selenium import webdriver
#引入 ActionChains 类
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("http://yunpan.360.cn")
....
#定位到要右击的元素
right_click =driver.find_element_by_id("xx")
#对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right_click).perform()

#执行元素的拖放操作
ActionChains(driver).drag_and_drop(element,target).perform()

#对定位到的元素执行双击操作
ActionChains(driver).double_click(double_click).perform()


### 等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
element = WebDriverWait(driver,5,0.5).until(
EC.presence_of_element_located((By.ID,"kw"))
)
element.send_keys('selenium')
driver.quit()

### 隐式等待
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait《Selenium2 Python 自动化测试实战》样张
85
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
input_ = driver.find_element_by_id("kw22")
input_.send_keys('selenium')
driver.quit()


###  4.9 多表单切换
from selenium import webdriver
import time
import os
driver = webdriver.Firefox()
file_path = 'file:///' + os.path.abspath('frame.html')
driver.get(file_path)
#切换到 iframe（id = "if"）
driver.switch_to_frame("if")
#下面就可以正常的操作元素了
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit(

### 4.10 多窗口切换
from selenium import webdriver
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
#获得百度搜索窗口句柄
sreach_windows= driver.current_window_handle
driver.find_element_by_link_text(u'登录').click()
driver.find_element_by_link_text(u"立即注册").click()《Selenium2 Python 自动化测试实战》样张
93
#获得当前所有打开的窗口的句柄
all_handles = driver.window_handles
#进入注册窗口
for handle in all_handles:
if handle != sreach_windows:
driver.switch_to_window(handle)
print 'now register window!'
driver.find_element_by_name("account").send_keys('username')
driver.find_element_by_name('password').send_keys('password')
#……
#进入搜索窗口
for handle in all_handles:
if handle == sreach_windows:
driver.switch_to_window(handle)
print 'now sreach window!'
driver.find_element_by_id('TANGRAM__PSP_2__closeBtn').click()
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit(
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