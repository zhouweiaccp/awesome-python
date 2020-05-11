import logging
import os
from logging.handlers import TimedRotatingFileHandler
import coloredlogs
# 设置颜色
coloredlogs.DEFAULT_FIELD_STYLES = {'asctime': {'color': 'green'}, 'hostname': {'color': 'magenta'},
                                    'levelname': {'color': 'green', 'bold': True}, 'request_id': {'color': 'yellow'},
                                    'name': {'color': 'blue'}, 'programname': {'color': 'cyan'},
                                    'threadName': {'color': 'yellow'}}
 
 
class Log:
    __instances = {}
 
    @classmethod
    def getLogger(cls, name=os.path.abspath(__name__)):
        if name not in cls.__instances:
            BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            log_dir = 'logs'
            if not log_dir.startswith('/'):
                log_dir = os.path.join(BASE_DIR, log_dir)

            if not os.path.isdir(log_dir):
                os.makedirs(log_dir, mode=0o755)
 
            log_file = os.path.join(log_dir, "app.log")
            logger = logging.getLogger(name)
            fmt = '%(asctime)s [%(levelname)s] [%(name)s] %(filename)s[line:%(lineno)d] [%(threadName)s] %(message)s'
            formater = logging.Formatter(fmt)
 
            ch = logging.StreamHandler()
            ch.setLevel(Log.__getLogLevel())
            ch.setFormatter(formater)
            logger.addHandler(ch)
 
            coloredlogs.install(fmt=fmt, level=Log.__getLogLevel(), logger=logger)
 
            fh = TimedRotatingFileHandler(log_file, when='M', interval=1, backupCount=7, encoding='utf-8')
            fh.setLevel(Log.__getLogLevel())
            fh.setFormatter(formater)
            logger.setLevel(Log.__getLogLevel())
            logger.addHandler(fh)
            cls.__instances[name] = logger
        return cls.__instances[name]
 
    @staticmethod
    def __getLogLevel():
        return logging.INFO
 
 
if __name__ == '__main__':
    Log.getLogger().error('log测试数据')
    Log.getLogger().info('log测试数据')
    Log.getLogger().warning('log测试数据')
    Log.getLogger().debug('log测试数据')