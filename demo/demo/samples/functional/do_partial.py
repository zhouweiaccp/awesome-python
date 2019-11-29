#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
# functools.partial(func, *args, **keywords)，函数装饰器，返回一个新的partial对象。调用partial对象和调用被修饰的函数func相同，只不过调用partial对象时传入的参数个数通常要少于调用func时传入的参数个数。当一个函数func可以接收很多参数，而某一次使用只需要更改其中的一部分参数，其他的参数都保持不变时，partial对象就可以将这些不变的对象冻结起来，这样调用partial对象时传入未冻结的参数，partial对象调用func时连同已经被冻结的参数一同传给func函数，从而可以简化调用过程。
#
# 如果调用partial对象时提供了更多的参数，那么他们会被添加到args的后面，如果提供了更多的关键字参数，那么它们将扩展或者覆盖已经冻结的关键字参数。
int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))
