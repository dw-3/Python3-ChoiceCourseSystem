from db import db_handler


class BaseClass():
    '''超类'''

    def save(self):
        db_handler.save(self)

    @classmethod
    def get_obj_name(cls, name):
        return db_handler.select(name, cls.__name__.lower())


class Admin(BaseClass):
    '''管理员类'''

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.save()

    def create_school(self, school_name, addr):
        School(school_name, addr)

    def create_course(self, name, price, period):
        Course(name, price, period)

    def create_teacher(self, name, password):
        Teacher(name, password)


class Teacher(BaseClass):
    '''老师类'''

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.course_list = []
        self.save()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()

    def tea_tell_info(self):
        for cours in self.course_list:
            cours_obj=Course.get_obj_name(cours)
            cours_obj.tell_info()

    def mark_student(self,student,course_name,score):
        student.score[course_name] = score
        student.save()


class Student(BaseClass):
    '''学生类'''

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.school = None
        self.course_list = []
        self.score = {}
        self.save()

    def choice_school(self, schoolname):
        self.school = schoolname
        self.save()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.score[course_name] = 0
        self.save()

    def stu_tell_info(self):
        for cours in self.course_list:
            cours_obj=Course.get_obj_name(cours)
            cours_obj.tell_info()


class School(BaseClass):
    '''学校类'''

    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.course_list = []
        self.save()

    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()


class Course(BaseClass):
    '''课程类'''

    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period
        self.student_list = []
        self.save()

    def add_student(self, stu_name):
        self.student_list.append(stu_name)
        self.save()

    def tell_info(self):
        print('课程名：%s  价格：%s  周期：%s' % (self.name, self.price, self.period))