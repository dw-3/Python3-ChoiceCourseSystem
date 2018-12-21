from core import src
from interface import admin_interface, common_interface, teacher_interface, student_interface
from lib import common

admin_info = {
    'name': None
}


def admin_registe():
    print('管理员注册'.center(40, '-'))
    if admin_info['name']:
        print('您已登录，无法注册')
        return
    while True:
        name = input('请输入名字：').strip()
        password = input('请输入密码：').strip()
        password1 = input('请确认密码：').strip()
        if not name or not password: continue
        if password == password1:
            state, msg = admin_interface.admin_registe_interface(name, password)
            if state:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('两次密码不一致')


def admin_login():
    print('管理员登录'.center(40, '-'))
    if admin_info['name']:
        print('您已登录')
        return
    while True:
        name = input('请输入名字：').strip()
        password = input('请输入密码：').strip()
        if not name or not password: continue
        state, msg = common_interface.login_interface('admin', name, password)
        if state:
            print(msg)
            admin_info['name'] = name
            break
        else:
            print(msg)


@common.auth(user_type='admin')
def create_school():
    print('创建学校'.center(40, '-'))
    name = input('请输入学校名称：').strip()
    addr = input('请输入学校地址：').strip()
    if not name or not addr:
        print('不可为空')
        return
    state, msg = admin_interface.create_school_interface(admin_info['name'], name, addr)
    if state:
        print(msg)
    else:
        print(msg)


@common.auth(user_type='admin')
def create_teacher():
    print('创建教师'.center(40, '-'))
    name = input('请输入教师名字：').strip()
    if not name:
        print('不可为空')
        return
    state, msg = admin_interface.create_teacher_interface(admin_info['name'], name)
    if state:
        print(msg)
    else:
        print(msg)


@common.auth(user_type='admin')
def create_corse():
    print('创建课程'.center(40, '-'))
    while True:
        school_list = common_interface.check_all_school()
        if school_list:
            for i, school in enumerate(school_list):
                print('%s : %s' % (i, school))
        choice = input('请选择学校：').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >= len(school_list): continue
            name = input('请输入课程名字：').strip()
            price = input('请输入课程价格：').strip()
            period = input('请输入课程周期：(mouth)').strip()
            if not name or not price or not period: continue
            state, msg = admin_interface.create_course_interface(admin_info['name'], name, price, period,
                                                                 school_list[choice])
            if state:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('请输入整数')


@common.auth(user_type='admin')
def check_log():
    common_interface.check_log_interface(admin_info['name'])


choice_dict = {
    '1': admin_registe,
    '2': admin_login,
    '3': create_school,
    '4': create_teacher,
    '5': create_corse,
    '6': check_log

}


def admin_main():
    while True:
        print('管理员界面'.center(60, '-'))
        print(
            '''
               1. 注册
               2. 登录
               3. 创建学校
               4. 创建老师
               5. 创建课程
               6. 查看操作日志
               q. 退出
            '''
        )
        choice = input('请选择(管理员)：').strip()
        if choice == 'q':
            src.tag = False
            break
        if choice not in choice_dict: continue
        choice_dict[choice]()
