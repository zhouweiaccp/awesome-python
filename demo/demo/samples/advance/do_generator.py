#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'zw'
# s = (x * x for x in range(5))
# print(s)
# for x in s:
#     print(x)
'''public
int
RecUrsive(int
index)

{

if (index < 3) // 若index的值等于1或2，则返回1

{

return 1;

}

else

{

return RecUrsive(index - 1) + RecUrsive(index - 2);
}
}
'''
print('def fib(max):斐波那契数列 https://blog.csdn.net/duanworld/article/details/68489796')
'''
https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128
注意，赋值语句：
a, b = b, a + b
相当于：
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
'''


def fib(max):
    n, a, b = 0, 0, 1
    print('1---n:{0},a:{1},b:{2},max:{3}'.format(n, a, b, max))
    while n < max:
        yield b
        print('2-0---n:{0},a:{1},b:{2},max:{3}'.format(n, a, b, max))
        a, b = b, a + b
        print('2-1---n:{0},a:{1},b:{2},max:{3}'.format(n, a, b, max))
        n = n + 1
    return 'done'


f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
