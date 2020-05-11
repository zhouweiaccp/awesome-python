#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import subprocess

ss=os.system('dir')
print('type ----- %s'%type(ss))
read_fh=os.popen('dir').readlines()
print(type(read_fh))
for name in read_fh:
    print(name)
   # name = name.decode('gbk').encode('utf-8')


print('subprocess......')
#好处在于:运用对线程的控制和监控，将返回的结果赋于一变量，便于程序的处理
p = subprocess.Popen('ls *.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print( p.stdout.readlines())

for line in p.stdout.readlines():
    print (line)

retval = p.wait()

# (4)
# 使用模块commands模块
#
# 方法
# 说明
#
# getoutput
# 获取执行命令后的返回信息
#
# getstatus
# 获取执行命令的状态值(执行命令成功返回数值0，否则返回非0)
#
# getstatusoutput
# 获取执行命令的状态值以及返回信息
#
# >> > import commands
#
# >> > commands.getoutput('ls *.sh')
# 输出结果：
#
# 'install_zabbix.sh\nmanage_deploy.sh\nmysql_setup.sh\npython_manage_deploy.sh\nsetup.sh'
#
# >> > commands.getstatusoutput('ls *.sh')
# 输出结果：
#
# (0, 'install_zabbix.sh\nmanage_deploy.sh\nmysql_setup.sh\npython_manage_deploy.sh\nsetup.sh')
#
# import commands
#
# (status, output) = commands.getstatusoutput('cat /proc/cpuinfo')
#
# print
# status, output