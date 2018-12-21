选课系统目录结构
 |-----conf
 |      |-----settings.py 路径配置+日志配置
 |
 |-----core 用户核心
 |      |-----src.py      二级启动文件
 |      |-----admin.py    管理员功能层
 |      |-----teacher.py  教师功能层
 |      |-----student.py  学生功能层
 |
 |-----db 数据
 |      |-----db_handler.py  数据处理
 |      |-----modules.py     类及方法
 |
 |-----interface 接口层
 |      |-----common_interface.py  公共接口
 |      |-----admin_interface.py   管理员接口
 |      |-----teacher_interface.py 教师接口
 |      |-----student_interface.py 学生接口
 |
 |-----lib 公共方法
 |      |-----common.py  公共功能
 |
 |-----log 日志数据
 |      |-----operation.log 日志文件
 |
 |-----start.py   程序启动文件
