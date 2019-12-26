#!/usr/bin/env python3 
# -*- coding:utf-8 -*-
# date:2019/12/26
__author__ = 'xxx'

# https://www.cnblogs.com/sss4/p/9869464.html  pip install pexpect
# 6.python远程登录Linux各模块小结
#
# fabric：方便与shell脚本结合，擅长批量部署，任务管理。
#
# paramiko：方便嵌套系统平台中，擅长远程执行命令，文件传输，自身不执行多进程；
#
# pexpect：擅长自动交互，比如ssh、ftp、telnet，原生支持多线程；
import pexpect
import sys

password = 'EC_history&LINGzhi'
ssh = pexpect.spawn('ssh root@10.102.6.38 -p 22')
status = ssh.expect(['password:', 'continue connecting (yes/no)?', pexpect.TIMEOUT, pexpect.EOF], timeout=50)
if status == 0:
    ssh.sendline(password)  # 注意输入密码 不要使用send 不需要\n回车！
elif status == 1:
    ssh.send('yes')
    ssh.expect('password: ')
    ssh.sendline(password)
elif status == 2:
    print('贱婢做了好久~做不到')
elif status == 3:
    print('贱婢死爹了，您请回！')
    sys.exit('Bye...')
index = ssh.expect(['#', pexpect.EOF, pexpect.TIMEOUT])
if index == 0:
    print('You were logged in as root.')
    ssh.sendline('su - oracle')
    ssh.sendline('whoami')
    status = ssh.expect(['oracle', pexpect.EOF, pexpect.TIMEOUT])
    if status == 0:
        print('切换到oracle用户！')

# pexpect的nteract() 和远程主机交互
password = 'EC_history&LINGzhi'
ssh = pexpect.spawn('ssh root@10.102.6.38 -p 22')
status = ssh.expect(['password:', 'continue connecting (yes/no)?', pexpect.TIMEOUT, pexpect.EOF], timeout=50)
if status == 0:
    ssh.sendline(password)  # 注意输入密码 不要使用send 不需要\n回车！
elif status == 1:
    ssh.send('yes')
    ssh.expect('password: ')
    ssh.sendline(password)
elif status == 2:
    print('贱婢做了好久~做不到')
elif status == 3:
    print('贱婢死爹了，您请回！')
    sys.exit('Bye...')
index = ssh.expect(['#', pexpect.EOF, pexpect.TIMEOUT])
if index == 0:
    print('You were logged in as root.')
    ssh.interact()  # 直接 进入远程主机交互式模式
