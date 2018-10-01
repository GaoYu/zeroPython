﻿#练习:
#  1. 把学生管理系统划分为模块（把相关操作放在一个模块内）:
#    建议:
#       main.py 放主事件循环
#       menu.py 放show_menu函数
#       student_info.py 放学生信息相关的操作

#3.写一个打印菜单的函数

def show_menu():
    print('+--------------------------------------------+')
    print('|  1) 添加学生信息                           |')
    print('|  2) 查看所有学生信息                       |')
    print('|  3) 修改学生的成绩                         |')
    print('|  4) 删除学生信息                           |')
    print('|  5) 按成绩从高至低打印学生信息             |')
    print('|  6) 按成绩从低至高打印学生信息             |')
    print('|  7) 按年龄从大到小打印学生信息             |')
    print('|  8) 按年龄从小到大打印学生信息             |')
    print('|  q) 退出                                   |')
    print('+--------------------------------------------+')
   