#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo - 当前Project名称;
# use_builtins - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2019 / 10 / 29 - 当前系统日期;
import builtins

# 作用域的概述及运用
global_scope = 0  # 全局作用域

# 定义闭包函数中的局部作用域
def outer():
    o_count = 1  # 闭包函数外的函数中，相对于函数 inner() 来说 作用域非局部
    def inner():
       local_scope = 2  # 局部作用域

# 查看模块中引入哪些变量
print('builtins 模块中引入的变量为：%s' %dir(builtins))

# dir(__builtins__)
#https://www.cnblogs.com/Ladylittleleaf/p/10240096.html
#         不管怎么说，在启动Python解释器或运行一个Python程序时，内建名称空间都是从__builtins__模块中加载的，只是__builtins__本身是对Python内建模块__builtin__的引用，而这种引用又分下面两种情况：
#
# 如果是在主模块__main__中，__builtins__直接引用__builtin__模块，此时模块名__builtins__与模块名__builtin__指向的都是同一个模块，即<builtin>内建模块（这里要注意变量名和对象本身的区别）
#
# 如果不是在主模块中，那么__builtins__只是引用了__builtin__.__dict__