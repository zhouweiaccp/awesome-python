#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# demo - 当前Project名称;
# use_logbook - 在创建文件的对话框中指定的文件名;
# chive - 当前用户名;
# 2019/10/2922:46 - 当前系统日期;
# 554961776@qq.com
# https://www.cnblogs.com/imyalost/p/9026379.html
import os
import sys
import logbook
from logbook import Logger,StreamHandler,FileHandler,TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler

def log_type(record,handler):
    log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
        date = record.time,                              # 日志时间
        level = record.level_name,                       # 日志等级
        filename = os.path.split(record.filename)[-1],   # 文件名
        func_name = record.func_name,                    # 函数名
        lineno = record.lineno,                          # 行号
        msg = record.message                             # 日志内容
    )
    return log

# 日志存放路径
LOG_DIR = os.path.join("Log")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
# 日志打印到屏幕
log_std = ColorizedStderrHandler(bubble=True)
log_std.formatter = log_type
# 日志打印到文件
log_file = TimedRotatingFileHandler(
    os.path.join(LOG_DIR, '%s.log' % 'log'),date_format='%Y-%m-%d', bubble=True, encoding='utf-8',backup_count=2)
log_file.formatter = log_type

# 脚本日志
run_log = Logger("script_log")
def init_logger():
    logbook.set_datetime_format("local")
    run_log.handlers = []
    run_log.handlers.append(log_file)
    run_log.handlers.append(log_std)

# 实例化，默认调用
logger = init_logger()

# actions are:
# notice / info / trace / warn / error / critical

if __name__ == '__main__':
    run_log.notice('ddddddd',2123)
    run_log.info("测试log模块，暂时就优化到这一步，后续再改进")