#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))
print(len('dddddddddddd'))

# 切片
s[0], s[-1], s[3:], s[::-1]  # '优', 'n', 'Python', 'nohtyP的雅优'
# 替换，还可以使用正则表达式替换
s.replace('Python', 'Java')  # '学习Java'
# 查找，find()、index()、rfind()、rindex()
s.find('P')  # 3, 返回第一次出现的子串的下标
s.find('h', 2)  # 6, 设定下标2开始查找
s.find('23333')  # -1, 查找不到返回-1
s.index('y')  # 4, 返回第一次出现的子串的下标
s.index('P')  # 不同与find(), 查找不到会抛出异常
# 转大小写, upper()、lower()、swapcase()、capitalize()、istitle()、isupper()、islower()
s.upper()  # '学习PYTHON'
s.swapcase()  # '学习pYTHON', 大小写互换
s.istitle()  # True
s.islower()  # False
# 去空格,strip()、lstrip()、rstrip()
# 格式化
s1 = '%s %s' % ('Windrivder', 21)  # 'Windrivder 21'
s2 = '{}, {}'.format(21, 'Windridver')  # 推荐使用format格式化字符串
s3 = '{0}, {1}, {0}'.format('Windrivder', 21)
s4 = '{name}: {age}'.format(age=21, name='Windrivder')
# 连接与分割，使用 + 连接字符串，每次操作会重新计算、开辟、释放内存，效率很低，所以推荐使用join
l = ['2017', '03', '29', '22:00']
s5 = '-'.join(l)  # '2017-03-29-22:00'
s6 = s5.split('-')  # ['2017', '03', '29', '22:00']

# encode 将字符转换为字节
str = '学习Python'
print(str.encode())  # 默认编码是 UTF-8  输出：b'\xe5\xad\xa6\xe4\xb9\xa0Python'
print(str.encode('gbk'))  # 输出  b'\xd1\xa7\xcf\xb0Python'
# decode 将字节转换为字符
print(str.encode().decode('utf8'))  # 输出 '学习Python'
print(str.encode('gbk').decode('gbk'))  # 输出 '学习Python'

# 字符串拼接 mehon5 直接连接
str_name2 = '33'
print('str_name1' + str_name2)
print('-----------method5-----------')

print('hello''python')

# methon6 format 拼接 str.format(args,**kwargs)
# eg(1) {} 充当占位符
str_word = 'hello, word! {} {}'.format('张三', '李四')
print(str_word)
# eg(2) {[index]} 按索引位置填充 .format([0]=value1, [1]= value1},)
str_word_index0 = 'hell0, word！{0},{1}'.format('张三', '李四')
str_word_index1 = 'hell0, word！{1},{0}'.format('张三', '李四')
print(str_word_index0)
print(str_word_index1)
# eg(3) {[keyword]}
str_word_keyword = 'hell0, word！{a},{b}'.format(b='张三', a='李四')
print(str_word_keyword)
# eg(4) {[keyword,indec]} keyword 放在最后
str_word1 = 'hell0, word！{1}{a}{0},{b}'.format('index0', 'index1', b='张三', a='李四')
print(str_word1)
# eg(5) format 参数类型不限，当为元祖，列表，集合，字典时输出
str_word2 = 'hell0, word！{b}'.format(b=['eee', 'd'])
print(str_word2)
# eg(6) 作为函数使用
str_word3 = 'hello, word! {} {}'.format
word = str_word3('张三', '李四')
print(word)
