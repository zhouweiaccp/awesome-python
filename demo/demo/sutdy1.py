# -*- coding: UTF-8 -*-
#!/usr/bin/ python3
# def my_function():
#     for i in range(10):
#         print ( i )
#
# my_function()

# def my_function():
#     for i in range(10):
#         yield i
#
# print(my_function())

# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b
#
# # 引用函数
# for x in fibon(1000000):
#     print(x , end = ' ')

#https://www.readwithu.com/Article/PythonBasis/python7/4.html
def triangles( n ):# 杨辉三角形
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [ L [ i -1 ] + L [ i ] for i in range (len(L))]

n= 0
for t in triangles( 10 ):   # 直接修改函数名即可运行
    print(t)
    n = n + 1
    if n == 10:
        break

list1 = [1,2,3,4,5]
for num1 in list1 :
    print ( num1 , end = ' ' )