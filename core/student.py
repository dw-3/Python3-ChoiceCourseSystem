from core import src
from interface import student_interface, common_interface
from lib import common

student_info = {
    'name': None
}


def student_registe():
    print('学生注册'.center(40, '-'))
    if student_info['name']:
        print('您已登录，无法注册')
        return
    while True:
        name = input('请输入名字：').strip()
        password = input('请输入密码：').strip()
        password1 = input('请确认密码：').strip()
        if not name or not password: continue
        if password == password1:
            state, msg = student_interface.student_registe_interface(name, password)
            if state:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


def student_login():
    print('学生登录'.center(40, '-'))
    if student_info['name']:
        print('您已登录，无需再登录')
        return
    while True:
        name = input('请输入名字：').strip()
        password = input('请输入密码：').strip()
        if not name or not password: continue
        state, msg = common_interface.login_interface('student', name, password)
        if state:
            print(msg)
            student_info['name'] = name
            break
        else:
            print(msg)


@common.auth(user_type='student')
def choose_school():
    print('选择学校'.center(40, '-'))
    while True:
        school_list = common_interface.check_all_school()
        if school_list:
            for i, school in enumerate(school_list):
                print('%s : %s' % (i, school))
            choice = input('请选择(学校)：').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice >= len(school_list): continue
                state, msg = student_interface.choice_school_interface(student_info['name'], school_list[choice])
                if state:
                    print(msg)
                    break
                else:
                    print(msg)
                    break
            else:
                print('请输入数字')
        else:
            print('暂无学校')
            break


@common.auth(user_type='student')
def choose_course():
    print('选择课程'.center(40, '-'))
    while True:
        state, msg = student_interface.check_all_course(student_info['name'])
        if state:
            for i, course in enumerate(msg):
                print('%s : %s' % (i, course))
            choice = input('选择课程(学生)：').strip()
            if choice.isdigit():
                choice = int(choice)
                if choice >= len(msg): continue
                flag, mssg = student_interface.choice_course_interface(student_info['name'], msg[choice])
                if flag:
                    print(mssg)
                    break
                else:
                    print(mssg)
                    break
            else:
                print('请输入数字')
        else:
            print(msg)
            break


@common.auth(user_type='student')
def check_score():
    print('查看成绩'.center(40, '-'))
    score_dict = student_interface.check_score_interface(student_info['name'])
    for k, v in score_dict.items():
        print('课程：%s\t 成绩：%s' % (k, v))


@common.auth(user_type='student')
def check_log():
    common_interface.check_log_interface(student_info['name'])


@common.auth(user_type='student')
def check_course():
    print('查看课程信息'.center(40, '-'))
    state, msg = student_interface.check_stu_course_interface(student_info['name'])
    if state:
        pass
    else:
        print(msg)


choice_dict = {
    '1': student_registe,
    '2': student_login,
    '3': choose_school,
    '4': choose_course,
    '5': check_score,
    '6': check_log,
    '7': check_course

}


def student_main():
    while True:
        print(
            '''
            1. 注册
            2. 登录
            3. 选择学校
            4. 选择课程
            5. 查看成绩
            6. 查看操作日志
            7. 查看课程信息
            q. 退出
            '''
        )
        choice = input('请选择(学生)：').strip()
        if choice == 'q':
            src.tag = False
            break
        if choice not in choice_dict: continue
        choice_dict[choice]()