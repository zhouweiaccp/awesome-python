#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#coding=utf-8
#python+selenium  百度贴吧群发(模拟人工发送 不删帖)  日发帖2W条
#QQ29295842   欢迎交流  博客园   搜狐  CSDN 知乎  各种BLOG群发
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
import time
import random
import re
import json
import io
os_path=""

chrome_file=""
chrome_chromedriver=""
title=[]
content=[]
lm=[]
Cookie={}
data_index=0      #m每次运行发布总数
open_sleep=0  #登录等待多长时间在发布
lm_sleep=0  #发布完成发布下个延时
open_tb=0    #打开贴吧延时
title_sleep=0    #标题输入完成延时
content_sleep=0   #输入内容完成  点击发布延时


def get_path():
    global chrome_file,chrome_chromedriver
    #chrome_file = os_path + "\\Chrome\\chrome.exe"
    chrome_file = os_path + "\\Chrome\\chrome.exe"
    chrome_file = chrome_file.replace("\\", "\\\\")
    print(chrome_file)
    chrome_chromedriver = os_path + "\\Chrome\\chromedriver.exe"
    chrome_chromedriver = chrome_chromedriver.replace("\\", "\\\\")


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def init_google(url):
    # 检测谷歌是否开启
    # 杀掉谷歌进程
    # os.system("taskkill /F /IM chrome.exe")
    # 开启谷歌
    try:
        os.environ["webdriver.chrome.driver"] = chrome_chromedriver
        options = webdriver.ChromeOptions()
        options.binary_location = r"%s" % (chrome_file)
        options.add_argument('disable-infobars')
        # prefs = {"--disable-bundled-ppapi-flash": 2}
        options.add_argument("--disable-bundled-ppapi-flash")  # 禁止加载FLSH
        options.add_argument("--disable-internal-flash")  # 禁止加载FLSH
        options.add_argument("--disable-flash-core-animation")  #
        browser = webdriver.Chrome(executable_path=chrome_chromedriver, chrome_options=options)
        #browser.maximize_window()  # 浏览器全屏显示
        browser.get(url)
        if os.path.exists('cookies.json'):
            browser.delete_all_cookies()
            with io.open('cookies.json', 'r', encoding='utf-8') as f:
                listCookies = json.loads(f.read())
                for cookie in listCookies:
                    browser.add_cookie({
                        'domain': cookie['domain'],
                        'name': cookie['name'],
                        'value': cookie['value'],
                        'path': '/',
                        'expires': None
                    })
            browser.get(url)


        # cookies = {"name": "BDUSS", "value": BDUSS}
        # cookies2 = {"name": "STOKEN", "value": STOKEN}
        # browser.add_cookie(cookie_dict=cookies)
        # browser.add_cookie(cookie_dict=cookies2)
        # browser.get(url) #刷新页面

        print (u"浏览器成功初始化完毕....")
        return 1,browser
    except:
        return 0, ""

def  if_user(browser):
    try:
        user_elements = browser.find_elements_by_xpath(".//*[@id='j_u_username']/div[1]/a/span")  #.//*[@id='j_u_username']/div[1]/a
        if len(user_elements):
            if user_elements[0].is_displayed():
                cookies = browser.get_cookies()
                jsonCookies = json.dumps(cookies)
                with open('cookies.json', 'w') as f:
                    f.write(jsonCookies)
                print u"登录成功"
                return 1
        print u"登录失败"
        return 0
    except:
         return 0

def gz(url,browser):   #一键关注
    # user_elements = browser.find_elements_by_xpath(".//*[@id='forum_recommend']/span/a[1]")
    # if len(user_elements):
    #     if user_elements[0].is_displayed():
    try:
        browser.find_element_by_xpath(".//*[@id='j_head_focus_btn']").click()
        browser.find_element_by_xpath("html/body/div[9]/div/div[3]/input").click()
        browser.get(url)  # 刷新页面
    except:
        pass

def public_randint(x,s): #抽取随机数
    try:
        return random.randint(x,s)
    except:
        return 1

def key_Break(str):  #KEY  关键字词拆分
    try:
        x=0
        key_list = []
        for i in range(0, len(str.decode('utf-8'))):
            if x<=i:
                x2=x+public_randint(2,3)
                key_list.append(str.decode('utf-8')[x:x2].encode('utf-8'))  # 添加数据
                x=x2
        return key_list
    except:
        return []

def ft(url,browser,titlex, contentx):   #发帖
    try:
        browser.get(url)  # 刷新页面
        time.sleep(int(open_tb))
        #browser.find_element_by_xpath('.//*[@id="tb_rich_poster"]/div[3]/div[1]/div[2]/input').click()
        title_list = key_Break(titlex)
        for title_s in title_list:
            browser.find_element_by_xpath('.//*[@id="tb_rich_poster"]/div[3]/div[1]/div[2]/input').send_keys(u"%s"%(title_s))
            time.sleep(1)
        time.sleep(int(title_sleep))
        content_list = key_Break(contentx)
        for content_s in content_list:
            browser.find_element_by_xpath('.//*[@id="ueditor_replace"]').send_keys(u"%s"%(content_s))
            time.sleep(1)
            # x = public_randint(0, 100)
            # if x <= 8:
            #     for i in range(0, len(title_s)):
            #         time.sleep(0.5)
            #         browser.find_element_by_xpath('.//*[@id="ueditor_replace"]').send_keys(Keys.BACK_SPACE)  # 删除
            #     time.sleep(1)
            #     browser.find_element_by_xpath('.//*[@id="ueditor_replace"]').send_keys(u"%s" % (title_s))

        time.sleep(int(content_sleep))
        browser.find_element_by_xpath('.//*[@id="tb_rich_poster"]/div[3]/div[5]/div/button[1]').click()
        return 1
    except:
        return 0

def get_url(browser,title):
    try:
        # ss = browser.find_elements_by_xpath('.//*[@id="thread_list"]/li[1]/div/div[2]/div[1]/div[1]/a')
        # if len(ss):
        #     # print(ss[0].get_attribute('href'))
        #     # print(ss[0].get_attribute('title'))
        #     if {}
        browser.refresh()
        for i in range(1, 6):
            # print i
            try:
                ss = browser.find_elements_by_xpath('.//*[@id="thread_list"]/li['+str(i)+']/div/div[2]/div[1]/div[1]/a')
                if len(ss):
                    # print ss[0].get_attribute('title')
                    if ss[0].get_attribute('title')==title:
                        return 1,ss[0].get_attribute('href')
            except Exception, e:
                pass
        return 0, ""
    except Exception, e:
        print e
        return 0,""

def TXT_file2(file_nem,data):  #写入文本 中文
    try:
        #file_nem=time.strftime('%Y.%m.%d')   #file_nem+".txt"
        file_object = open(u"%s"%(file_nem),'a')
        file_object.write(data.encode("utf-8")) #成功
        file_object.writelines("\n")
        file_object.close()
        # send_data = u"###########################%s %s###########################" % (str(file_nem), str(data))
        # print send_data
    except Exception,e:
        print u"写入TXT失败",file_nem,data,e
        return 0

def clear(text_path):   #清空数据
    try:
        with open(text_path, 'r+') as file:
            file.truncate(0)
    except Exception, e:
        print u"清空数据失败   %s"%(text_path)
        pass



import ConfigParser  #INI读取数据
def open_txt_ini():
    try:
        f = open("title.txt", "r")
        lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
        for line in lines:
            if len(line)>=3:
                title.append(line.replace("\n", ""))
        f.close()
    except:
        pass
    try:
        f = open("content.txt", "r")
        lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
        for line in lines:
            if len(line)>=3:
                content.append(line.replace("\n", ""))
        f.close()
    except:
        pass
    try:
        f = open("lm.txt", "r")
        lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
        for line in lines:
            if len(line)>=3:
                lm.append(line.replace("\n", ""))
        f.close()
    except:
        pass
    try:
        f = open("Cookie.txt", "r")
        lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
        for line in lines:
            if len(line)>=3:
                try:
                    ss=line.replace("\n", "")
                    mes_to_dict = eval(ss)
                    Cookie[mes_to_dict['BDUSS']]= mes_to_dict['STOKEN']
                except:
                    pass
        f.close()
    except:
        pass
    try:
        # proDir = os.path.split(os.path.realpath(__file__))[0]    # 在当前文件路径下查找.ini文件
        # configPath = os.path.join(proDir, "teiba.ini")
        # print(configPath)
        # import configparser
        # conf = configparser.ConfigParser()  # 读取.ini文件
        # conf.read(configPath)
        # lm_sleep=conf.get('teiba', 'lm_sleep')
        global lm_sleep,open_tb,title_sleep,content_sleep,open_sleep,data_index
        INI_config = ConfigParser.ConfigParser()
        INI_config.readfp(open("teiba.ini"))
        data_index = INI_config.get('teiba', 'data_index')  # # m每次运行发布总数
        open_sleep = INI_config.get('teiba', 'open_sleep')  # 登录等待多长时间在发布
        lm_sleep = INI_config.get('teiba', 'lm_sleep')  #发布完成发布下个延时
        open_tb = INI_config.get('teiba', 'open_tb')   #打开贴吧延时
        title_sleep = INI_config.get('teiba', 'title_sleep')   #标题输入完成延时
        content_sleep = INI_config.get('teiba', 'content_sleep')  #输入内容完成  点击发布延时
    except:
        pass


def if_id(contentx):
    try:
        colours = ["jycg789", "15516190823", "29295842","jycg7⑧9","wuyouhuoke01","15505151927"]
        for colour in colours:
            if len(re.findall(colour, contentx)) >= 1:
                return 1
        return 0
    except:
        return 0

def get_content():
    try:
        random.shuffle(title)
        random.shuffle(content)
        contentx=content[0]
        if if_id(contentx):
            if len(re.findall("jycg789", contentx)) >= 1:
                return 1,title[0],contentx
            else:
                if random.randint(0, 200)<5:
                    return 1, title[0], contentx + title[0] + u" (V:jycg789)"
            return 1, title[0], contentx
        else:
            return 1,title[0], contentx+title[0]+u" 中原大数据(V:jycg789)"
    except:
        return 0,"",""

def get_Cookie():
    # a = random.sample(Cookie.keys(), 1)
    # print (Cookie[a])
    try:
        if len(Cookie):
            a = random.choice(list(Cookie.keys()))
            return 1,a,Cookie[a]
        return 0, "", ""
    except:
        return 0,"",""

import getpass
if __name__ == '__main__':
    #os_path = str(sys.path[0])  # 记录当前路径   调试使用
    os_path = os.path.dirname(sys.executable)#str(sys.path[0])   #记录当前路径  编译使用
    get_path()
    open_txt_ini()
    clear("err.txt")  # 清空数据
    random.shuffle(lm)  #栏目
    # bool,titlex,contentx=get_content()
    # print titlex,contentx
    # print len(title)

    # except_key = public_def.random_str(public_def.public_randint(2, 5))
    # bool,BDUSS,STOKEN=get_Cookie()
    # print bool,BDUSS,STOKEN

    print u"QQ:29295842  百度贴吧群发专用  2020.10.27"
    url="https://tieba.baidu.com/index.html"
    bool,browser=init_google(url)
    if bool==0:
        print u"打开失败请重新运行程序"
        time.sleep(130)
    while 1:
        print u"用户登录完成后请输入1进行群发："
        pwd = int(input())
        if pwd==1:
            if if_user(browser):
                break  # 跳出
            else:
                print u"未检测到登录"

    print u"等待%s秒  开始群发"%(open_sleep)
    time.sleep(int(open_sleep))
    while 1:
        for lm_colour in lm:
            try:
                print "=========================================="
                print u"本次发布任务还有   %s  条需要发布"%(data_index)
                if data_index<=1:
                    print u"发布完成"
                    time.sleep(10)
                    break  # 跳出
                try:
                    url = u"https://tieba.baidu.com/f?kw=%s" % (lm_colour)
                    print url
                    browser.get(url)
                except:
                    pass
                bool, titlex, contentx = get_content()
                if bool==0:
                    print u"获取内容失败"
                    #browser.quit()  # 关闭浏览器
                    time.sleep(1)
                    continue  # 跳过
                #gz(url, browser)  # 一键关注
                bool=ft(url, browser,titlex, contentx)  # 发帖
                if bool==0:
                    print u"发帖失败"
                    #browser.quit()  # 关闭浏览器
                    continue  # 跳过
                time.sleep(5)
                #//*[@id="TANGRAM__2__header_h3"]
                bool, href = get_url(browser, titlex)
                if bool == 0:
                    print u"未找到链接"
                    if lm_sleep<3000:
                        lm_sleep=lm_sleep+lm_sleep
                else:
                    data_index=data_index-1
                    print u"发帖成功  %s" % (href)
                    data_txt=u"%s,%s,%s"%(href,titlex, contentx)
                    TXT_file2("teiba_ok_url.csv", data_txt)  # 写入文本 中文
                time.sleep(3)
                #browser.quit()  # 关闭浏览器
                print u"等待%s秒发送下一条"%(str(lm_sleep))
                time.sleep(int(lm_sleep))
            except:
                print u"异常 等待%s秒发送下一条" % (str(lm_sleep))
                time.sleep(int(lm_sleep))
                pass






    # BDUSS="XgwTS00S0lkcm1BVlljdUFac29UODFMRXdZVkpwM3ZwNVMweXJZV2pZNnhmUFBJCQAAAAAAAAAAAEAAABSgP0BQUxBTE1OwLa6~AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALHvTV-x701fM"
    # STOKEN="9e4c97cbcb19943082b58ff4327915fce517fc76a4b5bf245f7812d3e3a6c8a1"
    # url="https://tieba.baidu.com/f?kw=网络营销培训"
    # bool,browser=init_google(url, BDUSS,STOKEN)
    # if bool==0:
    #     print u"登录失败"
    # else:
    #     # gz(url,browser)  # 一键关注
    #     #ft(url, browser)  # 发帖
    #     bool,href=get_url(browser, u"花了3 、4 千买来的网络营销资料")
    #     if bool:
    #         print u"发帖成功  %s"%(href)
    #         TXT_file2("teiba_ok_url.txt", href)  # 写入文本 中文
    #
    # while 1:
    #     time.sleep(2)
    # # self.browser.quit()  # 关闭浏览器
