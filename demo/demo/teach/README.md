# 安装Python学习助手

首先确认Python 3.4已安装。

# 下载learning.py

下载地址：

[https://raw.githubusercontent.com/michaelliao/learn-python3/master/teach/learning.py](https://raw.githubusercontent.com/michaelliao/learn-python3/master/teach/learning.py)

(右键 - 另存为)

放到某个目录，例如`C:\Work`下。

# 运行命令：

切换到`learning.py`所在目录，运行：

```
C:\Work> python learning.py
```

如果看到`Ready for Python code on port 39093...`表示运行成功，不要关闭命令行窗口，最小化放到后台运行即可。
https://www.liaoxuefeng.com/wiki/1016959663602400/1017454145929440
![run-learning.py.png](https://raw.githubusercontent.com/michaelliao/learn-python3/master/teach/run-learning.py.png)




## 语法


### 调用函数时使用* **
test(*args)* 的作用其实就是把序列 args 中的每个元素，当作位置参数传进去。比如上面这个代码，如果 args 等于 (1,2,3) ，那么这个代码就等价于 test(1, 2, 3) 。
test(**kwargs)** 的作用则是把字典 kwargs 变成关键字参数传递。比如上面这个代码，如果 kwargs 等于 {'a':1,'b':2,'c':3} ，那这个代码就等价于 test(a=1,b=2,c=3) 



## 目录
├─advance
├─async
├─basic       基本语法 if for input print  dict list set string tuple 字符串操作
              py_conver.py 类型转换 

├─commonlib   第三库 
            use_logbook.py logbook 应用
            user_logging_coloredlogs 日志带颜色
├─commonlib\commonlib\use_datetime.py  时间处理
├─context
├─db
├─debug
    do_logging 日志
├─devops  自动化运维
├─function
├─functional  functools，用于高阶函数：指那些作用于函数或者返回其它函数的函数，Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
├─gui
│  └─turtle
├─io
    use_json use_pickle  json对象处理
├─mail
├─module
       sys_cmd 系统命令
├─multitask
├─oop_advance 面向对象高级编程 __slots__ [限制属性] @property
├─oop_basic  面向对象编程 【类  多态 继承  实例
├─packages
│  └─pil
├─regex
├─socket
├─test
    └─appium 手机测试
    └─selenium 浏览器测试
└─web
    └─mvc
        └─templates
