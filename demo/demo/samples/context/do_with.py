#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
with 语句实质是上下文管理。
1、上下文管理协议。包含方法__enter__() 和 __exit__()，支持该协议对象要实现这两个方法。
2、上下文管理器，定义执行with语句时要建立的运行时上下文，负责执行with语句块上下文中的进入与退出操作。
3、进入上下文的时候执行__enter__方法，如果设置as var语句，var变量接受__enter__()方法返回值。
4、如果运行时发生了异常，就退出上下文管理器。调用管理器__exit__方法。
"""

# 作者：skullfang
# 链接：<a href='https://www.jianshu.com/p/5b01fb36fd4c'>https://www.jianshu.com/p/5b01fb36fd4c</a>

from contextlib import contextmanager

@contextmanager
def log(name):
    print('[%s] start...' % name)
    yield
    print('[%s] end.' % name)

with log('DEBUG'):
    print('Hello, world!')
    print('Hello, Python!')
