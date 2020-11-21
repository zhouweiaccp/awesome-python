# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 20:57
# @Author  : play4fun
# @File    : 午夜生成新log1.py
# @Software: PyCharm

"""
通过logging.basicConfig函数对日志的输出格式及方式做相关配置.py:

logging.basicConfig函数各参数:
filename: 指定日志文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
 %(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s: 打印当前执行程序名
 %(funcName)s: 打印日志的当前函数
 %(lineno)d: 打印日志的当前行号
 %(asctime)s: 打印日志的时间
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID
 %(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

午夜生成新log1.py: https://github.com/makelove/Python_Master_Courses/blob/3241175d3565eb7d3818884d40f4fba9bbf7a101/Python3.6/logging1/午夜生成新log1.py#L14
"""
from time import sleep
import logging
from logging.handlers import TimedRotatingFileHandler

logHandler = TimedRotatingFileHandler(filename="logs/logfile", when="midnight")
logFormatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logHandler.setFormatter(logFormatter)

logger = logging.getLogger('MyLogger')
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

while True:
    for k in range(5):
        logger.info("Line %d" % k)
        sleep(3)