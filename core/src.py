from core import admin, teacher, student

tag = True

choice_dict = {
    '1': admin.admin_main,
    '2': teacher.teacher_main,
    '3': student.student_main
}


def run():
    global tag
    while tag:
        print(
            '''
            1. 管理员视图
            2. 教师视图
            3. 学生视图
            q. 退出
            '''
        )
        choice = input('请选择：').strip()
        if choice == 'q':
            tag = False
            break
        if choice not in choice_dict: continue
        choice_dict[choice]()