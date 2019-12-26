#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
# date:2019/12/26

__author__ = 'xxx'
try:
    import psutil
except ImportError:
    print('错误: psutil模块没有发现!')
    exit()
import platform
import datetime
import time
# pip install psutil
# psutil模块
# psutil模块是什么？
#https://www.cnblogs.com/sss4/p/9869464.html python 运维常用模块
# psutil可以跨平台获取系统运行的进程和系统利用率（CP、内存、硬盘、网络信息的python扩展库），跨平台这就意味着Windows系统主机的信息也可以被采集到！
#
# 一专多能：实现了ps、top、lsof、netstat、ifconfig、who、df、kill、free、nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等命令工具的功能；
def get_osinfo():
    """获取操作系统相关信息"""
    osType = platform.system()
    osVersion = platform.version()
    osArchitecture = platform.architecture()
    hostName = platform.node()
    return osType, osVersion, osArchitecture, hostName


def get_processor():
    """获取物理CPU个数"""
    return psutil.cpu_count(logical=False)


def get_cores():
    '''获取逻辑CPU个数'''
    return psutil.cpu_count()


def get_boot_time():
    '''获取开机时间'''
    return datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")


def get_disk_root():
    '''获取根分区磁盘空间'''
    return psutil.disk_usage('D:')


def get_mem_total():
    '''获取内存容量'''
    return psutil.virtual_memory()[0] / 1024 / 1024


def get_mem_free():
    '''获取可用内存大小'''
    return psutil.virtual_memory()[4] / 1024 / 1024


def get_key():
    '''函数获取各网卡发送、接收字节数'''

    key_info = psutil.net_io_counters(pernic=True).keys()  # 获取网卡名称

    recv = {}
    sent = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(
            pernic=True).get(key).bytes_recv)  # 各网卡接收的字节数
        sent.setdefault(key, psutil.net_io_counters(
            pernic=True).get(key).bytes_sent)  # 各网卡发送的字节数

    return key_info, recv, sent


def get_rate(func):
    '''函数计算每1秒网卡速率'''
    key_info, old_recv, old_sent = func()  # 上1秒收集的数据

    time.sleep(1)

    key_info, now_recv, now_sent = func()  # 当前所收集的数据

    net_in = {}
    net_out = {}

    for key in key_info:
        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)  # 每秒接收速率
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024)  # 每秒发送速率

    return key_info, net_in, net_out


def main():
    '''程序入口函数'''
    ostype, osversion, osarchitecture, hostname = get_osinfo()

    print('操作系统类型:', ostype)
    print('操作系统版本:', osversion)
    print('操作系统位数:', osarchitecture[0])
    print('主机名:', hostname)
    print('物理CPU个数:', get_processor())
    print('逻辑CPU个数:', get_cores())
    print('开机时间:', get_boot_time())
    print('根分区可用空间(单位为MB):', get_disk_root()[2] / 1024 / 1024)
    print('内存总量(单位为MB):', get_mem_total())
    print('可用内存大小(单位为MB):', get_mem_free())

    i = 0
    while i < 3:  # 去获取每秒每块网卡的 速率
        key_info, net_in, net_out = get_rate(get_key)
        for key in key_info:
            print('%s\nInput:\t %-5sKB/s\nOutput:\t %-5sKB/s\n' %
                  (key, net_in.get(key), net_out.get(key)))
        i += 1


if __name__ == '__main__':
    main()

# 获取本机的基本信息和 3秒的网卡速率

#
# 查看系统中所有运行的进程
#
# 复制代码
# import psutil
# pid_list=psutil.pids() #获取当前系统进程ID列表
# for i in pid_list:
#     p=psutil.Process(i)
#     print('我是进程:{0},我的进程ID:{1} 俺爹的进程ID:{2}'.format(p.name(),str(p.pid),str(p.ppid()  )))#获取所有进程的名称
#
# pidList = psutil.pids()
# for pid in pidList:       #查看系统中进行的相关信息
#     proc = psutil.Process(pid)
#     pidDictionary=proc.as_dict(attrs=['pid', 'name', 'username', 'exe', 'create_time', 'status', 'num_threads'])#获取所有进程的相关信息以字典显示
#     tempText = ''
#     for keys in pidDictionary.keys():
#         tempText += keys + ':' + str(pidDictionary[keys]) + '\n'
#         print(tempText)
#         print('*********************\n')
#
# 复制代码
# 查看单个进程的详细信息
#
# 复制代码
# p = psutil.Process(pid=7160)
# print(p.exe())           #获取进程的工作目录
# print(p.cwd())           #获取进程的工作目录的绝对路径
# print(p.cpu_times())     #c查看进程CPU时间信息
# print(p.cpu_affinity())  #查看CPU占用情况
# print(p.username())            #开启该进程的用户
# print(p.num_threads())         #查看进程包含的线程数量
# print(p.memory_percent())      #查看进程的内存使用率
# print(p.memory_info())         #查看进程rss、vms信息
# print(p.connections())         #获取进程的namedutples列表、fs、family、laddr等信息
# print(p.io_counters())         #查看进程的IO
# print(p.status())              #查看进程状态
# print(datetime.datetime.fromtimestamp(p.create_time()).strftime('%Y-%m-%d %H:%M:%S') )#查看进程的创建时间
# p.suspend()                    #挂起进程
# p.resume()                     #恢复
# p.kill()                       #杀死进程

# ipy模块主要对IP地址进制处理和转换；
#
# 复制代码
# from IPy import IP
# private_ipaddr=IP('192.168.0.0/24')
# public_ipaddr=IP('123.150.204.166')
# print(public_ipaddr.make_net('255.255.0.0')) #查询IP所在的网段
# print(public_ipaddr.reverseNames()) 　　　　　 #查看该IP地址的反向解析
# print(private_ipaddr.version()) 　　　　　　　  #查看IP地址的版本
# print(public_ipaddr.iptype())  　　　　　　　　  #查看是 私网地址？公网地址？
#
#
# ########################ip地址格式转换#####################
#
#
# print(private_ipaddr.int())     #转换成整型格式            3232235520
# print(private_ipaddr.strBin())  #把IP地址转换成二进制格式  11000000101010000000000000000000
# print(private_ipaddr.strHex())  #把IP地址转换成16进制格式  0xc0a80000
# 复制代码