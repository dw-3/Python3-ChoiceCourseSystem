import logging.config,os
from conf import settings


def auth(user_type):
    from core import admin, teacher, student
    def validation(func):
        def wrapper(*args,**kwargs):
            if user_type=='admin':
                if not admin.admin_info['name']:
                    admin.admin_login()
                else:
                    func(*args,**kwargs)
            elif user_type=='teacher' :
                if not teacher.teacher_info['name']:
                    teacher.teacher_login()
                else:
                    func(*args,**kwargs)
            elif user_type=='student':
                if not student.student_info['name']:
                    student.student_login()
                else:
                    func(*args,**kwargs)
        return wrapper
    return validation



def get_all_obj(path):
    '''得到路径下所有对象'''
    obj_path = os.path.join(settings.BASE_DB, path)
    if os.path.exists(obj_path):
        obj_list = os.listdir(obj_path)
        return obj_list
    else:
        return None



def get_logger(name):
    '''日志模块'''
    logging.config.dictConfig(settings.LOGGING_DIC)
    logger = logging.getLogger(name)
    return logger


def get_log_info(user_name):
    with open(settings.LOG_PATH,'rt',encoding='utf-8')as f:
        for names in f.readlines():
            if user_name in names:
                print(names)