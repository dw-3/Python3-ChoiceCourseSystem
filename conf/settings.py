import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BASE_DB=os.path.join(BASE_DIR,'db')


standard_format = '[%(asctime)s][task_id:%(name)s]' \
                  '[%(levelname)s]< %(message)s >'  # 其中name为getlogger指定的名字

id_simple_format = '[%(asctime)s][task_id:%(name)s] %(message)s'

LOG_PATH = os.path.join(BASE_DIR, 'log', 'operation.log')  # 日志路径


LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': id_simple_format
        },
    },
    'filters': {},
    'handlers': {
        # 打印到终端的日志,使用的格式为 simple_format
        'ch': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        # 打印到文件的日志,使用的格式为 standard_format
        'default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'formatter': 'standard',
            'filename': LOG_PATH,  # 日志文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        '': {
            'handlers': ['ch', 'default'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}