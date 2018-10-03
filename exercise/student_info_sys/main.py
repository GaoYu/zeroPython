#练习:
#  1. 把学生管理系统划分为模块（把相关操作放在一个模块内）:
#    建议:
#       main.py 放主事件循环
#       menu.py 放show_menu函数
#       student_info.py 放学生信息相关的操作


'''定义一个主函数，用来获取键盘操作，实现选择的工作
'''
from menu import show_menu
from student_info import *

def main():
    docs = [] #此列表用来存储所有学生的信息字典
    while True:
        if __name__ == '__main__':
            show_menu()
            s = input("请选择：")
            if s == '1':
                docs += input_student()
            elif s =='2':
                output_student(docs)
            elif s =='3':
                modify_student_info(docs)
            elif s=='4':
                delete_student_info(docs)
            elif s =='5':
                get_score_rev(docs)
            elif s =='6':
                get_score(docs)
            elif s =='7':
                get_age_rev(docs)
            elif s =='8':
                get_age(docs)
            elif s =='q':
                return #结束此函数执行，直接退出
main()