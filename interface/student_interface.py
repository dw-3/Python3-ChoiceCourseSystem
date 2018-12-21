from db import modules
from lib import common

logger = common.get_logger('操作日志')


# 学生：学生注册接口
def student_registe_interface(name, password):
    obj = modules.Student.get_obj_name(name)
    if obj:
        return False, '用户名已存在'
    else:
        modules.Student(name, password)
        logger.info('学生%s注册成功' % name)
        return True, '学生注册成功'


# 学生：选择学校接口
def choice_school_interface(stu_name, school_name):
    obj = modules.Student.get_obj_name(stu_name)
    if obj.school:
        return False, '您已选择过学校，无法再次选择'
    else:
        obj.choice_school(school_name)
        logger.info('%s选择学校%s成功' % (stu_name, school_name))
        return True, '%s选择学校%s成功' % (stu_name, school_name)


# 学生：根据学校查看所有课程接口
def check_all_course(stu_name):
    stu_obj = modules.Student.get_obj_name(stu_name)
    if stu_obj.school:
        school_obj = modules.School.get_obj_name(stu_obj.school)
        if school_obj.course_list:
            return True, school_obj.course_list
        else:
            return False, '该学校暂无课程'
    else:
        return False, '您还没选择学校'


# 学生：选择课程接口
def choice_course_interface(stu_name, course_name):
    stu_obj = modules.Student.get_obj_name(stu_name)
    if course_name in stu_obj.course_list:
        return False, '您已选择本门课程'
    stu_obj.add_course(course_name)
    course_obj = modules.Course.get_obj_name(course_name)
    course_obj.add_student(stu_name)
    logger.info('%s选择课程%s成功' % (stu_name, course_name))
    return True, '%s选择课程%s成功' % (stu_name, course_name)


# 学生：查看分数接口
def check_score_interface(stu_name):
    stu_obj = modules.Student.get_obj_name(stu_name)
    return stu_obj.score


# 学生：查看学生课程信息接口
def check_stu_course_interface(stu_name):
    stu_obj = modules.Student.get_obj_name(stu_name)
    if stu_obj.course_list:
        return True, stu_obj.stu_tell_info()
    else:
        return False, '暂无课程，请先选择课程'