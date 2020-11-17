
#url可以是字符串  https://www.cnblogs.com/qikeyishu/p/10748497.html
import urllib.request, urllib.parse
resp = urllib.request.urlopen('http://www.baidu.com')
print(resp.read().decode('utf-8'))  # read()获取响应体的内容，内容是bytes字节流，需要转换成字符串
##url可以也是Request对象
# import urllib.request

# request = urllib.request.Request('http://httpbin.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# data参数：post请求
# coding:utf8


data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
resp = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(resp.read())

# urlopen()中的参数timeout：设置请求超时时间：
# coding:utf8
#设置请求超时时间
# resp = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# print(resp.read().decode('utf-8'))









proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
# This time, rather than install the OpenerDirector, we use it directly:
resp = opener.open('http://www.example.com/login.html')
print(resp.read())


try:
    resp = urllib.request.urlopen('http://www.blueflags.cn')
except urllib.error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except urllib.error.URLError as e:
    print(e.reason)



# url = 'http://httpbin.org/post'
# headers = {
#     'Host': 'httpbin.org',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
# }
# dict = {'name': 'Germey'}
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))



# url = 'http://httpbin.org/post'
# dict = {'name': 'Thanlon'}
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent',
#                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')
# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))



# 3、url解析模块：urllib.parse
# parse.urlencode
# coding:utf8
from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'Host': 'httpbin.org',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
dict = {'name': 'Germey'}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
{
"args": {},
"data": "",
"files": {},
"form": {
"name": "Thanlon"
},
"headers": {
"Accept-Encoding": "identity",
"Content-Length": "12",
"Content-Type": "application/x-www-form-urlencoded",
"Host": "httpbin.org",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
},
"json": null,
"origin": "117.136.78.194, 117.136.78.194",
"url": "https://httpbin.org/post"
}

# 3 add_header方法添加请求头：
# # coding:utf8
# from urllib import request, parse

# url = 'http://httpbin.org/post'
# dict = {'name': 'Thanlon'}
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, method='POST')
# req.add_header('User-Agent',
#                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36')
# resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
# parse.urlparse：
# # coding:utf8
# from urllib.parse import urlparse

# result = urlparse('http://www.baidu.com/index.html;user?id=1#comment')
# print(type(result))
# print(result)
# <class 'urllib.parse.ParseResult'>
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=1', fragment='comment')

# from urllib.parse import urlparse

# result = urlparse('www.baidu.com/index.html;user?id=1#comment', scheme='https')
# print(type(result))
# print(result)
# <class 'urllib.parse.ParseResult'>
# ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='user', query='id=1', fragment='comment')

# # coding:utf8
# from urllib.parse import urlparse

# result = urlparse('http://www.baidu.com/index.html;user?id=1#comment', scheme='https')
# print(result)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=1', fragment='comment')

# # coding:utf8
# from urllib.parse import urlparse

# result = urlparse('http://www.baidu.com/index.html;user?id=1#comment',allow_fragments=False)
# print(result)
# ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=1', fragment='comment')

# parse.urlunparse：
# # coding:utf8
# from urllib.parse import urlunparse

# data = ['http', 'www.baidu.com', 'index.html', 'user', 'name=Thanlon', 'comment']
# print(urlunparse(data))
# 在这里插入图片描述

# parse.urljoin：
# # coding:utf8
# from urllib.parse import urljoin

# print(urljoin('http://www.bai.com', 'index.html'))
# print(urljoin('http://www.baicu.com', 'https://www.thanlon.cn/index.html'))#以后面为基准
# 在这里插入图片描述

# urlencode将字典对象转换成get请求的参数:
# # coding:utf8
# from urllib.parse import urlencode

# params = {
#     'name': 'Thanlon',
#     'age': 22
# }
# baseUrl = 'http://www.thanlon.cn?'
# url = baseUrl + urlencode(params)
# print(url)



















# 4、Cookie
# cookie的获取(保持登录会话信息)：
# # coding:utf8
# #cookie的获取(保持登录会话信息)
# import urllib.request, http.cookiejar

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + '=' + item.value)
# 在这里插入图片描述

# MozillaCookieJar(filename)形式保存cookie
# # coding:utf8
# #将cookie保存为cookie.txt
# import http.cookiejar, urllib.request

# filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)
# LWPCookieJar(filename)形式保存cookie：
# # coding:utf8
# import http.cookiejar, urllib.request

# filename = 'cookie.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# res = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)
# 读取cookie请求，获取登陆后的信息
# # coding:utf8
# import http.cookiejar, urllib.request

# cookie = http.cookiejar.LWPCookieJar()
# cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# resp = opener.open('http://www.baidu.com')
# print(resp.read().decode('utf-8'))