from db import modules
from lib import common

logger = common.get_logger("操作日志")


# 管理员：注册接口
def admin_registe_interface(name, password):
    admin_obj = modules.Admin.get_obj_name(name)
    if admin_obj:
        return False, '管理员已存在'
    else:
        modules.Admin(name, password)
        logger.info('管理员%s注册成功' % name)
        return True, '管理员注册成功'


# 管理员：创建学校接口
def create_school_interface(admin, school_name, addr):
    school_obj = modules.School.get_obj_name(school_name)
    if school_obj:
        return False, '学校已存在'
    else:
        admin_obj = modules.Admin.get_obj_name(admin)
        admin_obj.create_school(school_name, addr)
        logger.info('%s：%s学校创建成功' % (admin, school_name))
        return True, '%s：%s学校创建成功' % (admin, school_name)


# 管理员：创建老师接口
def create_teacher_interface(admin, name, password='123'):
    teacher_obj = modules.School.get_obj_name(name)
    if teacher_obj:
        return False, '该教师已存在'
    else:
        admin_obj = modules.Admin.get_obj_name(admin)
        admin_obj.create_teacher(name, password)
        logger.info('%s：%s教师创建成功' % (admin, name))
        return True, '%s：%s教师创建成功,初始密码为%s' % (admin, name, password)


# 管理员：创建课程接口
def create_course_interface(admin, name, price, period, school_name):
    course_obj = modules.Course.get_obj_name(name)
    if course_obj:
        return False, '该课程已存在'
    else:
        admin_obj = modules.Admin.get_obj_name(admin)
        admin_obj.create_course(name, price, period)

        school_obj = modules.School.get_obj_name(school_name)
        school_obj.add_course(name)

        logger.info('%s：%s课程创建成功' % (admin, name))
        return True, '%s：%s课程创建成功' % (admin, name)