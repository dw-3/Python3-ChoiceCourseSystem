from db import modules
from lib import common

logger = common.get_logger('操作日志')


# 老师：选择课程接口
def choose_course_interface(tea_name, course_name):
    '''选择课程'''
    obj = modules.Teacher.get_obj_name(tea_name)
    if course_name in obj.course_list:
        return False, '课程已存在,无法添加'
    else:
        obj.add_course(course_name)
        logger.info('%s选择课程%s成功' % (tea_name, course_name))
        return True, '%s选择课程%s成功' % (tea_name, course_name)


# 老师：查看老师课程接口
def check_tea_course_interface(tea_name):
    '''查看课程'''
    tea_obj = modules.Teacher.get_obj_name(tea_name)
    if not tea_obj.course_list:
        return False, '暂无课程，请先选择课程', None
    # course_dict_info={}  方式二（未测试）
    # for course in tea_obj.course_list:
    #     course_obj=modules.Course.get_obj_name(course)
    #     course_dict_info[course_obj.name]={'价格':course_obj.price,'周期':course_obj.period}
    # return True,course_dict_info
    else:                 #方式一
        return True, tea_obj.tea_tell_info(), tea_obj.course_list


# 老师：查看学生接口
def check_student_interface(course_name):
    '''查看学生'''
    course_obj = modules.Course.get_obj_name(course_name)
    if not course_obj.student_list:
        return False, '暂无学生'
    return True, course_obj.student_list


# 老师：为学生打分接口
def mark_student_interface(tea_name, stu_name, course_name, score):
    tea_obj = modules.Teacher.get_obj_name(tea_name)
    stu_obj = modules.Student.get_obj_name(stu_name)
    tea_obj.mark_student(stu_obj, course_name, score)
    logger.info('%s 修改 %s 的 %s 课程成绩成功！' % (tea_name, stu_name, course_name))
    return '%s 修改 %s 的 %s 课程成绩成功！' % (tea_name, stu_name, course_name)