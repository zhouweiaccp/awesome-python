# https://www.cnblogs.com/yang-2018/p/10807667.html
# int(x[, base]) 将x转换为一个整数，base为进制，默认十进制
#
# long(x[, base] ) 将x转换为一个长整数
#
# float(x) 将x转换到一个浮点数
#
# complex(real[, imag])  创建一个复数
#
# str(x) 将对象 x 转换为字符串
#
# repr(x) 将对象 x 转换为表达式字符串
#
# eval(str)  用来计算在字符串中的有效Python表达式, 并返回一个对象
#
# tuple(s) 将序列 s 转换为一个元组
#
# list(s) 将序列 s 转换为一个列表
#
# set(s) 转换为可变集合
#
# dict(d) 创建一个字典。d 必须是一个序列(key, value) 元组。
#
# frozenset(s) 转换为不可变集合
#
# chr(x) 将一个整数转换为一个字符
#
# unichr(x) 将一个整数转换为Unicode字符
#
# ord(x) 将一个字符转换为它的整数值
#
# hex(x) 将一个整数转换为一个十六进制字符串
#
# oct(x)  将一个整数转换为一个八进制字符串

if __name__ == "__main__":
    print(int(1.2))  # 1
    print(int('12', 16))  # 18

    print(float(1))  # 1.0
    print(float('123'))  # 123.0

    # complex() 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
    print(complex(1, 2))  # (1+2j)
    print(complex("1"))  # (1+0j)

    dict1 = {'a': 'b', 'c': 'd'};
    print(type(str(dict1)))  # {'a': 'b', 'c': 'd'} <class 'str'>

    print(eval('pow(2,2)'))  # 4

    print(tuple([1, 2, 3, 4]))  # (1, 2, 3, 4)

    aTuple = (123, 'xyz', 'zara', 'abc');
    print(list(aTuple))  # [123, 'xyz', 'zara', 'abc']

    # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等
    x = set("yangs")
    print(x)  # {'y', 's', 'n', 'a', 'g'}
    print(type(x))  # <class 'set'>
    y = set('yy')
    print(x & y)  # 交集 {'y'}
    print(x | y)  # 并集 {'n', 's', 'g', 'a', 'y'}
    print(x ^ y)  # 非集 {'n', 'g', 'a', 's'}
    print(x - y)  # 差集 {'n', 'g', 's', 'a'}

    print(dict(a='a', b='b', t='t'))  # {'a': 'a', 'b': 'b', 't': 't'}
    print(dict(zip(["a", "b"], ["c", "d"])))  # {'a': 'b', 'c': 'd'}
    print(dict([(1, 2), (3, 4)]))  # {1: 2, 3: 4}

    # frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
    print(frozenset("yangs"))  # frozenset({'s', 'y', 'g', 'n', 'a'})
    print(type(frozenset("yangs")))  # <class 'frozenset'>

    # chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
    print(chr(123))  # {
    print(chr(48))  # '0'

    print(ord('a'))  # 97
    print(ord('0'))  # 48

    # 将10进制整数转换成16进制，以字符串形式表示
    print(hex(255))  # 0xff
    print(hex(0))  # 0x0

    # 将一个整数转换成8进制字符串
    print(oct(10))  # 0o12