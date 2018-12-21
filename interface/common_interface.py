from db import modules
from lib import common
import os
from conf import settings

logger = common.get_logger('操作日志')

#公共：登录接口
def login_interface(user_type, name, password):
    if user_type == 'admin':
        obj = modules.Admin.get_obj_name(name)
    elif user_type == 'teacher':
        obj = modules.Teacher.get_obj_name(name)
    elif user_type == 'student':
        obj = modules.Student.get_obj_name(name)
    else:
        return False, '模式不存在'
    if obj:
        if obj.password == password:
            return True, '%s : %s登录成功' % (user_type, name)
        else:
            return False, '密码错误'
    else:
        return False, '用户不存在'

#公共：查看所有所有学校
def check_all_school():
    path = os.path.join(settings.BASE_DB, 'school')
    return common.get_all_obj(path)

#公共：查看所有课程接口
def check_all_course():
    path = os.path.join(settings.BASE_DB, 'course')
    return common.get_all_obj(path)

#公共：查看日志记录接口
def check_log_interface(user_name):
    common.get_log_info(user_name)