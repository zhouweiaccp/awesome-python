#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce

'''
reduce(...)
reduce(function, sequence[, initial]) -> value

Apply a function of two arguments cumulatively to the items of a sequence,
from left to right, so as to reduce the sequence to a single value.
For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
((((1+2)+3)+4)+5). If initial is present, it is placed before the items
of the sequence in the calculation, and serves as a default when the
sequence is empty.

从左到右对一个序列的项累计地应用有两个参数的函数，以此合并序列到一个单一值。

例如，reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])  计算的就是((((1+2)+3)+4)+5)。

如果提供了 initial 参数，计算时它将被放在序列的所有项前面，如果序列是空的，它也就是计算的默认结果值了

嗯， 这个文档其实不好理解。看了还是不懂。 序列 其实就是python中 tuple  list  dictionary string  以及其他可迭代物，别的编程语言可能有数组。

reduce 有 三个参数
function	有两个参数的函数， 必需参数
sequence	tuple ，list ，dictionary， string等可迭代物，必需参数
initial	初始值， 可选参数
reduce的工作过程是 ：在迭代sequence(tuple ，list ，dictionary， string等可迭代物)的过程中，首先把 前两个元素传给 函数参数，函数加工后，然后把得到的结果和第三个元素作为两个参数传给函数参数， 函数加工后得到的结果又和第四个元素作为两个参数传给函数参数，依次类推。 如果传入了 initial 值， 那么首先传的就不是 sequence 的第一个和第二个元素，而是 initial值和 第一个元素。经过这样的累计计算之后合并序列到一个单一返回值
'''
CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
