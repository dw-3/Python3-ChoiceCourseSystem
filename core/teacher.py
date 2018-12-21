from core import src
from interface import common_interface, teacher_interface
from lib import common

teacher_info = {
    'name': None
}


def teacher_login():
    print('教师登录'.center(40, '-'))
    if teacher_info['name']:
        print('您已登录，无需再登录')
        return
    while True:
        name = input('请输入名字：').strip()
        password = input('请输入密码：').strip()
        if not name or not password: continue
        state, msg = common_interface.login_interface('teacher', name, password)
        if state:
            print(msg)
            teacher_info['name'] = name
            break
        else:
            print(msg)


@common.auth(user_type='teacher')
def choose_course():
    print('选择课程'.center(40,'-'))
    course_list = common_interface.check_all_course()
    if course_list is None:
        print('暂无课程')
    else:
        for i, course in enumerate(course_list):
            print('%s ： %s' % (i, course))
        choice = input('请选择(课程)：').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= len(course_list): return
            state, msg = teacher_interface.choose_course_interface(teacher_info['name'], course_list[choice])
            if state:
                print(msg)
            else:
                print(msg)
        else:
            print('请输入整数')


@common.auth(user_type='teacher')
def check_course():
    print('查看课程'.center(40, '-'))
    state, msg, _ = teacher_interface.check_tea_course_interface(teacher_info['name'])
    if state:
        pass
    else:
        print(msg)


@common.auth(user_type='teacher')
def check_student():
    print('查看学生'.center(40, '-'))
    _, _, course_list = teacher_interface.check_tea_course_interface(teacher_info['name'])
    if course_list is None: return
    for i, course in enumerate(course_list):
        print('%s ：课程 %s' % (i, course))
    choice = input('请选择课程：').strip()
    if choice.isdigit():
        choice = int(choice)
        if choice >= len(course_list):
            print('输入的数字超过范围')
        else:
            state,student_list = teacher_interface.check_student_interface(course_list[choice])
            if state:
                for k, v in enumerate(student_list):
                    print('%s ：学生 %s' % (k, v))
            else:print(student_list)
    else:
        print('请输入数字')


@common.auth(user_type='teacher')
def set_stu_score():
    print('为学生打分'.center(40, '-'))
    _, _, course_list = teacher_interface.check_tea_course_interface(teacher_info['name'])
    if course_list is None:
        print('暂无课程，请先去选择课程')
        return
    while True:
        for i, course in enumerate(course_list):
            print('%s ：课程 %s' % (i, course))
        choice_course = input('请选择课程：').strip()
        if choice_course.isdigit():
            choice_course = int(choice_course)
            if choice_course >= len(course_list):
                print('输入的数字超过范围')
                continue
            else:
                state,student_list = teacher_interface.check_student_interface(course_list[choice_course])
                if state:
                    for k, v in enumerate(student_list):
                        print('%s ：学生 %s' % (k, v))
                    choice_stu = input('请选择要打分的学生：').strip()
                    if choice_stu.isdigit():
                        choice_stu = int(choice_stu)
                        if choice_stu >= len(course_list):
                            print('输入的数字超过范围')
                        else:
                            score = input('请输入分数(打分)：').strip()
                            if score.isdigit():
                                msg = teacher_interface.mark_student_interface(teacher_info['name'],
                                                                               student_list[choice_stu],
                                                                               course_list[choice_course], score)
                                print(msg)
                                break
                            else:
                                print('请输入数字，亲')
                    else:
                        print('请输入数字，亲')
                else:
                    print(student_list)
        else:
            print('请输入数字，亲')

@common.auth(user_type='teacher')
def check_log():
    common_interface.check_log_interface(teacher_info['name'])

choice_dict = {
    '1': teacher_login,
    '2': choose_course,
    '3': check_course,
    '4': check_student,
    '5': set_stu_score,
    '6': check_log

}


def teacher_main():
    while src.tag:
        print(
            '''
               1. 登录
               2. 选择课程
               3. 查看课程
               4. 查看学生
               5. 修改学生成绩
               6. 查看操作日志
               q. 退出
            '''
        )
        choice = input('请选择(教师)：').strip()
        if choice == 'q':
            src.tag = False
            break
        if choice not in choice_dict: continue
        choice_dict[choice]()